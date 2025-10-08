import streamlit as slt
import plotly.express as plty_exp
from functions import data_source as ds

slt.title("In Search For Happiness")

x_data_option = slt.selectbox("Select the data for the X Axis:", ("GDP",
                                                                  "Happiness", "Generosity"))
y_data_option = slt.selectbox("Select the data for the Y Axis:", ("GDP",
                                                                  "Happiness", "Generosity"))
slt.subheader(f"{x_data_option} and {y_data_option}")

x_value, y_value = ds.get_remote_mapping_data(x_data_option, y_data_option)

graph = plty_exp.scatter(x=x_value, y=y_value, labels={"x": x_data_option,
                                                       "y": y_data_option})
slt.plotly_chart(graph)

