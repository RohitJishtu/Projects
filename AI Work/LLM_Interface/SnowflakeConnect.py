import snowflake.connector as sf
def QA_snowflake_connection(role: str ='DS_ROLE', warehouse: str ='DS_STD_WH', database: str ='EDW_LS', schema: str ='DATASCIENCE_GENAI'):
    conn_ = sf.connect(
        user=USER,
        authenticator="externalbrowser",
        account=ACCOUNT,
        role=role,
        warehouse=warehouse,
        database=database,
        schema=schema
        )
    return conn_

def Dev_snowflake_connection(role: str ='DS_ROLE', warehouse: str ='DS_STD_WH', database: str ='EDW_LS', schema: str ='DATASCIENCE_GENAI'):
    conn_ = sf.connect(
        user=USER,
        authenticator="externalbrowser",
        account=ACCOUNT,
        role=role,
        warehouse=warehouse,
        database=database,
        schema=schema
        )
    return conn_


def Lab_snowflake_connection(role: str ='DEVELOPER_ROLE', warehouse: str ='DE_PERF_L0_WH', database: str ='EDW_LS', schema: str ='DATASCIENCE_GENAI'):
    conn_ = sf.connect(
        user=USER,
        authenticator="externalbrowser",
        account=ACCOUNT,
        role=role,
        warehouse=warehouse,
        database=database,
        schema=schema
        )
    return conn_
