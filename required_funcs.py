import streamlit as st
import pandas as pd
from graph_plots import line_plot_with_csv, line_plot_with_input, scatter_plot, bar_plot_with_csv,bar_plot_with_input
import numpy as np
import re

state = st.session_state

def data_file(graph_type):
    state.csv_content = st.file_uploader(label="Upload the data file",type=["csv","xlsx"],accept_multiple_files=False,help="Upload either csv file or xlsx(excel) file")
        
    if state.csv_content:
        try:
            extension = re.findall(pattern=r".xlsx|.csv",string=str(state.csv_content))[0] # To extract the format extension
            if extension == ".xlsx":
                state.file_data = pd.read_excel(state.csv_content)
            elif extension == ".csv":
                state.file_data = pd.read_csv(state.csv_content)
            
            col1,col2,col3,col4 = st.columns(4) # Has to keep it here.,
                    
            with col1:
              state.x_label = st.text_input(label="Name for X-axis:", help="For data file, add the column name you want for the x-axis")
            with col2:
              state.y_label = st.text_input(label="Name for Y-axis:",help="For data file, add the column name you want for the y-axis")
            with col3:
              state.title = st.text_input(label="Title for the plot:")
            with col4:
              state.label = st.text_input(label="Label name if required:")
                            
            st.write("")  # Blank line for spacing between the two column pairs
            spacer_col1, spacer, spacer_col2 = st.columns([3, 2, 3]) # Introducing new columns space below the 4 columns
            
            with spacer:
              graph_make = st.button(label="Start the Graph-plot") 
            
            for x_col in state.file_data.columns:
              if state.x_label.replace(" ","").lower() in x_col.replace(" ","").lower():
                state.x_column = x_col
      
            for y_col in state.file_data.columns:
              if state.y_label.replace(" ","").lower() in y_col.replace(" ","").lower():
                state.y_column = y_col  
          
            if graph_make:
                if graph_type == "line plot":
                  figure = line_plot_with_csv(data_frame=state.file_data,x_column=state.x_column,y_column=state.y_column,x_label=state.x_label,y_label=state.y_label,title=state.title,label=state.label) # variables at their correct position
                
                elif  graph_type == "scatter plot":
                    figure = scatter_plot(data_frame=state.file_data,x_column=state.x_column,y_column=state.y_column,x_label=state.x_label,y_label=state.y_label,title=state.title,label=state.label)
                
                else:
                    figure = bar_plot_with_csv(data_frame=state.file_data,x_column=state.x_column,y_column=state.y_column,x_label=state.x_label,y_label=state.y_label,title=state.title,label=state.label)                                        
                
                st.pyplot(fig=figure)
                st.balloons()
                space1,space2,space3 = st.columns([2,3,2.5])
                with space2:
                 st.success(body="Plotting of the graph successful",icon="🥳")  
          
        except Exception as e:
            st.error(f"Encountered error: {e}") 
            
            
def input_data(graph_type):
      state.x_num = None if "x_num" not in state else state.x_num
      state.y_num = None if "y_num" not in state else state.y_num
      
      state.x_input = "" if "x_input" not in state else state.x_input
      state.y_input = "" if "y_input" not in state else state.y_input
      
       
      state.x_input = st.text_input(label="Enter the x-values",help="Make sure to have commas between the entries")
      state.y_input = st.text_input(label="Enter the y-values",help="Make sure to have commas between the entries")
      
      if state.x_input and state.y_input:
        try:
          if graph_type == "line plot":
              x_numbers = [float(num.strip()) for num in state.x_input.split(",")]
          elif graph_type == "bar plot":
              x_numbers = [str(num.strip()) for num in state.x_input.split(",")]
              
          y_numbers = [float(num.strip()) for num in state.y_input.split(",")]
          
          if len(x_numbers) != len(y_numbers):
            raise ValueError("The x and y need to be of same length")
          
          state.x_num, state.y_num = np.array(x_numbers), np.array(y_numbers)
          col1,col2,col3,col4 = st.columns(4) # Has to keep it here.,
                    
          with col1:
            state.x_column = st.text_input(label="Name for X-axis:", help="For csv file, add the column name you want for the x-axis")
          with col2:
            state.y_column = st.text_input(label="Name for Y-axis:",help="For csv file, add the column name you want for the y-axis")
          with col3:
            state.title = st.text_input(label="Title for the plot:")
          with col4:
            state.label = st.text_input(label="Label name if required:")  
          
          st.write("")  # Blank line for spacing between the two column pairs
          spacer_col1, spacer, spacer_col2 = st.columns([3, 2, 3]) # Introducing new columns space below the 4 columns
            
          with spacer:
            graph_make = st.button(label="Start the Graph-plot") 
          
          if graph_make:
            if graph_type == "line plot":
             figure = line_plot_with_input(x_nums=state.x_num , y_nums=state.y_num, x_column=state.x_column,y_column=state.y_column,title=state.title, label=state.label)
            else:
                figure = bar_plot_with_input(x_nums=state.x_num , y_nums=state.y_num, x_column=state.x_column,y_column=state.y_column,title=state.title, label=state.label)
                                          
            st.pyplot(fig=figure)
            st.balloons()
            space1,space2,space3 = st.columns([2,3,2.5])
            with space2:
              st.success(body="Plotting of the graph successful",icon="🥳")        
        
        except Exception as e:
          st.error(f"Encountered error: {e}")


#             
