import openai
import snowflake_connector as sc

# with open("API_OPENAI.txt",'r') as key:
#     apiKey = key.read()
sch = sc.fetch_and_display_data("Select GET_DDL('SCHEMA','POC') AS schema_details;")
tableStructText = sch['SCHEMA_DETAILS'][0] #sch.replace('\\n','\n').replace('\\t','  ')
tableStructText = tableStructText + "\n above is the DDL of Snowflake insurance data model. \n Using Given tables, Only Generate Snowflake SQL query to extract multi-column table related to this prompt: {}"
openai.api_key = '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'

def find_SQL_substring(main_string):
    #start_index = main_string.find('```sql') + 7
    start_index = main_string.find('SELECT')
    #end_index = main_string.find('```', start_index)
    end_index = main_string.find(';', start_index) +1

    if start_index != -1 and end_index != -1:
        substring = main_string[start_index:end_index]
        return substring
    else:
        return None

def generate_code(user_input):
    # Provide the user input as a system message
    system_message = f"User: {user_input}\nAssistant:"

    # Define the instruction for the model
    instruction = "Please generate the SQL code snippet required for the given task. The whole code snippet must be enclosed within 2 '```' symbol. Remember all the tables and their column names. Include a few additional coulmns related to given attributes."

    # Generate the code by sending the conversation and instruction to the model
    response = openai.ChatCompletion.create(
        verify=False,
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": instruction},
        ]
    )
    # Get the assistant's reply (code snippet)
    assistant_reply = response.choices[0].message.content

    return find_SQL_substring(assistant_reply)

# Generate code snippet based on user input
#user_input = "In europe continent how many users are there?"


def Main2(input):
    code_snippet = generate_code(tableStructText.format(input))
    return code_snippet
