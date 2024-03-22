import psycopg2
from config import load_config
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
# from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__) #name contain current module

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
#--> Follow change

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
    
# có các column là các cột trong file csv này
# sau đó viết code python load dữ liệu vào postgres nhé
# rồi sử dụng project flask hôm trước viết thêm 1 route orders, để query orders trong file này ra, có hỗ trợ filter theo các params

@app.route("/") 
@cross_origin(origin='*')

def home():
    return "API LOGIN"

def printData(list_content): 
    print(list_content)

def create_table():
    print("creating")
    cur = conn.cursor()
    create_table_query = '''CREATE TABLE orders (
        id INTEGER PRIMARY KEY,
        order_priority CHARACTER VARYING,
        discount NUMERIC,
        unit_price NUMERIC, 
        shipping_cost NUMERIC,
        customer_id INTEGER,
        customer_name CHARACTER VARYING,
        ship_mode CHARACTER VARYING, 
        customer_segment CHARACTER VARYING,
        product_category CHARACTER VARYING,
        product_subCategory CHARACTER VARYING,
        product_container CHARACTER VARYING,
        product_name CHARACTER VARYING,
        product_base_margin NUMERIC,
        region CHARACTER VARYING,
        state_or_province CHARACTER VARYING,
        city CHARACTER VARYING,
        postal_code INTEGER,
        order_date DATE,
        ship_date DATE,
        profit NUMERIC,
        quantity_ordered_new INTEGER,
        sales NUMERIC,
        order_id INTEGER
    )'''
    try: 
        cur.execute(create_table_query)
        print("Create table success")
    except:
        print("Fail")
    

def table_exists(table_name, cursor):
    cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s)", (table_name,))
    return cursor.fetchone()[0]

if __name__ == '__main__':
    config = load_config()
    conn = connect(config)
    cur = conn.cursor()
    if not table_exists('orders', cur):
        create_table()

    cur.execute('SELECT * FROM orders')
    orders = cur.fetchall()
    print(orders)
    # app.run(host='0.0.0.0', port='6868') 
    





# try:
#     f = open("Orders.csv", "r") 
#     list_content = f.readline().strip().split(',')
#     # printData(list_content)
#     create_table()
# except Exception as e:
#         print(e)
# finally:
#         f.close()
#         conn.close()