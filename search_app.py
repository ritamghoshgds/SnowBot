import time
import streamlit as st
import openaiTest
import snowflake_connector

# Function to process the prompt and return the query
def process_prompt(prompt):
    code = openaiTest.Main2(prompt)
    return code

# Function to execute the SQL query and get the result table (replace with your actual implementation)
def execute_query(query):
    result = snowflake_connector.fetch_and_display_data(query)
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
    st.title('SQL ChatBot: Insurance')
    st.markdown("### How to Use the Search Bot")
    st.text("1. Enter your query prompt in the text input box provided.")
    st.text("2. Click the 'Send' button to generate the SQL query based on your prompt.")
    st.text("3. The generated SQL query will be displayed. Review it to ensure it matches your intent.")
    st.text("4. If you approve the query, click the 'Execute' button to execute it.")
    st.text("5. The result table will be displayed below. You can review the query results.")
    st.text("6. If you want to refresh the prompt and start over, click the 'Reload' button.")
    
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
            st.session_state.step = 3
            st.session_state.done = False
            if 'done2' not in st.session_state or st.session_state.done2 == False:
                loading_placeholder = st.empty()
                loading_placeholder.text("Loading...")
                st.session_state.result = execute_query(st.session_state.query)
                loading_placeholder.empty()
                st.success("Task Completed!")
                st.session_state.done2 = True
                
        elif st.button("No"):
            st.write("Sure you don't? (Press No Again)")
            st.session_state.step = 1
            st.session_state.result = None
            st.session_state.query = None

    if st.session_state.step == 3:
        st.session_state.done2 = False
        st.subheader("Result Table:")
        st.dataframe(st.session_state.result, width=1500)
        st.write("Press reload: to REFRESH prompt results or GENERATE NEW one!")
        if st.button('Reload'):
            st.session_state.result = None
            st.session_state.query = None
            st.write("Are you sure? (PRESS Reload Again)")
            st.session_state.step = 1

if __name__ == "__main__":
    main()
