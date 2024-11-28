max = 777
min = 11

def cheese_order(order_amount):
    if order_amount.isdigit() == False:
        print("Stewart Bowman, enter your cheese order weight:", order_amount)
    elif int(order_amount) > max:
        print(order_amount, "is more than currently available stock.")
    elif int(order_amount) < min:
        print(order_amount, "is less than currently available stock.")
    elif (int(order_amount) <= max) and (int(order_amount) >= min):
        print((order_amount), "costs", "$", int(order_amount))
    else:
        print("Please enter a valid input.")
amount = input("Stewart Bowman, enter cheese order weight (numeric value): ")
function = cheese_order(amount)