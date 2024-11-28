def adding_report(report = 'T'):
    total = 0
    items = ''
    while True:
        item = input("Enter an integer or \"Q\": ")
        if item.isdigit():
            total += int(item)
            if report == 'A':
                items += item + '\n'
        else:
            if item.lower().startswith('q'):
                if report == 'A':
                    print("\nItems\n" + str(items))
                    print("Total\n" + str(total) + "\n")
                    break
                elif report == 'T':
                    print("\nTotal\n" + str(total) + "\n")
                    break
            else:
                print(item, "is invalid input")

adding_report()
adding_report('A')