from connect_database import connect
from config import load_config
from flask import Flask, request, render_template

def home():
    return "Read File csv and add database"

def order():
    params = request.args.to_dict()
    # print(params)
    config = load_config()
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