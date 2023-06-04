import streamlit as st 
import pandas as pd 

# # "with" notation
# with st.sidebar:
#     st.title("mha")

   

# # Store the initial value of widgets in session state
# if "visibility" not in st.session_state:
#     st.session_state.visibility = "visible"
#     st.session_state.disabled = False

# col1, col2 = st.columns(2)

# with col1:
#     st.checkbox("Disable text input widget", key="disabled")
#     st.radio(
#         "Set text input label visibility 👉",
#         key="visibility",
#         options=["visible", "hidden", "collapsed"],
#     )
#     st.text_input(
#         "Placeholder for the other text input widget",
#         "This is a placeholder",
#         key="placeholder",
#     )

# with col2:
#     text_input = st.text_input(
#         "Enter some text 👇",
#         label_visibility=st.session_state.visibility,
#         disabled=st.session_state.disabled,
#         placeholder=st.session_state.placeholder,
#     )

#     if text_input:
#         st.write("You entered: ", text_input)



# Store the initial value of widgets in session state
# if "visibility" not in st.session_state:
#     st.session_state.visibility = "visible"
#     st.session_state.disabled = False
#     st.session_state.horizontal = False

# col1, col2 = st.columns(2)

# with col1:
#     st.checkbox("Disable radio widget", key="disabled")
#     st.checkbox("Orient radio options horizontally", key="horizontal")

# with col2:
#     st.radio(
#         "hi",
#         ["visible", "hidd", "collap"],
#         key="visibility",
#         label_visibility=st.session_state.visibility,
#         disabled=st.session_state.disabled,
#         horizontal=st.session_state.horizontal,
#     ) 

# with st.sidebar:
#     st.title("mha mha mha")
#     digits1 = st.text_input("minhteaung")
#     digits2 = st.text_input("Questions 11-20", value="0,0,0,0,0,0,0,0,0,0")
#     digits3 = st.text_input("Questions 21-30", value="0,0,0,0,0,0,0,0,0,0")
#     digits4 = st.text_input("Questions 31-40", value="0,0,0,0,0,0,0,0,0,0")
#     digits5 = st.text_input("Questions 41-50", value="0,0,0,0,0,0,0,0,0,0")
#     digits6 = st.text_input("Questions 51-60", value="0,0,0,0,0,0,0,0,0,0")

# import yfinance as yf
# import streamlit as st

# st.write("""
# # Simple Stock Price App

# Shown are the stock closing price and volume of Google!

# """)

# # https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# #define the ticker symbol
# tickerSymbol = 'GOOGL'
# #get data on this ticker
# tickerData = yf.Ticker(tickerSymbol)
# #get the historical prices for this ticker
# tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# # Open	High	Low	Close	Volume	Dividends	Stock Splits

# st.line_chart(tickerDf.Close)
# st.line_chart(tickerDf.Volume)

st.set_page_config(
    page_title="Multipage App",
    page_icon= "🧐"
)

st.title("Main Page")
st.sidebar.success("select a page above.")


if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")

if submit:
     st.session_state["my_input"] = my_input
     st.write("You have entered", my_input)

     