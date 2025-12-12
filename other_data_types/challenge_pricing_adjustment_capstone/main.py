grocery_inventory ={"Milk":("Dairy",3.50,8),"Eggs":("Dairy",5.50,30),"Bread":("Bakery",2.99,15),"Apples":("Produce",1.50,50)}
eggs_cat, eggs_price, eggs_stock = grocery_inventory["Eggs"]
milk_cat, milk_price, milk_stock = grocery_inventory["Milk"]
if grocery_inventory["Eggs"][1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"]=(eggs_cat, eggs_price - 1, eggs_stock)
else:
    print("The price oof Eggs is resonable")
grocery_inventory["Tomatoes"]=("Produce",1.20,30)
print("Inventory after adding tomatoes: ",grocery_inventory)
if grocery_inventory["Milk"][2]<10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"]=(milk_cat, milk_price, milk_stock + 20)
else :
    prin("Milk has sufficient stock.")
if grocery_inventory["Apples"][1]>2:
    grocery_inventory.pop("Apples")
    print ("Apples removed from inventory du to high price.")
print("Updated inventory: ",grocery_inventory)
