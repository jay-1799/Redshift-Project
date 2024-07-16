import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()

def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    config = configparser.ConfigParser()
    config.read('dhw.cfg')  # Ensure the correct file name

    # Extract configuration details
    host = config.get('CLUSTER', 'HOST')
    dbname = config.get('CLUSTER', 'DB_NAME')
    db_port = config.get('CLUSTER', 'DB_PORT')
    iam_role = config.get('IAM_ROLE', 'ARN')

    # Establish connection
    conn = psycopg2.connect(
        dbname=dbname,
        host=host,
        port=db_port,
        user='',  # For Redshift Serverless, IAM role is used, user/password may not be needed
        password=''  # If IAM role is used, password may not be needed
    )
    cur = conn.cursor()

    # Load staging tables
    load_staging_tables(cur, conn)
    # Insert data into final tables
    insert_tables(cur, conn)

    # Close connection
    conn.close()

if __name__ == "__main__":
    main()
