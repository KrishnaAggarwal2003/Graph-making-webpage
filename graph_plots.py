import numpy as np 
import matplotlib.pyplot as plt  

def line_plot_with_csv(data_frame,x_column,y_column,x_label,y_label,title,label=None):
    x_val = data_frame[x_column]
    y_val = data_frame[y_column]
    
    fig,ax = plt.subplots()
    ax.plot(x_val,y_val,label=label) # better to add label here, this way plt function automatically calculates the best layout for label display
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    if label:
        ax.legend(loc="best")
        
    return fig

def bar_plot_with_csv(data_frame,x_column,y_column,x_label,y_label,title,label=None):
    x_val = data_frame[x_column]
    y_val = data_frame[y_column]
    
    fig,ax = plt.subplots()
    ax.bar(x_val,y_val,label=label) # better to add label here, this way plt function automatically calculates the best layout for label display
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    if label:
        ax.legend(loc="best")
        
    return fig

def line_plot_with_input(x_nums,y_nums,x_column,y_column,title,label=None):
    x_val , y_val = x_nums , y_nums
    
    fig,ax = plt.subplots()
    ax.plot(x_val,y_val,label=label)
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title(title)
    if label:
        ax.legend(loc="best")
    
    return fig

def bar_plot_with_input(x_nums,y_nums,x_column,y_column,title,label=None):
    x_val , y_val = x_nums , y_nums
    
    fig,ax = plt.subplots()
    ax.bar(x_val,y_val,label=label)
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title(title)
    if label:
        ax.legend(loc="best")
    
    return fig


def scatter_plot(data_frame,x_column,y_column,x_label,y_label,title,label=None):
    x_val = data_frame[x_column]
    y_val = data_frame[y_column]
    
    fig,ax = plt.subplots()
    ax.scatter(x_val,y_val,label=label)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    if label:
        ax.legend(loc="best")
        
    return fig
    
