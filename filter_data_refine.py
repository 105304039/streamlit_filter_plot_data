import streamlit as st
import pandas as pd
import numpy as np
from plotly_module import graph_parameters

# Styling
#  https://discuss.streamlit.io/t/how-to-style-a-selectbox/45465
#  https://discuss.streamlit.io/t/how-to-style-slider-annotations/24177
#  https://stackoverflow.com/questions/74611608/how-to-change-the-height-of-streamlit-sidebar
#  create anchor link: https://github.com/dataprofessor/streamlit/blob/main/anchor_app.py
st.set_page_config(layout="wide")

with st.sidebar:
    st.markdown('''
# Sections
- [Select data](#select-data)
- [Glance at data](#glance-at-data)
- [Visualization](#visualization)
''', unsafe_allow_html=True)
    df_up = st.file_uploader("Choose a file",type = ["csv","xlsx"])
    if df_up!=None:
        if df_up.name[::-1][:df_up.name[::-1].find(".")]=="vsc":
            df=pd.read_csv(df_up)
        else:
            df_all=pd.read_excel(df_up,sheet_name = None)
            if len(df_all)==1:
                df = list(df_all.values())[0]
            else:
                sheetname = st.selectbox("Sheet name",list(df_all.keys()))
                df = df_all[sheetname]
    else:
        df = pd.read_csv("https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv")
    st.write("Data Types for file")
    st.dataframe(df.dtypes.astype(str).reset_index().rename(columns = {0:"Data type","index":"Column name"}))


