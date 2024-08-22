import psycopg2
import pandas as pd

def extract_data(input_config):
    db_url = input_config["db"]["url"]
    table = input_config["db"]["table"]

    conn_params = db_url.replace("postgresql://", "").split(":")
    user, password_host = conn_params[0], conn_params[1].split("@")
    password, host_port = password_host[0], password_host[1].split(":")
    host, port_db = host_port[0], host_port[1].split("/")

    conn = psycopg2.connect(
        dbname=port_db[1],
        user=user,
        password=password,
        host=host,
        port=port_db[0]
    )
    
    query = f"SELECT * FROM {table}"
    df = pd.read_sql(query, conn)
    
    conn.close()
    
    return df
