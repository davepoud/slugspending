import json
import matplotlib.pyplot as plt

def add_cat(dict):
    name = input("What would you like your catgeory to be named?")
    number = int(input("How much have you spend on " + name+"?"))
    dict[name] = number
    save_data(dict)
    return

def del_cat(dict):
    for key in dict:
        if (key != "recurring"):
            print (key)
    name = input("\nWhat category would you like to delete? Your options are listed above: ")
    if name not in dict:
        print("Name not found, try again.")
        del_cat(dict)
    else:
        if (key!="recurring"):
            del dict[name]
            save_data(dict)
            return
    
def load_data():
    try:
        with open ("values.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return { 
             "grocery":0, #grocery
             "restaurant":0, #restaurant
             "gas":0, #gas
             "rent":0, #rent
             "recurring":0
             } 

def save_data(data):
    with open("values.json", "w") as file:
        json.dump(data, file, indent= 4)

def end():
    choice = input("\nPress 1 to end the program or press enter to go back to the main menu: ")
    if choice == "1":
        exit()
    else:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        return

def sum_up(dict):
    return sum(dict.values())

def percent(dict, key, total):    
    x = dict[key] / total
    return ("{:.2%}".format(x))

def clear_data(dict):
    recur1 = input("Input 1 to clear recurring payments as well: ")
    for val in dict:
        if val!="recurring":
            dict[val] = 0
    if recur1 == "1":
        dict["recurring"]=0
    return

valuedict=load_data()

while True:

    select = int(input("What did you want to do today? \n1. Add a new payment \n2. View categories \n3. Total Spending for the Month \n4. Clear Data \n5. Exit \n6. Add or Delete Categories \nEnter your numerical value: "))

    if (6<select or select<1):
        print("Try again.")
        continue


    if (select == 1):
        for key in valuedict:
            if key != ("recurring"):
                print (key)
        catinput = input("Enter which category your purchase was in from the ones listed above: ")
        if (catinput not in valuedict.keys()):

            print("Please enter a category from those listed.")
            continue
        else:
            valinput = int(input("Enter an amount: "))
            valuedict[catinput] += valinput            
            recur = int(input("Enter 1 if this is a recurring monthly payment and 0 otherwise: "))
            if (recur == 1):
                    valuedict["recurring"]+=valinput
            save_data(valuedict)
            end()




    elif (select == 2):
        for key in valuedict:
            print (key + ": " + str(valuedict[key])) 

        filtered_data = {k: v for k, v in valuedict.items() if v != 0 and k!="recurring"}
        
        plt.pie(filtered_data.values(), labels = filtered_data.keys(), autopct='%1.1f%%')
        plt.title = ("Financial distribution")
        plt.savefig('filename.png')
        end()



    elif (select == 3):

        total = sum_up(valuedict)
        if (total-valuedict["recurring"] == 0):
            print("\nYou have not spent any money this month")
            end()
        else:
            print ("\nTotal spent: " + str(total-valuedict["recurring"]))
            print("You spent " + str(valuedict["recurring"]) + " on recurring payments\n")
            for key in valuedict.keys(): 
                if key == "recurring":
                    continue
                else:
                    ratio = percent(valuedict, key, total-valuedict["recurring"])
                    print ("You spent " + ratio + " on " + key + ".") 
            end()



    elif (select == 4):
        check = int(input("Are you sure you want to clear your data? Press 1 to continue any other button otherwise"))
        if (check == 1):
            clear_data(valuedict)
            save_data(valuedict)
            print("\nData Successfully Cleared!")
            end()
            continue

        else:
            continue
        
    elif (select == 5):
        exit()

    elif (select == 6):
        choice_add_del=input("Press 1 to add an element and 2 to delete an element")
        if (choice_add_del == "1"):
            add_cat(valuedict)
        elif (choice_add_del == "2"):
            del_cat(valuedict)
        end()

