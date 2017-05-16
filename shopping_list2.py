# permet d'importer des outils liés à l'OS. Utile pour vider l'écran par exemple. Voir fonction "clear_screen()"
import os
# make a list to hold into our items
shopping_list = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# have a help command
def show_help():
    clear_screen()
    # print out instructions on how to use the app
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help^.
Enter 'SHOW' to see your current list.
Enter 'REMOVE' to delete an item from your list.
""")

show_help()

def add_to_list(item):
    show_list()
    if len(shopping_list):
        position = input("Where should I add {}?\n"
                         "Press ENTER to add to the end of the list\n"
                         "> ".format(item))
    else:
        position = 0

    try:
        #abs() donne la valeur absolue d'un nombre (un négatif devient positif)
        position = abs(int(position))
    except ValueError:
        position  = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        # add new items to our list
        shopping_list.append(new_item)

    show_list()


#have a SHOW command
def show_list():
    clear_screen()

    print("Here's your list:")

    index = 1
    for item in shopping_list:
        print("{}, {}".format(index, item))
        index +=1

    print("-"*10)

def remove_from_list():
    show_list()
    what_to_remove = input("What would you like to remove?\n> ")
    try:
        shopping_list.remove(what_to_remove)
    except ValueError:
        pass
    show_list()


while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item.upper() == "DONE" or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == "SHOW":
        show_list()
        continue
    elif new_item.upper() == "HELP":
        show_help()
        continue
    elif new_item.upper() == 'REMOVE':
        remove_from_list()
    else:
        add_to_list(new_item)

# print out the list
show_list()
