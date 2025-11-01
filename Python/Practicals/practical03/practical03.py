"""
Lists and Their Operations 
Create a shopping list application. 
● Add items to a list. 
● Remove an item if it is purchased (input from the user). 
● Sort the list alphabetically. 
● Print the list of items after each operation.
"""
shopping_list = ['note book', 'apple','soaps','pens']
print("shopping list: ", shopping_list)

inp = input("add item to shopping list: ")
shopping_list.append(inp)
print("Updated shopping list:", shopping_list)

remove = input("Remove item to shopping list: ")
shopping_list.remove(remove)
print("Item removed:", remove)
print(shopping_list)

shopping_list.sort()
print("Sorted shopping list:",shopping_list)


    

