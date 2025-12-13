prices = [29.99, 45.50, 12.75, 38.20]
discounts = [0.10,0.20,0.15,0.05]
#updated_price =[] # méthode liste
for i in range(len((prices))):
    prices[i] *= (1-discounts[i])
    print (f"Updated price for item {i}: §{prices[i]:.2f}")
    
    ''' la méthode liste  avec "updated_price" est bonne mais la validation se fait sur
    la liste "prices" qui ne change pas'''
    #updated_price.append(prices[i]*(1-discounts[i]))
    #print (f"Updated price for item {i}: {updated_price[i]:.2f}")
    
    
    

    