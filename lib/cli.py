# lib/cli.py
from models.recipient import Recipient
from models.gift import Gift
import ipdb
from helpers import (
    exit_program,
    show_recipients,
    create_recipient,
    show_gifts,
    create_gift,
    delete_recipient,
    delete_gift
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            top_menu()
        else:
            print("Invalid choice")

def top_menu():
    while True:
        recipients = show_recipients()
        print("Please select the number of the recipient to see their gifts")
        print("OR")
        print("Type 'a' to add a new recipient")
        print("Type 'b' to go back")
        print("Type 'e' to exit the program")
        print("------------------------------")
        choice = input("> ")
        ipdb.set_trace()
        try:
            choice = int(choice)
        except Exception as exc:
            pass
        if choice == 'a':
            create_recipient()
        elif choice == 'b':
            main()
        elif choice == "e":
            exit_program()
        elif isinstance(choice, int) and choice <= len(Recipient.get_all()):
            recipient_id = Recipient.get_all()[choice-1].id
            recipient = Recipient.find_by_id(recipient_id)
            recipient_menu(recipient)
        else:
            print('Invalid choice')
            # ipdb.set_trace()

def recipient_menu(recipient):
    while True:
        print("------------------------------")
        print(f"{recipient.name}'s Gifts: \n")
        gifts = show_gifts(recipient)
        print(f'\nTotal: ${"%.2f" % sum([gift.price for gift in gifts])}')
        print("\nPlease select the number of the recipient to see their gifts")
        print("OR")
        print("Type 'a' to add a new gift")
        print("Type 'b' to go back")
        print("Type 'd' to delete recipient")
        print("Type 'e' to exit the program")
        print("------------------------------")
        choice = input("> ")
        # ipdb.set_trace()
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
            top_menu()
        elif choice == "e":
            exit_program()
        elif isinstance(choice, int) and choice <= len(recipient.gifts()):
            ipdb.set_trace()
            gift_menu(choice, recipient)
        else:
            print('Invalid choice')

def gift_menu(index, recipient):
    while True:
        gift = recipient.gifts()[index-1]
        print(f"Here are the details on {recipient.name}'s selected gift: \n")
        print(f"Name: {gift.name}")
        print(f'Price: ${"%.2f" % gift.price}')
        print("\nPlease select the number of the recipient to see their gifts")
        print("OR")
        print("Type 'b' to go back")
        print("Type 'd' to delete gift")
        print("Type 'e' to exit the program")
        print("------------------------------")  
        choice = input("> ")
        if choice == 'b':
            recipient_menu(recipient)
        elif choice == 'd':
            delete_gift(gift)
            recipient_menu(recipient)
        elif choice == "e":
            exit_program()
        else:
            print('Invalid choice')



def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. See a list of recipients")


if __name__ == "__main__":
    main()
