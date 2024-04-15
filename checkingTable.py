import psycopg2

db_url = "postgres://gvdulkma:RPuoPh_iTN-1XwDnpkrBIsmTMqyiDo0f@bubble.db.elephantsql.com/gvdulkma"

try:
        conn = psycopg2.connect(db_url)
        cur = conn.cursor()

        # Execute a query to get the PostgreSQL version
        cur.execute("SELECT bookID, title, genre, author, publishDate, price, pgp_sym_decrypt(story::bytea, 'encryption_key') from book;")

        # Fetch and print the result
        count = 1
        row = cur.fetchone()
        while row is not None:
          print(row)
          count = count + 1
          print(count)
          row = cur.fetchone()
except psycopg2.DatabaseError as error:
        print(f"Error with database {db_url}: {error}")
finally:
        # Ensure that the cursor and connection are closed
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()