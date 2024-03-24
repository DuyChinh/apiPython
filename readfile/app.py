import psycopg2
from config import load_config
from flask import Flask, request
from flask_cors import CORS, cross_origin
from connect_database import connect
from routes import home, order
from file import readfile
app = Flask(__name__) #name contain current module

app.config['CORS_HEADERS'] = 'Content-Type'
    
@app.route("/")
def main():
    return home()

@app.route("/orders")
def orders():
    return order()

#readfile


if __name__ == '__main__':
    config = load_config()
    conn = connect(config)
    # cur = conn.cursor()
    readfile()
    # create_table()
    app.run(host='0.0.0.0', port='6868') 


