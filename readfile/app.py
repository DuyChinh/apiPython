import psycopg2
from urllib.parse import urlparse, parse_qs
from config import load_config
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
# from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__) #name contain current module

app.config['CORS_HEADERS'] = 'Content-Type'

#Connect PostgreSQL
def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    
@app.route("/") 
def home():
    return "Read File csv and add database"

@app.route("/orders")
def order():
    params = request.args.to_dict()
    # print(params)
    conn = connect(config)
    cur = conn.cursor()
    if len(params) == 0: 
        cur.execute("SELECT * FROM orders ORDER BY id ASC")
        orders = cur.fetchall()
        response = {
            "status": 200,
            "message": "Success",
            "data": orders
        }
        return response
    sql = "SELECT * FROM orders "
    sql += "WHERE "
    # print(" AND ".join(params))
    sql += " AND ".join(f"{key} = %s" for key in params.keys())
    sql += " ORDER BY id ASC"
    data = tuple(params.values())
    try:
        cur.execute(sql, data)
        orders = cur.fetchall()
        if len(orders) > 0: 
            response = {
                "count": len(orders),
                "status": 200,
                "message": "Success",
                "data": orders
            }
        else:
            response = {
                "status": 404,
                "message": "Not Found"
            }
        return response
    except: 
        response = {
            "status": 500,
            "message": "Server Error"
        }
        return response

# @app.post("/orders")
# def orderFilter():
#     params = request.args.to_dict()
#     print(params)

# @app.route("/orders/<name>")
# def orderFilter(name):
#     conn = connect(config)
#     cur = conn.cursor()
#     cur.execute("SELECT {} FROM orders ORDER BY id ASC".format(name))
#     filter = cur.fetchall()
#     response = {
#         "status": 200,
#         "message": "Success",
#         "data": filter
#     }
#     return response

def insert_orders_table(data):
    cur = conn.cursor()
    insert_query = "INSERT INTO orders(id, order_priority, discount, unit_price, shipping_cost, customer_id, customer_name, ship_mode, customer_segment, product_category, product_subcategory, product_container, product_name, product_base_margin, region, state_or_province, city, postal_code, order_date, ship_date, profit, quantity_ordered_new, sales, order_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    try: 
        cur.execute(insert_query, tuple(data.split(",")))
        cur.close()
        conn.commit()
        print("Insert success")
    except Exception as e:
        print("Insert failed:", str(e))
  
#readfile
def readfile(): 
    try:
        f = open("Orders.csv", "r") 
        arr = f.readlines()
        #read follow line
        # insert_orders_table(arr[1])
        for i in range(1, len(arr)-1):
            insert_orders_table(arr[i])
        # conn.close()
        #stop connect database
    
    except Exception as e:
            print(e)
    finally:
            f.close()
            # conn.close()

if __name__ == '__main__':
    config = load_config()
    conn = connect(config)
    # cur = conn.cursor()
    # readfile()
    # create_table()
    app.run(host='0.0.0.0', port='6868') 


