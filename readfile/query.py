from connect_database import connect
from config import load_config

def insert_orders_table(data):
    config = load_config()
    conn = connect(config)
    cur = conn.cursor()
    insert_query = "INSERT INTO orders(id, order_priority, discount, unit_price, shipping_cost, customer_id, customer_name, ship_mode, customer_segment, product_category, product_subcategory, product_container, product_name, product_base_margin, region, state_or_province, city, postal_code, order_date, ship_date, profit, quantity_ordered_new, sales, order_id) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    try: 
        cur.execute(insert_query, tuple(data.split(",")))
        cur.close()
        conn.commit()
        print("Insert success")
    except Exception as e:
        print("Insert failed:", str(e))