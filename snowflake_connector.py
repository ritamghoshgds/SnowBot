import snowflake.connector
import pandas as pd

# Function to fetch data from Snowflake and display it in a good-looking format
def fetch_and_display_data(query):
    global df
    snowflake_user = "MitadruChakraborty"#"MITADRU2000"
    snowflake_password = "Abcd1234@"
    snowflake_account = "eygds-lnd_dna_az_1"#"ynxsocx-fz48656"
    snowflake_warehouse = "LLM_WH"#"COMPUTE_WH"
    snowflake_database = "LLM_CHATBOT"#"SFPOC"
    snowflake_schema = "DATA"
    # Create a Snowflake connection
    conn = snowflake.connector.connect(
        user=snowflake_user,
        password=snowflake_password,
        account=snowflake_account,
        warehouse=snowflake_warehouse,
        database=snowflake_database,
        schema=snowflake_schema,
        role="LLM_RL"
    )

    # Create a Snowflake cursor
    cursor = conn.cursor()

    try:
        if(query.strip()==''):
            return "Query didn't generated correctly!"
        # Execute the SELECT query
        cursor.execute(query)

        # Fetch all the data and store it in a pandas DataFrame
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(data, columns=columns)

        # Display the table in a good-looking format

    # except snowflake.connector.errors.ProgrammingError as e:
    #     return f"Error executing query: {e}"
    except:
        return "Query didn't generated correctly!"

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()
        return df

# Call the function with the SELECT query
#print(fetch_and_display_data("SELECT * FROM POC.USER_DETAILS"))
