import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from required_funcs import csv_file,input_data

st.set_page_config(page_title="Graph-plotting Tool", page_icon="📊", menu_items={
        "Get Help": None,
        "Report a Bug": None,
        "About": None
    }) # The first code line

st.markdown('<h1 style="text-align: center;">EasyGraph Plot</h1>', unsafe_allow_html=True)

state = st.session_state
state.graph_type = st.selectbox(label="What kind of Graph do you want to make?:",options=["Line plot","Scatter plot","Bar plot"],index=None)

# Common variables for all plots
state.x_column = "" if "x_column" not in state else state.x_column
state.y_column = "" if "y_column" not in state else state.y_column # requires if-else pair
state.x_label = "" if "x_label" not in state else state.x_label
state.y_label = "" if "y_label" not in state else state.y_label

state.title = "" if "title" not in state else state.title
state.label = "" if "label" not in state else state.label

# Deploying graphs
if state.graph_type:
  if state.graph_type.lower() == "line plot":
    state.choice = st.selectbox(label="How will you upload the data?", options=["Csv file","Input the data"], index=None)
    
    if state.choice == "Csv file":
      csv_file(graph_type=state.graph_type.lower())  
            
    elif state.choice == "Input the data":
      input_data(graph_type=state.graph_type.lower())


  if state.graph_type.lower() == "scatter plot":
    csv_file(graph_type=state.graph_type.lower())
  
  if state.graph_type.lower() == "Bar plot".lower():
    state.choice = st.selectbox(label="How will you upload the data?", options=["Csv file","Input the data"], index=None)
  
    if state.choice == "Input the data":
      input_data(graph_type=state.graph_type.lower())
  
    elif state.choice == "Csv file":
      csv_file(graph_type=state.graph_type.lower())  
    
  
                 
