# streamlit_filter_plot_data
Selecting data and drawing interactive plot. In this program, users can upload files with a csv file or xlsx file as the desired dataset. The default dataset is penguins dataset ([reference](https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv)).
## Requirements
Need to install streamlit package: `pip install streamlit`<br>
When executing scripts in Google Colab, I use public IP as the password to the local tunnel. <br>
Run the command below in Google Colab:
`!streamlit run filter_data_refine.py & >/content/logs.txt & npx localtunnel --port 8501 & curl ipv4.icanhazip.com`<br>
The detailed information is in the comment section [here](https://discuss.streamlit.io/t/how-to-launch-streamlit-app-from-google-colab-notebook/42399) written by Kalin in May 2023).

## Web Design
* CSS and streamlit.markdown()
* sections of webpage: Select data, Glance at data, Visualization<br>
1. Select data, Glance at data<br>
![image](https://github.com/105304039/streamlit_filter_plot_data/blob/main/filer%20and%20display.png)<br>
2. Visualization<br>
![image](https://github.com/105304039/streamlit_filter_plot_data/blob/main/visualize.png)

## Demo
The gif below shows how the updates of data change the plots.<br>
![image](https://github.com/105304039/streamlit_filter_plot_data/blob/main/demo.gif)
