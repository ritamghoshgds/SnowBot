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


# Page 2: KPI Page
def kpi_page():
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
        st.session_state.kpires = ["","","","","","","","","","",""]

    if st.button("Claims Settlement Ratio"):
        if st.session_state.kpires[0] == "":
            st.session_state.kpires[0] = openaiTest.Main2(
                "Find Claims Settlement Ratio: Calculation: (Number of Claims Settled / Number of Claims Filed) * 100 Supported by: Claims, ClaimsHistory tables. Output should be a single query with a single aggregated output")
        #print(st.session_state.kpires[0])
        st.code(st.session_state.kpires[0])
        st.dataframe(execute_query(st.session_state.kpires[0]))

    if st.button("Underwriting Expense Ratio"):
        if st.session_state.kpires[1] == "":
            st.session_state.kpires[1] = openaiTest.Main2(
                "Find Underwriting Expense Ratio: Calculation: (Total Underwriting Expenses / Total Earned Premium) * 100 Supported by: Underwriting, PremiumPayments tables.  Output should be a single query with a single aggregated output")
        st.code(st.session_state.kpires[1])
        st.dataframe(execute_query(st.session_state.kpires[1]))

    if st.button("Average Underwriting Risk Score"):
        if st.session_state.kpires[2] == "":
            st.session_state.kpires[2] = openaiTest.Main2(
                "Find Average Underwriting Risk Score: Calculation: Total Risk Score / Number of Underwriting Cases Supported by: Underwriting table.  Output should be a single query with a single aggregated output")
        st.code(st.session_state.kpires[2])
        st.dataframe(execute_query(st.session_state.kpires[2]))

    if st.button("Average Age of Policies"):
        if st.session_state.kpires[3] == "":
            st.session_state.kpires[3] = openaiTest.Main2(
                "Find Average Age of Policies: Calculation: Average of (Current Date - Policy Start Date) for all policies Supported by: Policy table.  Output should be a single query with a single aggregated output")
        st.code(st.session_state.kpires[3])
        st.dataframe(execute_query(st.session_state.kpires[3]))

    if st.button("Average Age of Claims"):
        if st.session_state.kpires[4] == "":
            st.session_state.kpires[4] = openaiTest.Main2(
                "Find Average Age of Claims: Calculation: Average of (Current Date - Claim Date) for all claims Supported by: Claims table.  Output should be a single query with a single aggregated output")
        st.code(st.session_state.kpires[4])
        st.dataframe(execute_query(st.session_state.kpires[4]))

    if st.button("Claim Loss Ratio"):
        if st.session_state.kpires[5] == "":
            st.session_state.kpires[5] = openaiTest.Main2(
                "Find Claim Loss Ratio: Calculation: (Total Claims Amount / Total Premium Collected) * 100 Supported by: Claims, PremiumPayments tables.  Output should be a single query with a single aggregated output")
        st.code(st.session_state.kpires[5])
        st.dataframe(execute_query(st.session_state.kpires[5]))

    if st.button("Average Response Time for Claims Processing"):
        if st.session_state.kpires[6] == "":
            st.session_state.kpires[6] = openaiTest.Main2(
                "Find Average Response Time for Claims Processing: Calculation: Average of (Claim Processed Date - Claim Date) for all claims Supported by: Claims table.  Output should be a single query with a single aggregated output")
        st.code(st.session_state.kpires[6])
        st.dataframe(execute_query(st.session_state.kpires[6]))

    if st.button("Claims Closed Ratio"):
        if st.session_state.kpires[7] == "":
            st.session_state.kpires[7] = openaiTest.Main2(
                "Find Claims Closed Ratio: Calculation: (Number of Claims Closed / Total Number of Claims) * 100 Supported by: Claims table.  Output should be a single query with a single aggregated output")
        st.code(st.session_state.kpires[7])
        st.dataframe(execute_query(st.session_state.kpires[7]))

    if st.button("New Business Premiums"):
        if st.session_state.kpires[8] == "":
            st.session_state.kpires[8] = openaiTest.Main2(
                "Find New Business Premiums: Calculation: Sum of Premiums for New Policies Supported by: PremiumPayments table.  Output should be a single query with a single aggregated output")
        st.code(st.session_state.kpires[8])
        st.dataframe(execute_query(st.session_state.kpires[8]))

    if st.button("Average Policy Duration"):
        if st.session_state.kpires[9] == "":
            st.session_state.kpires[9] = openaiTest.Main2(
                "Find Average Policy Duration: Calculation: Average of (Policy End Date - Policy Start Date) for all policies Supported by: Policy table. Output should be a single query with a single aggregated output")
        st.code(st.session_state.kpires[9])
        st.dataframe(execute_query(st.session_state.kpires[9]))

    if st.button("Average Customer Lifetime Value (CLV)"):
        if st.session_state.kpires[10] == "":
            st.session_state.kpires[10] = openaiTest.Main2(
                "Find Average Customer Lifetime Value (CLV): Calculation: Sum of Premiums from Renewals / Number of Policies Renewed Supported by: Renewals table. Output should be a single query with a single aggregated output")
        st.code(st.session_state.kpires[10])
        st.dataframe(execute_query(st.session_state.kpires[10]))

