import sqlite3

def execute_query(filename, params=None):
    # Read the SQL query from the file
    with open(filename, 'r') as f:
        sql = f.read()

    # Connect to the database
    with sqlite3.connect('db_lite.sqlite') as con:
        cur = con.cursor()
        
        try:
            # Execute the query with parameters if provided, else just execute without parameters
            if params:
                cur.execute(sql, params)
            else:
                cur.execute(sql)
            
            # Fetch the results
            results = cur.fetchall()
            
            # Get column names
            column_names = [description[0] for description in cur.description]
            
            # Print column names
            print(" | ".join(column_names))
            print("-" * (sum(len(name) for name in column_names) + 3 * (len(column_names) - 1)))
            
            # Print results
            for row in results:
                print(" | ".join(str(item) for item in row))
            
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    query_file = 'query_12.sql'
    execute_query(query_file)