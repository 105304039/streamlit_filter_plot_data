import time

import streamlit as st
import numpy as np
import pandas as pd
# import plotly.figure_factory as ff
import plotly.express as px


def graph_parameters(df1,col_ratio = (2,1)):

    st.header(f"Drawing parameters")
    graph = st.selectbox("Drawing Type",["histogram","bar","scatter","line"])

    col1, col2 = st.columns(col_ratio) # 比例問題    
    with col1:
        lookat = st.selectbox("x:", df1.columns)
        code2 = f"""px.{graph}(data, x = '{lookat}'"""
        yoptions = st.multiselect('y:',list(df1.columns),default = [])
        y = yoptions if len(yoptions)>1 else yoptions[0] if len(yoptions)>0 else None

    with col2:
        args = {"color":st.selectbox("color:", [None]+list(df1.columns))}
        if graph!="histogram":
            args["text"] = st.selectbox("text:", [None]+list(df1.columns)) 
            if graph!="bar":
                args["symbol"] = st.selectbox("symbol:", [None]+list(df1.columns))
                if graph!="line":
                    args["size"] = st.selectbox("size:", [None]+list(df1.dtypes[(df1.dtypes=="float")|(df1.dtypes=="int64")|(df1.dtypes=="int32")].index))
        if graph!="line":
            args["opacity"] = st.slider('Opacity', 0.0, 1.0, 0.8)

    with st.container():           
        if graph=="histogram":
            fig = px.histogram(df1, x = lookat, y = y,**args)
        elif graph=="bar":
            fig = px.bar(df1, x = lookat, y = y,**args)
        elif graph=="scatter":
            fig = px.scatter(df1, x = lookat, y = y,**args)
        else:
            fig = px.line(df1, x = lookat, y = y,**args)
        st.plotly_chart(fig, use_container_width=True)

