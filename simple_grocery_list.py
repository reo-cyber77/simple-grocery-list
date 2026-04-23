def add_item(grocery_list, item_name):
    grocery_list.append(item_name)
    print('Item added!')
    

def view_items(grocery_list):
    print('\nYour Grocery List:')
    if not grocery_list:
        print('The list is empty.')
    else:
        for i in range(len(grocery_list)):
            print(f'{i+1}. {grocery_list[i]}')

def remove_item(grocery_list, index):
    try:
        removed = grocery_list.pop(index - 1)
        print(f'Item removed!')
    except Exception:
        print('Invalid Item Number')












grocery = []
print('--- GROCERY LIST ---')
print('\n1. Add Item',
      '\n2. View Items',
      '\n3. Remove Item',
      '\n4. Exit')
while True:
    choice = input('\nEnter choice: ')
    if choice == '1':
        item = input('Enter item: ')
        add_item(grocery, item)
    elif choice == '2':
        view_items(grocery)

    elif choice == '3':
        if not grocery:
            print('Nothing to remove!')
        else:
            try:
                remove = int(input('Enter item number to remove: '))
                remove_item(grocery, remove)
            except ValueError:
                print('Please enter valid number.')
    elif choice == '4':
        print('Goodbye')
        break
    else:
        print('Please enter 1-4 only')
    