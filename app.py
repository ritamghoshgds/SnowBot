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

# Function to simulate user authentication
def authenticate(username, password):
    # Replace with your authentication logic
    if username == "LLMChatbot" and password == "snowflake":
        return True
    return False

# Streamlit App
def main():
    st.markdown("""
        <style>
        .custom-icon {
            font-size: 24px;
            cursor: pointer;
        }
        </style>
        """,unsafe_allow_html=True)
    # Check if the user is authenticated, show login if not
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            st.write("Click again to Hide")
            if authenticate(username, password):
                st.session_state.authenticated = True
            else:
                st.error("Authentication failed!")

    # Main content
    if st.session_state.authenticated:
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
        logout_button = st.sidebar.button("Logout")
        if logout_button:
            st.sidebar.write('Are you sure you want to logout?')
            st.session_state.authenticated = False

if __name__ == "__main__":
    main()
