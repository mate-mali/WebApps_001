from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route("/addMovies")
def add_movies():
    #return ("<b>Jestem na stronie dodawania nowego filmu</b><a href='/'>Idz do strony domowej</a>")
    return render_template('add.html')



if __name__ == '__main__':
    app.run()