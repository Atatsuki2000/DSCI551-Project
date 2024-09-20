# DSCI 551 Final Project

## Name of the Project

NBA Games Real Time Database

## Project File Structure Overview

This README provides an overview of the directory and file structure for this project, which is designed to interact with NBA data using a Flask web application and MySQL databases.

### Directory Structure

#### `Data`
This directory stores the raw data for the project.
- `0`: Contains data for the `nba_0` database.
- `1`: Contains data for the `nba_1` database.

#### `for_import_data`
Stores processed data ready for import into databases. Each subdirectory contains four CSV files: `all_draft_picks.csv`, `all_players_season_stats_2023_2024.csv`, `current_players.csv`, and `player_info.csv`.
- `0`: Data for `nba_0`.
- `1`: Data for `nba_1`.

#### `static`
Contains static assets for the web application.
- `css`: This subdirectory contains the CSS file `index_styles.css` used for styling the web application.

#### `templates`
Holds all HTML files used by the Flask application.
- Files: `index.html`, `login.html`, `player_stats.html`, `query.html`, `signup.html`.

### Files Description

- **app.py**: The Flask application file that also manages connections to the MySQL server for data retrieval.
- **Data_Collecting.ipynb**: A Jupyter notebook for collecting raw data using the `nba_api` package and performing data cleaning.
- **Data_Sharding.ipynb**: A Jupyter notebook used for sharding data across the `nba_0` and `nba_1` databases.
- **insert_initial_data.py**: A Python script designed to facilitate the easy insertion of player data into databases. It handles connecting to the MySQL server, database creation, table creation, and data insertion.
- **README.md**: Provides context about the project, outlining its structure and instructions for replication.
- **schema.sql**: Contains the SQL commands to create the necessary database tables as designed for the project.

This structure supports efficient management and processing of data, allowing for a robust development environment for handling NBA statistics.

## Instructions on how to redirect the repository before running project

Before running any code, please redirect your repository to `DSCI551-Project`

### Usage

```bash
cd DSCI551-Project
```

## Instructions on how to insert initial data for the webpage to show

`insert_initial_data.py` would automatically insert initial data into local MySQL server. If you try to open the following application without inserting any data, you will only see the structure of the webpage but without any players data.

### Usage

```bash
python insert_initial_data.py password
```

Replace `password` to your local MySQL root user password. It shouldn't be empty.

## Instructions on how to open the frontend webpage

`app.py` is the python script that connects the frontend and the backend. You will need to run this script to see the webpage.

### Usage

```bash
python app.py password
```

Replace `password` to your local MySQL root user password. It shouldn't be empty.