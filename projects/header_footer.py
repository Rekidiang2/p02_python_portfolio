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
    html_temp = """
    <div style="background-color:black;padding:0px">
    <h2 style="color:white;text-align:center;">Python Portfolio </h2>   
    <h4 style="color:red;text-align:center;">My python learning journey in projects </h4>
    </div><br>"""
    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown('<style>h1{color: blue;}</style>', unsafe_allow_html=True)



def footer():
   
    footerr = """
            <div style="background-color:white;padding:1px">
            <h6 style="color:black;text-align:center;">======================== Author ========================</h6>
            <h6 style="color:black;text-align:center;">My name is Kiese Diangebeni Reagan, I'm Data Science Analyst, technology passionate person, Artificial Intelligence enthusiast and lifelong learner. </h6>
            <h6 style="color:red;text-align:center;"> For more information about me go to my Website and Social Network platform (👇)</h6>
            <h6 style="color:blue;text-align:center;"><a href:"https://kiese.tech>www.kiese.tech</a></h6>
            
            <p style="color:red;text-align:center;">
            <a href="https://twitter.com/ReaganKiese">Twitter</a> - 
            <a href="">Linkedin</a> - 
            <a href="https://github.com/RekidiangData-S">Github</a> - 
            <a href="https://medium.com/@rkddatas">Medium</a> - 
            <a href="https://www.kaggle.com/rekidiang">Kaggle</a></p>
            </div><br>"""
    st.markdown(footerr, unsafe_allow_html=True)
    st.markdown('<style>h1{color: blue;}</style>', unsafe_allow_html=True)