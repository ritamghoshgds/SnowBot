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
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;600;700&display=swap" rel="stylesheet">
        <style>
        
        div.css-6qob1r.eczjsme3{
            background-color: #747480;
        }
        h1, h3{
            color: #FFE600;
            font-family: 'Roboto', sans-serif;
        }
        div.st-c5.st-cj.st-ck.st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-cl.st-cm{
            color: #F6F6FA
        }
        p{
            color: #F6F6FA;
            font-family: 'Roboto', sans-serif;
        }
        button p{
            color: #2E2E38;
            font-weight: 600;
            font-family: 'Roboto', sans-serif;
        }
        .stButton button { background-color: #C4C4CD}
        [role="radiogroup"] {
            color: #000;
            font-weight: 600;
            font-family: 'Roboto', sans-serif;;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Search", "Popular KPIs"])

    if page == "Search":
        search_app.main()
    elif page == "Popular KPIs":
        kpi_page.kpi_page()

if __name__ == "__main__":
    main()
