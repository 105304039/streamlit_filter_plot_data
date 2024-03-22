# streamlit_filter_plot_data
Selecting data and drawing interactive plot. In this program, users can upload files with a csv file or xlsx file as the desired dataset. The default dataset is penguins dataset ([reference](https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv)).
## Execution
Need to install streamlit package: `pip install streamlit`<br>
When executing scripts in Google Colab, I use public IP as the password to the local tunnel.
Run the command below in Google Colab: <br>
`!streamlit run filter_data_refine.py & >/content/logs.txt & npx localtunnel --port 8501 & curl ipv4.icanhazip.com`<br>
The detailed information is in the comment section [here](https://discuss.streamlit.io/t/how-to-launch-streamlit-app-from-google-colab-notebook/42399) written by Kalin in May 2023.

## Web Design
* CSS and streamlit.markdown()
  I use `streamlit markdown()` to customize CSS styles.<br>
  ```
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
        margin-top: -8px;
    }
    [data-baseweb="input"] {
        margin-top: -8px;
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
    unsafe_allow_html=True)
  ```
* sections of webpage: Select data, Glance at data, Visualization<br>
  1. Select data, Glance at data<br>
  ![image](https://github.com/105304039/streamlit_filter_plot_data/blob/main/filer%20and%20display.png)<br>
  2. Visualization<br>
  ![image](https://github.com/105304039/streamlit_filter_plot_data/blob/main/visualize.png)

## Demo
The gif below shows how the updates of data change the plots.<br>
![image](https://github.com/105304039/streamlit_filter_plot_data/blob/main/demo.gif)
