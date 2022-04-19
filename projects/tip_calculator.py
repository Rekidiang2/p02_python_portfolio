import streamlit as st
from PIL import Image

#st.image(image, use_column_width=True)

def tip_calculator_about():
    if st.checkbox("About Shared Bill Tip Calculator"):
        st.markdown("""
            ## 1) Tip around the world
            ###### A tip or gratuity is an extra sum of money paid to certain service workers for\
            a provided service. Tip amounts, as well as acceptance, vary in different parts of\
            the world. In some countries in East Asia such as Japan, tips are seen as insulting\
            and can sometimes be interpreted as a bribe. In yet other countries such as the United\
            States, tipping is widely expected, and in many cases, is even factored into a service\
            worker's compensation towards satisfying the minimum wage requirement. This is important\
            to note, since although tipping is entirely voluntary, many servers depend on tips to make\
            a living in countries like the United States. As such, as a tourist, it can be helpful to\
            research the tipping customs in the countries being visited. In the U.S. or any other country\
            where tipping is expected, depending on the restaurant or the number of patrons at a table,\
            gratuity may be automatically applied to the bill amount. As previously mentioned, tipping can\
            be offensive in some countries, so although a citizen of the United States that is visiting\
            another country may want to express their appreciation of the service provided, the gesture may\
            in some cases result in the opposite effect.

            ## 2) Tip map

            ### 2.1) Tip expectation
            ###### map below  provides some information regarding whether or not a \
            tip is expected, or how a tip may be received in certain regions, as well
            """)
            
        tip_map = Image.open('images/tip_map.JPG')
        st.image(tip_map, use_column_width=True)

        st.markdown("""
            ### 2.2) Tip amount
            ###### table of typical tip amounts in the United States and Canada for different services.
            """)
        tip_table = Image.open('images/tip_table.JPG')
        st.image(tip_table, use_column_width=True)
        st.markdown("""
            ## 3) Logical digram
            """)
def tip_calculator():
    st.header("Shared Bill Tip Calculator")
    tot_bill = st.number_input("What was the total bill ? ")
    split_num = 1
    split_num = st.number_input("How many people to split the bill ?", 1)
    tip_perc = st.slider(
        "What percentage tip would you like to give ?", 5, 15, 10)
    if st.button("Calculate"):
        result = (tot_bill+(tot_bill*(tip_perc/100)))/split_num

        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("Total Bill $", tot_bill)
        with col2:
            st.write("Tip %", tip_perc, "%")
        with col3:
            st.write("Number of People", split_num)
        st.success(f"Each person should pay :  ${round(result, 1)}")
    tip_calculator_about()
