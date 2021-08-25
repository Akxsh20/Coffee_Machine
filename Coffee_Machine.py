import art
print(art.logo)
def payment(order):
    print("Please Insert Coins")
    Paycheck=float(input("Enter Quarters: ")) * 0.25
    Paycheck+=float(input("How many Nickels: ")) * 0.10
    Paycheck+=float(input("How many Dimes: ")) * 0.05
    Paycheck+=float(input("How many Pennies: ")) * 0.1

    if Paycheck == Menu[order]["cost"]:
        print(f"\nYour order Cost: ${Menu[order]['cost']}")
        print(f"Your Paid Amount: ${Paycheck}")
        print("Enjoy your Coffee & Have  A nice Day!!")
        return Paycheck
    elif Paycheck > Menu[order]["cost"]:
        balance=Paycheck-Menu[order]["cost"]
        print(f"\nYour order Cost: ${Menu[order]['cost']}")
        print(f"Your Paid Amount: ${Paycheck}")
        print(f"Your change: ${balance}")
        print("Enjoy your Coffee &1"
              " Have  A nice Day!!")
        return Paycheck-balance
    else:
        print("Insufficient Amount")
        return
def Check_Availability(order):
    if(report["Water"] >= Menu[order]["ingredients"]["water"]) and (
            report["Coffee"] >= Menu[order]["ingredients"]["coffee"])\
            and (report["Milk"] >= Menu[order]["ingredients"]["milk"]):
        report["Water"] -= Menu[order]["ingredients"]["water"]
        report["Coffee"] -= Menu[order]["ingredients"]["coffee"]
        report["Milk"] -= Menu[order]["ingredients"]["milk"]
        return 0
    else:
        return 1
Menu = {
    "Espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
            "milk":0
        },
    "cost":1.50
    },
    "Latte":{
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
    "cost":2.50
    },
    "Cappuccino":{
        "ingredients": {
             "water": 250,
             "milk": 100,
             "coffee": 24
        },
    "cost":3.00
    }
}
report = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money_earned":0
}
while True:
    print("\nHey There!!, Welcome to 'Latte On The Rocks'\n")
    user=int(input("Admin : '1'\nCustomer : '2'\nExit : '3\n"))

    if user == 1:
        print(f"Water:{report['Water']}ml\nMilk:{report['Milk']}ml\nCoffee:{report['Coffee']}g\nMoney earned:${report['Money_earned']}")
    elif user == 2:
        order=input("Here is the menu:\n"
                        "1. 'Espresso' : $1.50\n"
                        "2. 'Latte' : $2.50\n"
                        "3. 'Cappuccino' : $3.00\n")
        available=Check_Availability(order)
        if available == 0:
            print(f"Your order {order} is Available Please pay the Bill and wait for the order")
            Cash = payment(order)
            report["Money_earned"] += Cash
            continue
        else:
            print(f"Sorry but Your Order: {order} is not available")
            continue
    else:
        break





