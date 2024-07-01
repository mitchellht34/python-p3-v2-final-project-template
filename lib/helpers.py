# lib/helpers.py
from models.recipient import Recipient
from models.gift import Gift
# import ipdb

def top_menu():
    x = True
    while x:
        show_recipients()
        print("Please select the number of the recipient to see their gifts")
        print("OR")
        print("Type 'a' to add a new recipient")
        print("Type 'b' to go back")
        print("------------------------------")
        choice = input("> ")
        try:
            choice = int(choice)
        except Exception as exc:
            pass
        if choice == 'a':
            create_recipient()
        elif choice == 'b':
            x = False
        elif isinstance(choice, int) and choice <= len(Recipient.get_all()):
            recipient = Recipient.find_by_id(int(choice))
            recipient_menu(recipient)
        else:
            print('Invalid choice')
            # ipdb.set_trace()

def show_recipients():
    print("------------------------------")
    recipients = Recipient.get_all()
    for i, recipient in enumerate(recipients, start=1):
        print(f"{i}. {recipient.name}")
    print("------------------------------")


def show_gifts(recipient):
    gifts = recipient.gifts()
    for i, gift in enumerate(gifts, start=1):
        print(f"{i}. {gift.name}")
    return gifts


def create_recipient():
    name = input("Enter the new recipient's name: ")
    try:
        recipient = Recipient.create(name)
        print(f'{name} has been added')
    except Exception as exc:
        print("Error creating recipient", exc)


def create_gift(recipient_id):
    name = input("Enter the new gift's name: ")
    cost = input("Enter the new gift's cost: ")
    try:
        gift = Gift.create(name, cost, recipient_id)
        print(f'{name} added')
    except Exception as exc:
        print("Error creating gift", exc)


def delete_recipient(recipient):
    # delete gifts first
    recipient.delete()
    print(f"{recipient.name} deleted")


def delete_gift(gift):
    gift.delete()
    print(f"{gift.name} deleted")


def recipient_menu(recipient):
    x = True
    while x:
        print("------------------------------")
        print(f"{recipient.name}'s Gifts: \n")
        gifts = show_gifts(recipient)
        print(f'\nTotal: ${"%.2f" % sum([gift.price for gift in gifts])}')
        print("\nPlease select the number of the recipient to see their gifts")
        print("OR")
        print("Type 'a' to add a new gift")
        print("Type 'b' to go back")
        print("Type 'd' to delete recipient")
        print("------------------------------")
        choice = input("> ")
        try:
            choice = int(choice)
        except Exception as exc:
            pass
        if choice == 'a':
            create_gift(recipient.id)
        elif choice == 'b':
            top_menu()
        elif choice == 'd':
            delete_recipient(recipient)
            x = False
        elif isinstance(choice, int) and choice <= len(recipient.gifts()):
            gift_menu(choice, recipient)
        else:
            print('Invalid choice')

def gift_menu(index, recipient):
    x = True
    while x:
        gift = recipient.gifts()[index-1]
        print(f"Here are the details on {recipient.name}'s selected gift: \n")
        print(f"Name: {gift.name}")
        print(f'Price: ${"%.2f" % gift.price}')
        print("\nPlease select the number of the recipient to see their gifts")
        print("OR")
        print("Type 'b' to go back")
        print("Type 'd' to delete gift")
        print("------------------------------")  
        choice = input("> ")
        if choice == 'b':
            x = False
        elif choice == 'd':
            delete_gift(gift)
            x = False



def exit_program():
    print("Goodbye!")
    exit()
