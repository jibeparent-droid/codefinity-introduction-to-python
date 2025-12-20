# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

revenue_list = []
def calculate_revenue(prices, quantities_sold):
    revenue_list = []                 # reset locally
    for price, qty in zip(prices, quantities_sold):
         revenue_list.append(price * qty)
    return revenue_list

    
def formated_output(prducts,revenues):
    revenue_per_product = list(zip(products, revenues))
    for product, rev in sorted(revenue_per_product):
        print(f"{product} has total revenue of ${rev}")    
        
revenue = calculate_revenue(prices,quantities_sold)
print(revenue)
formated_output(products, revenue)     
        




        
    
# Example of expected output line (do not remove):
#print(f"{revenue[0]} has total revenue of ${revenue[1]}")