def get_names():

    list_of_input = []
    print("Welcome Stewart Bowman list any 5 of the first 20 elements in the Period table")
    cnt = 1
    while True:
        if cnt <= 5:
            element = input("Enter the name of an element: ").strip().lower()
        else:
            break

        if element == '':
            print("Empty enter is not allowed. You should enter 5 elements.")
        elif element not in list_of_input:
            list_of_input.append(element)
            cnt += 1
        else:
            print(element, "was already entered. No duplicates allowed.")
            
        '''
        if element:
            if element not in list_of_input:
                list_of_input.append(element)
                cnt += 1
            else:
                print(element, "was already entered. No duplicates allowed.")
        else:
            print("Empty enter is not allowed. You should enter 5 elements.")
        '''
    
    return list_of_input

#!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt
file_of_elements = open('elements1_20.txt', 'r')
elements = []

while file_of_elements:
    line = file_of_elements.readline()
    if line == '':
        break
    else:
        elements.append(line.strip().lower())
        
'''
for line in file_of_elements:
    elements.append(line.strip().lower())
'''

list_of_input = get_names()

responses_correct = []
responses_incorrect = []
for response in list_of_input:
    if response in elements:
        responses_correct.append(response)
    else:
        responses_incorrect.append(response)

print()
print(str(len(responses_correct)*20), "% correct")
print("Found: ", end='')
for element_id in range(len(responses_correct)):
    print(responses_correct[element_id].title(), end=' ')
print("\nNot Found: ", end='')
for element_id in range(len(responses_incorrect)):
    print(responses_incorrect[element_id].title(), end=' ')
print()

'''
print()
print(str(len(responses_correct)*20), "% correct")
print("Found: ", end='')
for element in responses_correct:
    print(element.title(), end=' ')
print("\nNot Found: ", end='')
for element in responses_incorrect:
    print(element.title(), end=' ')
print()
'''

file_of_elements.close()