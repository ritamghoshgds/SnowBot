import time
import streamlit as st
import snowflake_connector
import search_app, kpi_page

# Function to process the prompt and return the query
def process_prompt(prompt):
    code = openaiTest.Main2(prompt)
    return code

# Function to execute the SQL query and get the result table (replace with your actual implementation)
def execute_query(query):
    result = snowflake_connector.fetch_and_display_data(query)
    return result

# Streamlit App
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Search", "Popular KPIs"])

    if page == "Search":
        search_app.main()
    elif page == "Popular KPIs":
        kpi_page.kpi_page()

if __name__ == "__main__":
    main()
