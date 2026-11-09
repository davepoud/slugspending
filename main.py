
valuedict = {"grocery":0, #grocery
             "restaurant":0, #restaurant
             "gas":0, #gas
             "rent":0} #rent

def end():
    choice = int(input("Press 1 to end the program or 2 to go back to the main menu."))
    if choice == 1:
        exit()
    else:
        return

def sum_up(dict):
    return sum(dict.values())

def percent(dict, key, total):    
    x = dict[key] / total
    return ("{:.2%}".format(x))



while True:

    select = int(input("What did you want to do today? \n1. Add a new payment \n2. View categories \n3. Total Spending for the Month \nEnter your numerical value:"))

    if (3<select or select<1):
        print("Try again.\n")
        continue

    if (select == 1):
      
        catinput = input("Enter which category your purchase was in: grocery, restaurant, gas or rent\n")

        if (catinput not in valuedict.keys()):
            print("Please enter a category from those listed.\n")
            continue

        else:

            valinput = int(input("Enter an amount\n"))
            valuedict[catinput] += valinput
            print (valuedict[catinput])            
            end()

    elif (select == 2):

        print ("Rent Payment = " + str(valuedict["rent"]) + " Groceries = " + str(valuedict["grocery"])+ " Restaurants = " + str(valuedict["restaurant"]))
        end()
    elif (select == 3):

        total = sum_up(valuedict)
        if (total == 0):
            print("You have not spent any money this month")
            end()
        else:
            print ("Total spent: " + str(total))
            for key in valuedict.keys():
                ratio = percent(valuedict, key, total)
                print ("You spent " + ratio + "on " + key + ".") 
                end()
