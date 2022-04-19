import streamlit as st

def home():

    footerr = """
        <div style="background-color:white;padding:1px">
        <h4 style="color:black;text-align:normal;">This portfolio content diverse 
        project result of my python learning journey. each project is user friendly 
        as a web app grace to streamlit package, aside each application an about 
        page is provided for more details.</h4>
        <h4> Go to the manu in the side bar to navigate </h4>
        </div><br>"""
    st.markdown(footerr, unsafe_allow_html=True)
    st.markdown('<style>h1{color: blue;}</style>', unsafe_allow_html=True)
   
