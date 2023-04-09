import streamlit as st
from projects.header_footer import *
from projects.home import *
from projects.tip_calculator import *


# Sidebar Configuration
st.markdown(
    """
<style>
.sidebar .sidebar-content {
    background-image: linear-gradient(#99ffcc,#99ffcc);
    color: purple;
}
</style>
""",
    unsafe_allow_html=True,
)

def main():
    logo()
    # basic layout
    menu = ["Home", "Tip Calculator", "BMI", "Life Calendar",
            "Odd or Even Year", "Love Calculator", "Leap Year", "Treasure Island", 
            "Banker Roulette", "Rock-Paper-Scisors", "Password Generator", 
            "Hangman", "Unix epoch timestamp convertor"]
    choice = st.sidebar.radio("Menu", menu)
    # siderbar method
    #st.write(dir(st.sidebar))
    header()
    if choice == "Home":
        home()
    elif choice == "Tip Calculator":
        tip_calculator()
    elif choice == "Life Calendar":
        pass #life_calendar()
    elif choice == "BMI":
        pass #bmi()
    elif choice == "Odd or Even Year":
        pass #odd_or_even()
    elif choice == "Love Calculator":
        pass #love_calculator()
     elif choice == "Unix epoch timestamp convertor":
        pass #timestamp()


    footer()

if __name__ == '__main__':
    main()
