# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenue_list = []                 # reset locally
    for price, quantity in zip(prices, quantities_sold):
         revenue_list.append(price * quantity)
    return revenue_list

    
def formatted_output(products,revenues):
    revenue_per_product = list(zip(products, revenues))
    for product, revenue in sorted(revenue_per_product):
        print(f"{product} has total revenue of ${revenue}")    
        
revenues = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenues))
formatted_output(products, revenues)
        




        
    
# Example of expected output line (do not remove):
#print(f"{revenue[0]} has total revenue of ${revenue[1]}")