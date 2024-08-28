import pyodbc
import pandas as pd
import time

# Connection details
server = "localhost,1433"
database = "QPerformanceAnom"
username = "SA"
password = "MyStrongPass123"
connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"

# Establish connection
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()


# Function to execute a SQL query and measure its execution time
def execute_query(query, cursor):
    start_time = time.time() * 1000
    cursor.execute(query)
    cursor.commit()
    end_time = time.time() * 1000
    return end_time - start_time


# Read the txt file into a DataFrame
file_path = "./data/sql_queries.txt"
with open(file_path, "r") as file:
    queries = file.readlines()

# Create a DataFrame with one column named 'query'
df = pd.DataFrame(queries, columns=["query"])

processing_times = []
for query in df["query"]:
    try:
        processing_time = execute_query(query.strip(), cursor)
    except Exception as e:
        print(f"Error executing query: {query.strip()}")
        print(f"Error message: {e}")
        processing_time = None
    processing_times.append(processing_time)

# Append the processing times to the DataFrame
df["processing_time"] = processing_times

# Save the DataFrame to a new CSV file
df.to_csv("queries_with_processing_times.csv", index=False)


# Close the connection
cursor.close()
conn.close()
