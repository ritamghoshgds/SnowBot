import snowflake.connector
import pandas as pd


def fetch_and_display_data(query,snowflake_user,snowflake_password,snowflake_role):
    # snowflake_user = "MitadruChakraborty"
    # snowflake_password = "Abcd1234@"
    # snowflake_role = "LLM_RL"
    snowflake_account = "eygds-lnd_dna_az_1"
    snowflake_warehouse = "LLM_WH"
    snowflake_database = "LLM_CHATBOT"
    snowflake_schema = "DATA"

    try:
        conn = snowflake.connector.connect(
            user=snowflake_user,
            password=snowflake_password,
            account=snowflake_account,
            warehouse=snowflake_warehouse,
            database=snowflake_database,
            schema=snowflake_schema,
            role=snowflake_role
        )
        cursor = conn.cursor()
        print(snowflake_role)
        print("Problem here")
    except snowflake.connector.errors.DatabaseError as e:
        return (pd.DataFrame({0:[str(f"Incorrect username,password or role was specified.")]}))

    try:
        if query.strip() == '':
            raise ValueError("Query is empty")
        
        cursor.execute(query)
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(data, columns=columns)
        return df

    
    except snowflake.connector.errors.ProgrammingError as e:
        return (pd.DataFrame({0:[str(f"Query didn't produce any data or it has a syntax issue {e}")]}))
    
    except Exception as e:
        return (pd.DataFrame({0:[str(f"Query didn't produce any data or it has a syntax issue {e}")]}))
    
    finally:
        cursor.close()
        conn.close()

# print(fetch_and_display_data("Select GET_DDL('SCHEMA','DATA') AS schema_details;","MitadruChakraborty","Abcd1234@","LLM_RL").iloc[0,0])
