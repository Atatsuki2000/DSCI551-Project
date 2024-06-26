CREATE TABLE IF NOT EXISTS all_draft_picks(
    person_id INTEGER,
    player_name varchar(50),
    season INTEGER,
    round_num INTEGER,
    round_pick INTEGER,
    overall_pick INTEGER,
    draft_type varchar(50),
    team_id INTEGER,
    team_city varchar(50),
    team_name varchar(50),
    team_abbr varchar(3),
    organization varchar(50),
    organization_type varchar(50),
    player_profile_flag varchar(1),
    primary key (person_id)
);

CREATE TABLE IF NOT EXISTS current_players(
    person_id INTEGER,
    player_name varchar(50),
    from_year INTEGER,
    to_year INTEGER,
    team_id INTEGER,
    team_city varchar(50),
    team_name varchar(50),
    team_abbr varchar(3),
    games_played_flag varchar(1),
    primary key (person_id),
    unique key (player_name),
    index (person_id),
    foreign key (person_id) references all_draft_picks(person_id) on delete cascade on update cascade
);

CREATE TABLE IF NOT EXISTS all_players_season_stats_2023_2024(
    player_name varchar(50),
    team_id INTEGER,
    team_abbr varchar(3),
    max_game_date DATE,
    GP INTEGER,
    W INTEGER,
    L INTEGER,
    W_PCT REAL,
    MIN REAL,
    FGM INTEGER,
    FGA INTEGER,
    FG_PCT REAL,
    FG3M INTEGER,
    FG3A INTEGER,
    FG3_PCT REAL,
    FTM INTEGER,
    FTA INTEGER,
    FT_PCT REAL,
    OREB INTEGER,
    DREB INTEGER,
    REB INTEGER,
    AST INTEGER,
    TOV INTEGER,
    STL INTEGER,
    BLK INTEGER,
    BLKA INTEGER,
    PF INTEGER,
    PFD INTEGER,
    PTS INTEGER,
    PLUS_MINUS INTEGER,
    NBA_FANTASY_PTS INTEGER,
    DD2 INTEGER,
    TD3 INTEGER,
    WNBA_FANTASY_PTS INTEGER,
    GP_RANK INTEGER,
    W_RANK INTEGER,
    L_RANK INTEGER,
    W_PCT_RANK INTEGER,
    MIN_RANK INTEGER,
    FGM_RANK INTEGER,
    FGA_RANK INTEGER,
    FG_PCT_RANK INTEGER,
    FG3M_RANK INTEGER,
    FG3A_RANK INTEGER,
    FG3_PCT_RANK INTEGER,
    FTM_RANK INTEGER,
    FTA_RANK INTEGER,
    FT_PCT_RANK INTEGER,
    OREB_RANK INTEGER,
    DREB_RANK INTEGER,
    REB_RANK INTEGER,
    AST_RANK INTEGER,
    TOV_RANK INTEGER,
    STL_RANK INTEGER,
    BLK_RANK INTEGER,
    BLKA_RANK INTEGER,
    PF_RANK INTEGER,
    PFD_RANK INTEGER,
    PTS_RANK INTEGER,
    PLUS_MINUS_RANK INTEGER,
    NBA_FANTASY_PTS_RANK INTEGER,
    DD2_RANK INTEGER,
    TD3_RANK INTEGER,
    WNBA_FANTASY_PTS_RANK INTEGER,
    foreign key (player_name) references current_players(player_name) on delete cascade on update cascade
);

CREATE TABLE IF NOT EXISTS player_info(
    name varchar(50),
    position varchar(20),
    height varchar(6),
    weight INTEGER,
    last_attended varchar(50),
    country varchar(50),
    foreign key (name) references current_players(player_name) on delete cascade on update cascade
);

CREATE TABLE IF NOT EXISTS user_info(
    user_id INTEGER AUTO_INCREMENT,
    user_name varchar(50) NOT NULL,
    email varchar(50) NOT NULL,
    password_hash varchar(2000) NOT NULL,
    primary key (user_id),
    unique key (user_name),
    unique key (email)
);