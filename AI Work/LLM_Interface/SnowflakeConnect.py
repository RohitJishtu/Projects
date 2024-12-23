import snowflake.connector as sf
def QA_snowflake_connection(role: str ='ROLE', warehouse: str ='WH_1', database: str ='DB', schema: str ='SCHEMA'):
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

def Dev_snowflake_connection(role: str ='ROLE', warehouse: str ='WH_1', database: str ='DB', schema: str ='SCHEMA'):
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


def Lab_snowflake_connection(role: str ='ROLE', warehouse: str ='WH_1', database: str ='DB', schema: str ='SCHEMA'):
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
