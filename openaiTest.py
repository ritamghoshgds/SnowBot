import openai
import snowflake_connector as sc
# with open("API_OPENAI.txt",'r') as key:
#     apiKey = key.read()

# print("-------------------")
# print(tableStructText)
# print("-----------------------")
#openai.api_key = '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'

def find_SQL_substring(main_string):
    start_index = main_string.find('```') + 7
    #start_index = main_string.find('SELECT')
    end_index = main_string.find('```', start_index)
    #end_index = main_string.find(';', start_index) +1

    if start_index != -1 and end_index != -1:
        substring = main_string[start_index:end_index]
        return substring
    else:
        return None

def generate_code(user_input):
    # Provide the user input as a system message
    system_message = f"User: {user_input}\nAssistant:"

    # Define the instruction for the model
    instruction = """1. Please generate the SQL code snippet required for the given task using only the columns that exist in the tables.. 
    2. The whole code snippet must be enclosed within 2 '```' symbol. 
    3. Column and table names should be accurate and must be from the "DATA" schema. 
    4. Do not make your own columns, only use the ones that are in the table
    5. Query must be accurate, executable and not too long.
    6. Use minimum SQL Joins and group by.
    7. Use Chat GPT 4.0."""

    # Generate the code by sending the conversation and instruction to the model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": instruction},
        ], temperature = 0.2
    )
    # Get the assistant's reply (code snippet)
    assistant_reply = response.choices[0].message.content

    return find_SQL_substring(assistant_reply)

# Generate code snippet based on user input
#user_input = "In europe continent how many users are there?"

def Main2(input,user,passw,rl):
    sch = sc.fetch_and_display_data("Select GET_DDL('SCHEMA','DATA') AS schema_details;",user,passw,rl)
    tableStructText = sch['SCHEMA_DETAILS'][0].replace('{}','[]')
    tableStructText = tableStructText + "\n above is the DDL of Snowflake insurance data model. \n Using Given tables only, Generate Snowflake SQL query to extract multi-column table related to this prompt: {}"
    code_snippet = generate_code(tableStructText.format(input))
    return code_snippet
