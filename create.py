import psycopg2
from psycopg2 import sql

DATABASE_URLS = []


create_table_command1 = sql.SQL("""
CREATE TABLE IF NOT EXISTS book (
    
)  
""")

create_table_command2 = sql.SQL("""
CREATE TABLE IF NOT EXISTS customer (
    
)  
""")

def create_table_in_database(db_url):
    try:
        # Connect to the database using the database URL
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        
        # Execute the create table command
        cur.execute(create_table_command1)
        cur.execute(create_table_command2)
        
        # Commit the changes
        conn.commit()
        
        print("Tables 'book' and 'customer' created successfully in database:", db_url)
        
    except psycopg2.DatabaseError as e:
        print(f"An error occurred in database {db_url}: {e}")
    finally:
        # Close communication with the database
        if cur: cur.close()
        if conn: conn.close()


for db_url in DATABASE_URLS:
    create_table_in_database(db_url)