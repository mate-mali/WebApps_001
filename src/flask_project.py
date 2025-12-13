from flask import Flask, render_template
import sqlite3 
app = Flask(__name__)

@app.route("/")
def hello_world():
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM movies')
    # for row in cursor:
    #     outputx.append([row[0], row[1], row[2], row[3]])
    return render_template('home.html', movies = cursor)
    # db.close()

@app.route("/addMovies")
def add_movies():
    #return ("<b>Jestem na stronie dodawania nowego filmu</b><a href='/'>Idz do strony domowej</a>")
    return render_template('add.html')


if __name__ == '__main__':
    app.run()