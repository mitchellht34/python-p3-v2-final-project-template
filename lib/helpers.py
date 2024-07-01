# lib/helpers.py
from models.recipient import Recipient
from models.gift import Gift
# import ipdb

def show_recipients():
    print("------------------------------")
    recipients = Recipient.get_all()
    for i, recipient in enumerate(recipients, start=1):
        print(f"{i}. {recipient.name}")
    print("------------------------------")
    return recipients


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
    for gift in recipient.gifts():
        gift.delete()
    recipient.delete()
    print(f"{recipient.name} deleted")


def delete_gift(gift):
    gift.delete()
    print(f"{gift.name} deleted")


def exit_program():
    print("Goodbye!")
    exit()
