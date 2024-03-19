import psycopg2
from config import load_config
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
message = ""
@app.route("/") 
def home():
    return "API LOGIN"


@app.get("/login")
@cross_origin(origin='*')
def get_info():
    return render_template("login.html")


@app.post("/login")
@cross_origin(origin='*')
def get_name():
    username = request.form.get("username")
    password = request.form.get("password")
    conn = connect(config)
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE (name=%s OR email=%s) and password=%s', (username, username, password))
    user = cur.fetchall()
    conn.commit()
    conn.close()
    if not user:
        response = {
            "status": 404,
            "message": "password or username is incorrect"
        }
    else:
        response = {
            "status": 200,
            "message": "Login success",
            "data": {
                "id": user[0][0],
                "username": user[0][2],
                "email": user[0][1],
                "password": user[0][3]
            }
        }
        
    return response


@app.get("/users")
@cross_origin(origin='*')
def get_users():
    conn = connect(config)
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    conn.commit()
    conn.close()
    response = {
        "status": 200,
        "message": "Success",
        "data": users
    }
    return response

if __name__ == '__main__':
    config = load_config()
    app.run(host='0.0.0.0', port='6868') 
    