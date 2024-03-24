from query import insert_orders_table

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