import psycopg2

db_url = ""

def fastQuery(db_url):
        try:
                conn = psycopg2.connect(db_url)
                cur = conn.cursor()

                # Execute a query to get the PostgreSQL version
                cur.execute("SELECT b.*, c.* FROM book AS b JOIN customer AS c ON b.bookID = c.CustomerID WHERE b.price > 10 AND pgp_sym_decrypt(b.story, 'encryption_key') LIKE '%Fiction%' AND c.CustomerName LIKE '%Doe%' AND b.genre LIKE '%Fiction%' AND b.publishDate < '2000-01-01';")

                # Fetch and print the result
                row = cur.fetchone()
                while row is not None:
                  print(row[0])
                  row = cur.fetchone()

        except psycopg2.DatabaseError as error:
                print(f"Error with database {db_url}: {error}")
        finally:
                # Ensure that the cursor and connection are closed
                print(f"SQL command executed in database: {db_url}")
                if 'cur' in locals():
                    cur.close()
                if 'conn' in locals():
                    conn.close()

fastQuery(db_url)