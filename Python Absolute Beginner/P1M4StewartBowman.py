def str_analysis(input_string):
    if input_string.isdigit():
        input_string = int(input_string)

        if input_string > 99:
            return str(input_string) + " is a big number."
        else:
            return str(input_string) + " is a small number."
    else:
        if input_string.isalpha():
            return input_string + " uses only alphabetic characters."
        else:
            return input_string + " uses multiple character types."

print("Welcome to StringTester.\n-------------------------")

while True:
    user_input = input("Input string for testing: ")
    if user_input == "":
        print("No input detected.")
    else:
        print(str_analysis(user_input))
        break