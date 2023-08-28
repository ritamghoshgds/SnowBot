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

        # Wrap the query in a TRY...CATCH block for error handling within Snowflake SQL
        error_handling_query = f"""
                BEGIN
                    TRY
                        {query}
                    CATCH (error_var VARIANT)
                        RETURN PARSE_JSON('{{"error_message": "An error occurred"}}');
                    END TRY;
                END;
            """

        cursor.execute(error_handling_query)
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(data, columns=columns)
        return df

    except snowflake.connector.errors.ProgrammingError as e:
        return f"Error executing query: {e}"

    except Exception as e:
        return f"An error occurred: {e}"


    finally:
        cursor.close()
        conn.close()
