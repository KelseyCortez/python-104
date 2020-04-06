# prompt user for a single grocery item
# append it to the 'groceries' list
#in an infinite while loop, prompt the user for an item. append item to list
# print list after adding items

#to fill grocery list prompt until they enter an empty string
#print list
#give them a chance to replace items in list

groceries1 = []
while True:
    item = input('What item would you like to add to the list? ')
    if item == '':
        break
    else:
        groceries1.append(item)
        print(groceries1)

groceries2 = []
while True:
    item = input('What item would you like to add to this second list? ')
    if item == '':
        break
    else:
        groceries2.append(item)
        print(groceries2)

groceries3 = groceries1 + groceries2
print(groceries3)
indexes = range(len(groceries3))
for i in indexes:
    print(f'{i}: {groceries3[i]}')

while True:
    for i in indexes:
        item = groceries3[i]
    replace_item = input('What index would you like to replace? ')
    if replace_item == '':
        print(groceries3)
        break
    else:
        replace_item = int(replace_item)
        new_item = input('What item would you like instead? ')
        groceries3[replace_item] = new_item
        print(groceries3)

