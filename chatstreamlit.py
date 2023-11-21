import streamlit as st
from pyecharts import Line
from pyecharts.charts import Line
from pyecharts import options as opts

# Function to create a line chart using Echarts
def create_chart():
    line_chart = (
        Line()
        .add_xaxis(["January", "February", "March", "April", "May", "June"])
        .add_yaxis("Series 1", [1, 2, 3, 4, 5, 6])
        .add_yaxis("Series 2", [2, 3, 4, 5, 6, 7])
        .set_global_opts(title_opts=opts.TitleOpts(title="Chart_name"))
    )
    return line_chart

# Layout the app according to the mockup
st.sidebar.image("panda.png", use_column_width=True)
st.sidebar.title("Navigation")
st.sidebar.button('Page 1')
st.sidebar.button('Page 2')
st.sidebar.button('Page 3')
st.sidebar.checkbox("Checkbox 01")
st.sidebar.checkbox("Checkbox 02")
st.sidebar.selectbox("ComboBox", ["Option 1", "Option 2", "Option 3"])

# Main content
st.header("My_app_name")
st.write("Content goes here...")

# Create and display the chart
chart = create_chart()
st_echarts(options=chart.dump_options(), height="500px")

# Button to download chart data
if st.button('Download Chart data'):
    # Logic to download chart data
    st.write("Download logic goes here...")
