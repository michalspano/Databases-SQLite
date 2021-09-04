# Import module to parse command line arguments
from sys import argv, exit

# Import sqlite3 module
import sqlite3

# Import pandas
import pandas as pd

# Import time module (log)
import datetime

def main():
    begin = datetime.datetime.now()

    # Check for correct number of command-line arguments
    if len(argv) != 3: 
        exit("Usage: python3 $DATABASE_PATH #QUERY_PATH")

    # Store paths
    database_path, query_path = argv[1], argv[2]

    # Load the content from an SQL query
    with open(query_path) as query:
        temp = query.readlines()[1:][0]

    # Connect to SQLite
    con = sqlite3.connect(argv[1])

    # Create a cursor
    cur = con.cursor()

    # Read to dict from SQL and cursor (with selected query)
    data_base: dict = [row for row in cur.execute(temp)]

    # Assign to a DataFrame
    df = pd.DataFrame(data=data_base, index=[i + 1 for i in range(len(data_base))])

    # Print DataFrame
    print(df)

    end = datetime.datetime.now()

    # Print running time
    print(f"\nRunning time {end - begin}s")


# Define main executable
if __name__ == '__main__':
    main()
