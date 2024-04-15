import psycopg2

db_url = ""

def slowQuery(db_url):
        try:
                conn = psycopg2.connect(db_url)
                cur = conn.cursor()

                # Execute a query to get the PostgreSQL version
                cur.execute("SELECT * FROM (SELECT book.*, pgp_sym_decrypt(book.story, 'encryption_key') AS decrypted_story, customer.* FROM book JOIN customer ON book.bookID = customer.CustomerID WHERE pgp_sym_decrypt(book.story, 'encryption_key') LIKE '%Fiction%' AND book.price > 10 AND customer.CustomerName LIKE '%Doe%') AS subquery1 JOIN (SELECT book.*, pgp_sym_decrypt(book.story, 'encryption_key') AS decrypted_story, customer.* FROM book JOIN customer ON book.bookID = customer.CustomerID WHERE book.genre LIKE '%Fiction%' AND book.publishDate < '2000-01-01') AS subquery2 ON subquery1.bookID = subquery2.bookID;")

                # Fetch and print the result
                row = cur.fetchone()
                while row is not None:
                  print(row[0])
                  row = cur.fetchone()
        except psycopg2.DatabaseError as error:
                print(f"Error with database {db_url}: {error}")
        finally:
                print(f"SQL command executed in database: {db_url}")
                # Ensure that the cursor and connection are closed
                if 'cur' in locals():
                    cur.close()
                if 'conn' in locals():
                    conn.close()

slowQuery(db_url)