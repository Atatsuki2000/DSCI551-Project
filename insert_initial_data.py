import os
import pandas as pd
import sqlalchemy

# MySQL connection details
username = 'root'
password = '$Sammylee1021'  # Replace with your actual MySQL password
host = 'localhost'
port = '3306'  # Default MySQL port

# Paths for data shards
data_paths = {
    'nba_0': 'for_import_data/0',
    'nba_1': 'for_import_data/1'
}

# Create an engine to connect to MySQL
engine = sqlalchemy.create_engine(f'mysql://{username}:{password}@{host}:{port}')

# Function to execute SQL schema
def execute_sql_schema():
    # Connect to MySQL
    connection = engine.connect()
    # Execute SQL commands from schema.sql file
    with open('schema.sql', 'r') as file:
        schema_sql = file.read()
    commands = schema_sql.split(';')
    for command in commands[:-1]:
        connection.execute(sqlalchemy.text(command))
    connection.close()
    print("Schema executed successfully.")

# Function to import CSV data into the database
def import_data(db_name, path):
    connection = engine.connect()
    for filename in os.listdir(path):
        if filename.endswith('.csv'):
            table_name = filename.replace('.csv', '')
            file_path = os.path.join(path, filename)
            data = pd.read_csv(file_path)
            data.to_sql(table_name, con=connection, if_exists='append', index=False)
            print(f"Data from {filename} imported into {table_name} in {db_name}.")
    connection.close()

# Run schema execution
execute_sql_schema()

# Execute import for both databases
for db, path in data_paths.items():
    import_data(db, path)
