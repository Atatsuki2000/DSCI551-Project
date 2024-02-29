import pandas as pd
import Database

df = pd.read_csv("./Data/all_team_game_stats.csv")

Database.insert_data(df, 0)
Database.insert_data(df, 1)