import psycopg


# Connect to the PostgreSQL database
try:
    # Create a connection and a context manager for automatic cleanup
    with psycopg.connect("dbname=logs user=james password=ashihiro host=/var/run/postgresql port=5432") as conn:
        with conn.cursor() as cursor:

            # Execute a query to count the number of entries
            query1= "SELECT COUNT(*) FROM log_entries WHERE error_level = 'ERROR'"
            cursor.execute(query1)
            count = cursor.fetchone()[0]
            
            if(count > 5):
                with open('errors.txt', 'w') as f:
                    print(f"Number of entries in the table 'log_entries': {count}", file=f )
            
            query2 = "SELECT COUNT(*) FROM log_entries WHERE error_level = 'FATAL'"
            cursor.execute(query2)
            count1 = cursor.fetchone()[0]
            if(count1 > 1):
                with open('fatals.txt', 'w') as f:
                    print(f"Number of entries in the table 'log_entries': {count1}", file=f)

except Exception as e:
    print(f"Error: {e}")