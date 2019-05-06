import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """This function will ingest the data from the files in S3 to the staging tables using the COPY command from Redshift."""
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """This function will ingest the remain tables. It uses the staging tables that were ingested before from S3."""
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """This main function will ingest the data in the main tables for Sparkify. It asumes that the main tables are already created."""
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()