import time
import streamlit as st
import openaiTest
import snowflake_connector
import pandas as pd
import random

# Function to process the prompt and return the query
def process_prompt(prompt):
    code = openaiTest.Main2(prompt)
    return code

# Function to execute the SQL query and get the result table (replace with your actual implementation)
def execute_query(query):
    try:
        result = snowflake_connector.fetch_and_display_data(query)
    except:
        result = pd.DataFrame({0:["Error"]})
    return result
    
# Main Streamlit app
def main():
    st.markdown(
        """
        <style>
            section.main.css-uf99v8.ea3mdgi5
                {background-color: #2E2E38;}
            [data-testid="stText"] {
                color: #C4C4CD;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title('Snowbot')
    st.markdown("### How to Use the Search Bot")
    # ... (your existing instructions)

    # ... (your existing step handling code)

    if st.session_state.step == 3:
        st.session_state.done2 = False
        st.subheader("Result Table:")
        
        if st.session_state.result is None:
            st.warning("No query has been executed yet.")
        else:
            df = pd.DataFrame(st.session_state.result)
            if df.empty:
                st.error("Query result is empty. Please check your query or try again.")
            else:
                st.dataframe(df, width=1500)
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
            st.session_state.step = 1

if __name__ == "__main__":
    main()
