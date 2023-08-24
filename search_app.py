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
    
    # Display a brief summary message with typing effect
    summary_message = "Welcome to the SnowSQL ChatBot!\nThis chatbot can assist you with generating and executing SQL queries"
    typing_placeholder = st.empty()
    
    lines = summary_message.split('\n')
    for line_index, line in enumerate(lines):
        words = line.split()
        for word in words:
            typing_placeholder.text(" ".join(words[:words.index(word) + 1]))
            time.sleep(0.2)  # Adjust the sleep duration for typing speed
            if words.index(word) < len(words) - 1:
                typing_placeholder.text(" ")
                time.sleep(0.1)  # Add a shorter pause between words
        if line_index < len(lines) - 1:
            typing_placeholder.text("\n")
            time.sleep(0.1)  # Add a shorter pause between lines

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
        st.session_state.result = None
        st.session_state.query = None
        if st.button('Reload'):
            st.write("Are you sure? (PRESS Reload Again)")
            st.session_state.step = 1
            st.session_state.result = None
            st.session_state.query = None

if __name__ == "__main__":
    main()
