import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def drop_tables(cur, conn):
    """
    retrieves DROP statements from the list 'drop_table_queries', then excute them on the curser to drop database tables
    """
    for query in drop_table_queries:
        print('Executing drop: '+query)
        cur.execute(query)
        conn.commit()

def create_tables(cur, conn):
    """
    retrieves INSERT statements from the list 'create_table_queries', then excute them on the curser to create database tables
    """
    for query in create_table_queries:
        print('Executing create: '+query)
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

    print('Connecting to Redshift')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    print('Connected')
    cur = conn.cursor()

    print('Dropping existing tables if any')
    drop_tables(cur, conn)
    
    print('Creating tables')
    create_tables(cur, conn)

    conn.close()
    print('Created')


if __name__ == "__main__":
    main()
