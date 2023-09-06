import time
import streamlit as st
import openaiTest
import snowflake_connector
import pandas as pd
import random

username=""
password=""
# Function to process the prompt and return the query
def process_prompt(prompt):
    code = openaiTest.Main2(prompt)
    return code

# Function to execute the SQL query and get the result table (replace with your actual implementation)
def execute_query(query,username,password):
    try:
        result = snowflake_connector.fetch_and_display_data(query,username,password)
        return result
    except Exception as e:
        return pd.DataFrame()
    
# Main Streamlit app
def main(user,passw):
    global username
    username = user
    global password
    password = passw
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;600;700&display=swap" rel="stylesheet">
        <style>
            section.main.css-uf99v8.ea3mdgi5
                {background-color: #2E2E38;}
            [data-testid="stText"] {
                color: #C4C4CD;
                margin-bottom: -10px;
                font-size: 2.1vh;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title('Snowbot')
    st.markdown("### How to Use the Search Bot")
    st.text("1. Enter your prompt in the input box and click 'Send'")
    st.text("2. The generated SQL query will be displayed below.")
    st.text("3. If you approve the query, click the 'Execute' button to execute it.")
    st.text("4. The result table will be displayed below.")
    st.text("5. Click the 'Reload' button to start over.")
    st.text("")
    
    # Input text area for entering the prompt
    if 'step' not in st.session_state:
        st.session_state.step = 1

    if st.session_state.step == 1:
        # Input text area for entering the prompt
        last_prompt = st.session_state.get('prompt', "")
        prompt = st.text_input("Enter your prompt here", value=last_prompt)
            
        # Button to send the prompt
        if st.button('Send'):
            st.session_state.step = 2
            st.session_state.prompt = prompt

    if st.session_state.step == 2:
        if 'done' not in st.session_state or st.session_state.done == False:
            loading_placeholder = st.empty()
            loading_placeholder.text("Loading...")
            st.session_state.query = process_prompt(st.session_state.prompt)
            loading_placeholder.empty()
            st.success("Task Completed!")
            st.session_state.done = True

        st.subheader("Generated SQL Query:")
        st.code(st.session_state.query)
        st.write("Press Execute if you APPROVE this query!")

        if st.button('Execute'):
            st.session_state.done = False
            if 'done2' not in st.session_state or st.session_state.done2 == False:
                loading_placeholder = st.empty()
                loading_placeholder.text("Loading...")
                st.session_state.result = execute_query(st.session_state.query,username,password)
                st.session_state.counter = False
                #if df.empty:
                #st.session_state.counter = True
                loading_placeholder.empty()
                st.success("Task Completed!")
                st.session_state.done2 = True
                st.session_state.step = 3

        elif st.button("No"):
            st.write("Sure you don't? (Press No Again)")
            st.session_state.step = 1
            st.session_state.result = None
            st.session_state.query = None

    if st.session_state.step == 3:
        st.session_state.done2 = False
        st.subheader("Result Table:")
        #if st.session_state.counter:
            #st.write("Please try again")
        #else:
        st.dataframe(st.session_state.result, width=1500)
        try:
            df = pd.DataFrame(st.session_state.result)
        except:
            df = pd.DataFrame()
        csv = df.to_csv()
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="search_output.csv",
            key=random.random()
        )
        st.write("Press reload: to REFRESH prompt results or GENERATE NEW one!")
        if st.button('Reload'):
            st.session_state.result = None
            st.session_state.query = None
            st.write("Are you sure? (PRESS Reload Again)")
            st.session_state.step = 1

if __name__ == "__main__":
    main(username,password)
