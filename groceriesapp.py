groceries = []

main_menu = '''

1. Print List
2. Add Items
3. Edit Items
4. Remove Items
5. Quit

'''


while True:
    menu_choice = int(input(main_menu))
    if menu_choice == 1:
        indexes = range(len(groceries))
        for i in indexes:
            print(f'{i}: {groceries[i]}')
    elif menu_choice == 2:
            while True:
                item = input('What item would you like to add to the list? ')
            if item == '':
                break
            groceries.append(item)
            print(groceries)

    elif menu_choice == 3:
        indexes = range(len(groceries))
        for i in indexes:
            print(f'{i}: {groceries[i]}')
                for i in indexes:
                    item = groceries[i]
                    replace_item = input('What index would you like to replace? ')
                        if replace_item == '':
                            break
                                print(groceries)
        else:
            replace_item = int(replace_item)
            new_item = input('What item would you like instead? ')
            groceries[replace_item] = new_item
            print(groceries)

    # Add if/else statements for each menu item

    # For each of these, add in code to handle adding/editing/removing items

    if menu_choice == 5:
        break

print('Thank you for using the grocery list app!')