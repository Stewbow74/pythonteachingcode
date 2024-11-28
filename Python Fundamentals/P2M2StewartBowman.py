# [] create list-o-matic as a function and call it

def list_o_matic():
    name = ["Taylor","Zhaylen","Demetri","Shakur","Janet"]
# [] be sure to include your spelled-out name in the welcome prompt

    name_to_add= input("Welcome Stewart Bowman. Enter a name of your friends and family: ")

    if name_to_add.lower() not in name:
        name.append(name_to_add)
        print("Individual updated.")
    else:
        print("Invalid Input.")

    print(name)

list_o_matic()

        
# [] you are welcome to use any list you like for list-o-matic, does not have to be animals 
