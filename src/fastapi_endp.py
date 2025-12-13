from fastapi import FastAPI
import requests as r
import sqlite3

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
@app.get("/sum")
def sum(x: int = 0, y: int = 10):
    return x+y


@app.get("/geocode")
def sum(lat: float, lon: float):
    response = r.get(
        f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=jsonv2",
        headers={"User-Agent": "Mozilla/5.0"}
    )
    return response.json()

@app.get("/get_movies")
def get_movies():

    otp = []
    #http://127.0.0.1:8000/
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()
    cursor.execute(f'''
                    select * from movies
                    ''')
    for movie in cursor:
        moviex = {'id': row[0], 'title': row[1], 'year':row[2], '':row[3]}
    db.close()
    otp.append(moviex)
    
    return(otp)



# @app.get("/movies/{name}")
# def movies(like = null):
#     db = sqlite3.connect('movies.db')
#     cursor = db.cursor()
#     cursor.execute(f'''
#                     select * from movis where name = 
#                     ''')
#     db.commit()

# @app.get("/movies/{name}")
# def movies(like = null):
#     db = sqlite3.connect('movies.db')
#     cursor = db.cursor()
#     cursor.execute(f'''
#                     select * from movis where name = 
#                     ''')
#     db.commit()