st.markdown(
    """
    <style>
    .stDataFrame[data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 500px;
    }
    section[data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 500px;
        margin-left: -500px;
    }
    [data-baseweb="select"] {
        margin-top: -10px;
    }
    [data-baseweb="input"] {
        margin-top: -20px;
    }
    [data-baseweb="slider"] {
        margin-top: -15px;
        padding-left: 15px;
        padding-top: 15px;
    }
    [data-testid="stTickBar"] {margin-top: -5px;}
    [data-testid="stTickBarMin"] {font-size: 8px;margin-top: 0px;}
    [data-testid="stThumbValue"] {margin-top: 3px;}
    [data-testid="stTickBarMax"] {font-size: 8px;margin-top: 0px;}
    [data-testid="tag"] {font-size: 10px;}
    [data-testid="stHorizontalBlock"] .stButton>button{
        background-color: #e6e7e8;
        border-radius: 30px;
        margin-top: 20px;}

    
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Filtering and Drawing!")
st.session_state["data"] = None
if 'open' not in st.session_state:  
    st.session_state["open"] = {}

class data_conditions():
    def __init__(self,data):
        self.data = data
        self.conditions = pd.Series(np.full(data.shape[0],True),index = data.index)
def read_con(sign,bools_org,bools_new):
    if sign=="AND":
        return bools_org&bools_new
    elif sign=="OR":
        return bools_org|bools_new
    else:
        return bools_org&(~bools_new)
def read_default_filter(i,current_range):
    return st.session_state["open"][i]["Filters"] if ("Filters" in  st.session_state["open"][i].keys()) else current_range if (i in st.session_state["open"].keys()) else current_range
#-------------------------------------Adding Filters--------------------------------------
st.header('Select data')
bl,br = st.columns([10,1])
the_but = bl.button(f'Add filter',key = 0)
if the_but:
    # 每當按下「Add filter」，在session_state["open"]的字典中，新增第i個紀錄的key (從0開始編號)
    add_rec = max(st.session_state["open"].keys())+1 if st.session_state["open"]!={} else 0  
    st.session_state["open"][add_rec] = {}
clean = br.button(f'Reset',key = 1)
if clean:
    st.session_state["open"] = {} # 清空記憶
#-------------------------------------Filters parameters--------------------------------------

with st.container():
    co1_top,co2_top,co3_top,co4_top,co5_top = st.columns([1,3,2,5,1])
    co1_top.write("Condition")
    co2_top.write('Variable')
    co3_top.write('Data type')
    co4_top.write('Filters')
    co5_top.write('Delete')

DC = data_conditions(df)
con_options = ("AND", "OR", "NOT")
var_options = list(df.columns)
dtype_options = ('',"Numeric","Categorical","Time")
if st.session_state["open"]!={}:
    i = 0 
    while (i<=max(st.session_state["open"].keys())): 
        if i not in st.session_state["open"].keys():
            i+=1
            continue
        else:
            with st.container():
                co1,co2,co3,co4,co5 = st.columns([1,3,2,5,1]) 
                if st.session_state["open"][i]!={}:  # 當存在輸入紀錄
                    option = co1.selectbox("",con_options,key = f"option_{i}",
                                           index = con_options.index(st.session_state["open"][i]["Condition"]))
                    var = co2.selectbox("",var_options,key = f"var_{i}",
                                        index = var_options.index(st.session_state["open"][i]["Variable"]))
                    dtype = co3.selectbox("",dtype_options,key = f"dtype_{i}",
                                          index = dtype_options.index(st.session_state["open"][i]["Data type"]),
                                          format_func = lambda x: 'Select an option' if x == '' else x)
                    st.session_state["open"][i].update({"Condition":option,"Variable":var,"Data type":dtype})
                else:                               # 不存在輸入紀錄
                    option = co1.selectbox("",con_options,key = f"option_{i}")
                    var = co2.selectbox("",var_options,key = f"var_{i}")
                    dtype = co3.selectbox("",dtype_options,
                                          format_func=lambda x: 'Select an option' if x == '' else x,key = f"dtype_{i}")
                    st.session_state["open"][i] = {"Condition":option,"Variable":var,"Data type":dtype}
                if dtype:
                    if dtype=="Categorical":
                        full_cat_options = list(df[var].unique())
                        user_input = co4.multiselect("",full_cat_options,key = f"cat_{i}",
                                                     default=read_default_filter(i,full_cat_options))
                        DC.conditions = read_con(option,DC.conditions,df[var].isin(user_input))
                    elif dtype=="Numeric":
                        _min, _max = float(df[var].min()),float(df[var].max())
                        step = (_max - _min) / 100
                        user_input = co4.slider(f"",min_value=_min,max_value=_max,step=step,key = f"num_{i}",
                                                value = read_default_filter(i,[_min,_max]))
                        DC.conditions = read_con(option,DC.conditions,df[var].between(*user_input))
                    else:
                        time_sr = pd.to_datetime(df[var].astype(str))
                        user_input = co4.date_input("",value=read_default_filter(i,(time_sr.min(),time_sr.max())),key = f"time_{i}")

                        if len(user_input) == 2:
                            user_input = tuple(map(pd.to_datetime, user_input))
                            start_date, end_date = user_input
                            DC.conditions = read_con(option,DC.conditions, time_sr.between(start_date, end_date))
                    st.session_state["open"][i]["Filters"]=user_input
                if co5.button("X",key = f"del_{i}"):
                    del st.session_state["open"][i]
                    st.experimental_rerun()
                i+=1

#-----------------------Displaying Filtered Data and Interactive Plots---------------------------
st.header('Glance at data')
with st.container():
    st.write(f"Filtered Dataset: obs. = {DC.data[DC.conditions].shape[0]}")
    st.session_state["data"] = DC.data[DC.conditions]
    # if DC.data[DC.conditions].shape[0]>500:
    if st.session_state["data"].shape[0]>500:
        st.write("(Displays top 500 rows)")
    st.dataframe(st.session_state["data"].iloc[:500])
    # graph_parameters(st.session_state["data"])
    st.header('Visualization')
    graph_parameters(st.session_state["data"])
    # expander = st.expander("Generate interactive diagram!")
    # with st.expander("Generate interactive diagram!"):
    #     graph_parameters(st.session_state["data"])