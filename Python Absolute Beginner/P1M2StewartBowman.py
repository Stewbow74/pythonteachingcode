def fish_store(name,price):
    return "Report for Stewart Bowman. Fish type: "+name+" costs $"+price
fish = input("Enter fish name:")
price = input("Enter price:")
print(fish_store(fish,price))