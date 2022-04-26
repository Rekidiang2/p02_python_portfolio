import streamlit as st
import numpy as np
from PIL import Image
import pandas as pd
#import cv2 as cv
import pickle
import sqlite3
#import matplotlib as plt

def logo():
    # source: jason-leung from unsplash
    logo = "images/ktech_logo.png"
    logo = Image.open(logo)
    size=(100,100)
    #resize image
    logo = logo.resize(size)
    st.sidebar.image(logo)

def header():
    tip_map = Image.open('images/pyportfolio_banier.png')
    st.image(tip_map, use_column_width=True)
    st.markdown("""---""")
    



def footer():
    st.markdown("""---""")
   
    footer = """
            <div style="background-color:black;padding:1px">
            <h5 style="color:white;text-align:center;">My name is Kiese Diangebeni Reagan</h5>
            <p style="color:white;text-align:center;font-size:14px;">I'm Data Science Analyst, technology passionate person, Artificial Intelligence enthusiast and lifelong learner. </p>
            
            <p style="color:red;text-align:center;">
            <a href="https://kiese.tech">www.kiese.tech</a> -
            <a href="https://twitter.com/ReaganKiese">Twitter</a> - 
            <a href="https://www.linkedin.com/in/kiese-diangebeni-reagan-82992216a/">Linkedin</a> - 
            <a href="https://github.com/RekidiangData-S">Github</a> - 
            <a href="https://medium.com/@rkddatas">Medium</a> - 
            <a href="https://www.kaggle.com/rekidiang">Kaggle</a></p>
            </div><br>"""
    st.markdown(footer, unsafe_allow_html=True)
    st.markdown('<style>h1{color: blue;}</style>', unsafe_allow_html=True)