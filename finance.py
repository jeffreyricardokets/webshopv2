from models import *

#earning filter
def show_revenue(first_date,second_date):
    print('test')
    orders = Orders.select().where(Orders.order_date.between(first_date,second_date))
    if orders.exists():
        revenue_counter = 0
        for order in orders:
            revenue_counter = revenue_counter + order.product_price
        return print(f"the revenenue from the selected date's is : {round(revenue_counter,2)} euro's")
    else:
        return print('no record found')