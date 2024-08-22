import psycopg2

def load_data(df, output_config):
    db_url = output_config["db"]["url"]
    table = output_config["db"]["table"]
    mode = output_config["mode"]

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
    cursor = conn.cursor()

    if mode == "overwrite":
        cursor.execute(f"TRUNCATE TABLE {table}")

    columns = df.columns
    values = [tuple(row) for row in df.values]
    insert_query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES %s"
    psycopg2.extras.execute_values(cursor, insert_query, values)

    conn.commit()
    cursor.close()
    conn.close()
