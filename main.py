totalexpenses_value = 0
grocery_value = 0
restaurant_value = 0
gas_value = 0
rent_value = 0 



while True:

    select = int(input("What did you want to do today? 1.add 2.view cat 3.view total \n"))

    if (3<select or select<1):
        print("retry\n")
        
    if (select == 1):
      
        valinput = int(input("Enter an amount\n"))
        catinput = int(input("Enter which category: 1 for grocery, 2 for restaurant 3 for gas 4 for rent\n"))

        
        if (catinput not in valuedict):
                       print("error reading value\n")
        
        valuedict = {1:grocery_value, 2:restaurant_value, 3:gas_value, 4:rent_value}
        
                       

        
    elif (select == 2):

        dict = {"Rent Payment = ": rent_value, "Groceries = ": grocery_value, "Restaurants = ": restaurant_value}

        for key, value in dict.items():
            print (key, value)
