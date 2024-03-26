import csv
def load_orders():
    listOrders=[]
    with open(r'C:\Users\DuyChinhPro\Downloads\Orders.csv', encoding='latin1') as f:
        readfile = csv.reader(f)
        for row  in readfile:
          #print(row)
          keys = row
          break
        for row in readfile:
            dictArr = {}
            for i in range(len(keys)):
                dictArr[keys[i]] = row[i]
            listOrders.append(dictArr)
    return listOrders  

def create_customer_dict():
    orders = load_orders()
    customer_dict = {}
    
    for order in orders:
        customer_id = order['Customer ID']
        customer_name = order['Customer Name']
        unit_price = float(order['Unit Price'])
        quantity = int(order['Quantity ordered new'])
        shippingCost = float(order['Shipping Cost'])
        
        total_bill = unit_price * quantity + shippingCost
        
        if customer_id in customer_dict:
            customer_dict[customer_id]['total_order'] += 1
            customer_dict[customer_id]['total_bill'] += total_bill
        else:
            customer_dict[customer_id] = {
                'id': customer_id,
                'customer_name': customer_name,
                'total_order': 1,
                'total_bill': total_bill
            }
        
    return customer_dict
   
def find_customer_with_max_orders():
    customer_dict = create_customer_dict()
    max_orders = 0
    list_max_orders = []
    for customer_id, order in customer_dict.items(): 
        total_order = order['total_order']
        if total_order > max_orders:
            max_orders = total_order
        elif total_order == max_orders:
            list_max_orders.append((customer_id, order))
    return list_max_orders   
# list = create_customer_dict()
# print(list)
# create_customer_dict()
# list_max_orders = find_customer_with_max_orders()
# print(list_max_orders)
# return customer vs total order
# normal:  < 1000, vip: 1000 -> 2000, VVIP:  > 2000

def find_rank_customer():
    customer_dict = create_customer_dict()
    list_rank_customer_normal = []
    list_rank_customer_vip = []
    list_rank_customer_vvip = []
    
    for customer_id, order in customer_dict.items():
        total_bill = order['total_bill']
        if total_bill <= 1000:
            list_rank_customer_normal.append((order, 'NORMAL'))
        elif total_bill > 1000 and total_bill <= 2000:
            list_rank_customer_vip.append((order, 'VIP'))
        elif total_bill > 2000:
            list_rank_customer_vvip.append((order, 'VIPpro'))
    print("normal customer: ", list_rank_customer_normal[:5])
    print("===============================================")
    print("vip customer: ", list_rank_customer_vip[:5])
    print("===============================================")
    print("vvip customer: ", list_rank_customer_vvip[:5])
    
    

find_rank_customer()



      
