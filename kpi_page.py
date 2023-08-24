import time
import streamlit as st
import openaiTest
import snowflake_connector
import csv
import pandas as pd
import random


# Function to execute the SQL query and get the result table (replace with your actual implementation)
def execute_query(query):
    result = snowflake_connector.fetch_and_display_data(query)
    return result

df = pd.read_csv("kpi.csv")

def fetch_query(prompt):
    filtered_data = df[df['Prompt'] == prompt]
    return filtered_data['Query'].values[0]

# Page 2: KPI Page
def kpi_page():
    if 'query_outputs' not in st.session_state:
        st.session_state.query_outputs = []
    st.markdown(
        """
        <style>
            section.main.css-uf99v8.ea3mdgi5
                {background-color: #2E2E38;}
            [role="alert"] {
                background-color: #C4C4CD;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Important KPIs")
    st.write("Click on buttons to view respective queries & results for below KPIs\n")

    if 'kpires' not in st.session_state:
        st.session_state.kpires = [""] * 11

    # Buttons layout
    buttons = [
        'Loss Ratio',
        'Expense Ratio',
        'Retention Rate',
        'Average Premium per Policy',
        'Loss Adjustment Expense Ratio',
        'Underwriting Expense Ratio',
        'Average Response Time for Claims Processing',
        'Average Customer Lifetime Value',
        'Average New Business Premiums',
        'Average Policy Duration or Exposure',
        'Premium Growth Rate'
    ]

    rows = [buttons[i:i + 4] for i in range(0, len(buttons), 4)]

    for row in rows:
        cols = st.columns(len(row))
        st.markdown("<div class='row-center'>", unsafe_allow_html=True)
        for col, button_text in zip(cols, row):
            if col.button(button_text):
                button_index = buttons.index(button_text)
                if st.session_state.kpires[button_index] == "":
                    st.session_state.kpires[button_index] = fetch_query(button_text)
                st.session_state.query_outputs.append(button_text + ":\n" + st.session_state.kpires[button_index])
                result = execute_query(st.session_state.kpires[button_index])
                st.session_state.query_outputs.append(result)
        st.markdown("</div>", unsafe_allow_html=True)

    # Display query results
    if st.session_state.query_outputs:
        st.title("Query Results:")
        for i in range(len(st.session_state.query_outputs)):
            if i % 2 == 0:
                items = st.session_state.query_outputs[i].split(':')
                st.write(items[0])
                st.code(items[1])
            else:
                st.dataframe(st.session_state.query_outputs[i])
                df = pd.DataFrame(st.session_state.query_outputs[i])
                csv = df.to_csv()
                items = st.session_state.query_outputs[i - 1].split(':')
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name=f"{items[0]}.csv",
                    key=random.random()
                )
                separator = "---"
                st.text(separator)

        if st.button("Clear"):
            st.session_state.query_outputs=[]
            st.experimental_rerun()
