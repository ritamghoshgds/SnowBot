import snowflake.connector
import pandas as pd

def fetch_and_display_data(query):
    snowflake_user = "MitadruChakraborty"
    snowflake_password = "Abcd1234@"
    snowflake_account = "eygds-lnd_dna_az_1"
    snowflake_warehouse = "LLM_WH"
    snowflake_database = "LLM_CHATBOT"
    snowflake_schema = "DATA"
    
    conn = snowflake.connector.connect(
        user=snowflake_user,
        password=snowflake_password,
        account=snowflake_account,
        warehouse=snowflake_warehouse,
        database=snowflake_database,
        schema=snowflake_schema,
        role="LLM_RL"
    )
    
    cursor = conn.cursor()
    
    try:
        if query.strip() == '':
            raise ValueError("Query is empty")
        
        cursor.execute(query)
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(data, columns=columns)
        return df
    
    except snowflake.connector.errors.ProgrammingError as e:
        return pd.DataFrame({0:[str(f"Query didn't produce any data or it has a syntax issue {e}")]})
    
    except Exception as e:
        return pd.DataFrame({0:[str(f"Query didn't produce any data or it has a syntax issue {e}")]})
    
    finally:
        cursor.close()
        conn.close()
