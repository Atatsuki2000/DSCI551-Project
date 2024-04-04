import mysql.connector

def create_database(db_name):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="$Sammylee1021"
        )
        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database
            cursor.execute(f"CREATE DATABASE {db_name}")
            print(f"Database {db_name} created successfully")
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def drop_database(db_name):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="$Sammylee1021"
        )
        if connection.is_connected():
            cursor = connection.cursor()
            # Drop the database
            cursor.execute(f"DROP DATABASE {db_name}")
            print(f"Database {db_name} dropped successfully")
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def create_all_team_game_stats_table(db_name, table_name):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="$Sammylee1021",
            database=db_name
        )
        if connection.is_connected():
            cursor = connection.cursor()
            # Create the table
            cursor.execute(f"CREATE TABLE {table_name} (Home_Team_ID INT, Game_ID INT, GAME_DATE VARCHAR(10), HOME_TEAM_ABBR VARCHAR(3), VISITOR_TEAM_ABBR VARCHAR(3), WL VARCHAR(1), W FLOAT, L FLOAT, W_PCT FLOAT, MIN INT, FGM INT, FGA INT, FG_PCT FLOAT, FG3M INT, FG3A INT, FG3_PCT FLOAT, FTM INT, FTA INT, FT_PCT FLOAT, OREB INT, DREB INT, REB INT, AST INT, STL INT, BLK INT, TOV INT, PF INT, PTS INT)")
            print(f"Table {table_name} created successfully")
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def drop_table(db_name, table_name):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="$Sammylee1021",
            database=db_name
        )
        if connection.is_connected():
            cursor = connection.cursor()
            # Drop the table
            cursor.execute(f"DROP TABLE {table_name}")
            print(f"Table {table_name} dropped successfully")
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def show_databases():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="$Sammylee1021"
        )
        if connection.is_connected():
            cursor = connection.cursor()
            # Show the databases
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            for database in databases:
                print(database)
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def use_database(db_name):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="$Sammylee1021",
            database=db_name
        )
        if connection.is_connected():
            print(f"Connected to database {db_name}")
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

def show_tables(db_name):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="$Sammylee1021",
            database=db_name
        )
        if connection.is_connected():
            cursor = connection.cursor()
            # Show the tables
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            for table in tables:
                print(table)
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def show_data(db_name, table_name):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="$Sammylee1021",
            database=db_name
        )
        if connection.is_connected():
            cursor = connection.cursor()
            # Show the data
            cursor.execute(f"SELECT * FROM {table_name}")
            data = cursor.fetchall()
            for row in data:
                print(row)
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def insert_data(db_name, table_name, data):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="$Sammylee1021",
            database=db_name
        )
        if connection.is_connected():
            cursor = connection.cursor()
            # Inserting each row
            for i, row in data.iterrows():
                cursor.execute(f"INSERT INTO {table_name} VALUES {tuple(row)}")
                connection.commit()
            print("Data inserted successfully")
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def insert_all_team_game_stats_data(dataframe, db_index):
    try:
        # Determine the database to connect based on the db_index
        database_name = f"nba_{db_index}"
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="$Sammylee1021",
            database=database_name
        )
        if connection.is_connected():
            cursor = connection.cursor()
            # Inserting each row
            for i, row in dataframe.iterrows():
                # Check the condition and insert data accordingly
                if int(row['Home_Team_ID']) % 2 == db_index:
                    sql_query = "INSERT INTO all_team_game_stats (Home_Team_ID, Game_ID, GAME_DATE, HOME_TEAM_ABBR, VISITOR_TEAM_ABBR,\
                                WL, W, L, W_PCT, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM, FTA, FT_PCT, OREB, DREB,\
                                REB, AST, STL, BLK, TOV, PF, PTS) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
                                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql_query, tuple(row))
                    connection.commit()
            print(f"Data inserted successfully for {database_name} database")
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def clear_table(database_name, table_name):
    try:
        # Determine the database to connect based on the db_index
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="$Sammylee1021",
            database=database_name
        )
        if connection.is_connected():
            cursor = connection.cursor()
            # Clear the table
            sql_query = f"DELETE FROM {table_name}"
            cursor.execute(sql_query)
            connection.commit()
            print(f"Data deleted successfully for {database_name} database")
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def sql_command(sql_query):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="$Sammylee1021"
        )
        if connection.is_connected():
            cursor = connection.cursor()
            # Execute the SQL command
            cursor.execute(sql_query)
            connection.commit()
            print("SQL command executed successfully")
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

