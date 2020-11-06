import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Load data from files stored in S3 bucket to the staging tables in Redshift cluster using the queries in 'sql_queries'
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Select and Transform data from staging tables into the dimensional tables using the queries in 'sql_queries'
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Connect to the Redshift database and excute the ETL pipeline: 
    - Extract songs metadata and user activity data from S3 bucket, 
    - Transform it using a staging table, 
    - Load it into dimensional tables in Redshift cluster for analysis
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
