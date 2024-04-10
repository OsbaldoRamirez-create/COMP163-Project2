import psycopg2
from psycopg2 import sql

db_url = ""

create_table_book = sql.SQL("""
CREATE TABLE IF NOT EXISTS book (
    bookID SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    author TEXT NOT NULL,
    publishDate DATE NOT NULL,
    price DECIMAL NOT NULL,
    description bytea
    );
""")

create_table_customer = sql.SQL("""
CREATE TABLE IF NOT EXISTS customer (
    CustomerID SERIAL PRIMARY KEY,    
    CustomerName TEXT NOT NULL,
    CustomerNumber TEXT NOT NULL,
    CustomerEmail TEXT NOT NULL
    );
""")

def create_table_in_database(db_url):
    try:
        # Connect to the database using the database URL
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()
        
        # Execute the create table command
        cur.execute(create_table_book)
        cur.execute(create_table_customer)
        
        # Commit the changes
        conn.commit()
        
        print("Tables 'book' and 'customer' created successfully in database:", db_url)
        
    except psycopg2.DatabaseError as e:
        print(f"An error occurred in database {db_url}: {e}")
    finally:
        # Close communication with the database
        if cur: cur.close()
        if conn: conn.close()

create_table_in_database(db_url)