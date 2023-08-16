import streamlit as st
import pandas as pd
import numpy as np
import pickle

@st.cache_data
def get_fvalue(val):    
    feature_dict = {"No":1,"Yes":2}    
    for key,value in feature_dict.items():        
        if val == key:            
            return value
        
def get_value(val,my_dict):    
    for key,value in my_dict.items():        
        if val == key:            
            return value