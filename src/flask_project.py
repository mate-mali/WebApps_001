from flask import Flask, render_template, request, redirect, url_for
import sqlite3 
app = Flask(__name__)


@app.route("/")
def home():
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM movies')
    # for row in cursor:
    #     outputx.append([row[0], row[1], row[2], row[3]])
    return render_template('home.html', movies = cursor)
    # db.close()

@app.route("/addMovies", methods=['GET', 'POST', 'DELETE'])
def add_movies():
    if request.method == 'POST':
        movieTitle = request.form.get('title')
        movieYear = request.form.get('year')
        movieActors = request.form.get('actors')
        print(movieTitle, movieYear, movieActors)
        db = sqlite3.connect('movies.db')
        cursor = db.cursor()
        cursor.execute(f'''
                        INSERT INTO movies 
                       (title, year, actors)
                       values(
                       '{movieTitle}',
                       '{movieYear}',
                       '{movieActors}'
                       )
                       ''')
        db.commit()
        # db.close()
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run()
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.debug = True