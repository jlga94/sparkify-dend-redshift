import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """This function drops all the tables in the database specified in the connection and in the list in 'sql_queries.py'."""
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """This function creates all the tables in the database specified in the connection and in the list in 'sql_queries.py'."""
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """This is the main function. It reads the credentials from Redshift in dwh.cfg, and drops tables and creates tables."""
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()