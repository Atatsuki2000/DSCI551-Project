from flask import Flask,render_template, request, flash
from flask_mysqldb import MySQL

app = Flask(__name__)


# Set a secret key
app.secret_key = 'dsci551'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '$Sammylee1021'
app.config['MYSQL_DB'] = 'nba_0'

mysql = MySQL(app)


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/all_team_game_stats', methods=['GET', 'POST']) #TODO
def all_team_game_stats():
    cur = mysql.connection.cursor()
    all_team_game_stats = cur.execute("SELECT * FROM all_team_game_stats")
    if all_team_game_stats > 0:
        playerstats = cur.fetchall()
        return render_template('all_team_game_stats.html', playerstats=playerstats)
    
@app.route('/player_stats/<int:player_id>', methods=['GET', 'POST'])
@app.route('/player_stats/<string:player_name>', methods=['GET', 'POST'])
def player_stats(player_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT ps.*, cp.person_id FROM all_players_season_stats_2023_2024 ps JOIN current_players cp ON ps.player_name = cp.player_name WHERE person_id = %s", (player_id,))
    player_stat = cur.fetchone()
    cur.close()

    # Flash player_stat for debugging
    flash(player_stat)

    return render_template('player_stats.html', player_stat=player_stat)
    

if __name__ == '__main__':
    app.run(debug=True)

 


