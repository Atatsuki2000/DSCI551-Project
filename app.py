from flask import Flask,render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '$Sammylee1021'
app.config['MYSQL_DB'] = 'nba_0'

mysql = MySQL(app)


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/all_team_game_stats')
def all_team_game_stats():
    cur = mysql.connection.cursor()
    all_team_game_stats = cur.execute("SELECT * FROM all_team_game_stats")
    if all_team_game_stats > 0:
        playerstats = cur.fetchall()
        return render_template('all_team_game_stats.html', playerstats=playerstats)
if __name__ == '__main__':
    app.run(debug=True)

 


