import mysql.connector
def insert_data(dataframe, db_index):
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
def clear_table(table_name, db_index):
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
            