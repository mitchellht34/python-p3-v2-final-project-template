# lib/cli.py

from helpers import (
    exit_program,
    show_recipients,
    recipient_menu,
    top_menu
    # sub_menu
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


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. See a list of recipients")


if __name__ == "__main__":
    main()
