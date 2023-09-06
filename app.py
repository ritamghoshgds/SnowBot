import time
import streamlit as st
import snowflake_connector
import search_app,kpi_page
username=""
password=""
# Function to process the prompt and return the query
# def process_prompt(prompt):
#     code = openaiTest.Main2(prompt)
#     return code

# Function to execute the SQL query and get the result table (replace with your actual implementation)
# def execute_query(query):
#     result = snowflake_connector.fetch_and_display_data(query)
#     return result

# Function to simulate user authentication
def authenticate(username, password):
    # Replace with your authentication logic
    # if username == "LLMChatbot" and password == "snowflake":
    #     return True
    # return False
    # My aim here is to write code that takes the username and password and runs the query in the execte query function using these credentials and check if these credentials have snowflake access or not ,
    #if that account does not have access then we return authenticate variable as false and if it can return query result then we return it as true
    var=snowflake_connector.fetch_and_display_data("Select GET_DDL('SCHEMA','DATA') AS schema_details;",username,password)
    if var.iloc[0,0]=="Incorrect username or password was specified.":
        return False
    else:
        return True

# Streamlit App
def main():
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;600;700&display=swap" rel="stylesheet">
        <style>
        .custom-icon {
            font-size: 24px;
            cursor: pointer;
        }
        section{
            background-color: #2E2E38;
        }
        #login-to-snowbot{
            color: #FFE600;
        }
        p { color: #F6F6FA; }
        button p { color: #000; }
        </style>     
        """, unsafe_allow_html=True)
    
    # Check if the user is authenticated, show login if not
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.title("Login to Snowbot")
        global username
        username= st.text_input("Username")
        st.session_state.user=username
        global password
        password=st.text_input("Password", type="password")
        st.session_state.passw=password
        if st.button("Login"):
            st.write("Click again to Proceed")
            if authenticate(username, password):
                st.session_state.authenticated = True
            else:
                st.error("Authentication failed!")

    # Main content
    elif st.session_state.authenticated:
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
            search_app.main(st.session_state.user,st.session_state.passw)
        elif page == "Popular KPIs":
            kpi_page.kpi_page(st.session_state.user,st.session_state.passw)
        logout_button = st.sidebar.button("Logout")
        if logout_button:
            st.sidebar.write('Press again to logout')
            st.session_state.authenticated = False

if __name__ == "__main__":
    main()
