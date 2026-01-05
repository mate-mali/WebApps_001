from flask import Flask, render_template, request, redirect, url_for
import sqlite3 
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        db = sqlite3.connect('movies.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM movies')
        return render_template('home.html', movies = cursor)
   
    
@app.route("/deleteMovies", methods=['POST'])
def deleteMovies():
    if request.method == 'POST':
        datalist = request.form.getlist('moviesToRemove') #unique keys to remove 
        remove_ids = f"({','.join(datalist)})"
        print(remove_ids)
        db = sqlite3.connect('movies.db')
        cursor = db.cursor()
        cursor.execute(f'''
                       DELETE FROM movies 
                       WHERE 
                       ID in {remove_ids}
                       ''')
        db.commit()
        return redirect(url_for('home'))
  
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
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == '__main__':
    app.run(port=5000)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    #app.debug = True