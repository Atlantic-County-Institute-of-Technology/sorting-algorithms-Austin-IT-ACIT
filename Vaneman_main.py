# Austin Vaneman 10/14/25

import random

import os

from bubble_sort import bubblesort

from insertion_sort import insertion

from selection_sort import selection

from change_numbers import change

# start of the code / project
print(input(" [-] welcome to my sorting numbers project \n [-] Press enter to begin"))
os.system('cls' if os.name == 'nt' else 'clear')

# global variable declarations
temp_numbers = []
numbers = []


# main menu code
def main():

    # all variables for code
    selection_1 = 0
    selection_2 = 0
    shown = 0
    menu = 0
    min_numbers = 0
    max_numbers = 0
    amount_numbers = 0

    min_numbers, max_numbers, amount_numbers = change(min_numbers, max_numbers, amount_numbers)
    # min_numbers = int(input(" [-] what is the lowest number wanted to see?"))
    # max_numbers = int(input(" [-] what is the highest number wanted to see?"))
    # amount_numbers = int(input(" [-] what is the amount of number(s) wanted to see?"))
    numbers = [random.randint(min_numbers, max_numbers) for i in range(amount_numbers)]
    temp_numbers = str(numbers)

    # start of main menu code
    while True:

        os.system('cls' if os.name == 'nt' else 'clear')

        print(f" {temp_numbers} \n [-] 0. Exit \n [-] 1. renter numbers \n [-] 2. select sort \n")

        # ask for what number to enter from the main menu
        selection_1 = int(input(" [-] Please enter an number: "))

        # this is the exit code to terminate the terminal
        if selection_1 == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()

        # change numbers
        if selection_1 == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            change(min_numbers, max_numbers, amount_numbers)

        # go to the sorting menu
        if selection_1 == 2:
            sec_menu()


# second menu code / sorting menu
def sec_menu():

    # all variables for code
    selection_1 = 0
    selection_2 = 0
    shown = 0
    menu = 0

    # start of second menu code
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" [-] Select a sorting from this page \n [-] 0. Back to Menu \n [-] 1. Bubble Sorting \n"
          " [-] 2. Insertion Sorting \n [-] 3. Selection Sorting")
    selection_2 = int(input(" [-] Please enter an number: "))

    # goes back to the main menu
    if selection_2 == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        main()

    # asking if they want to see what the code does
    if selection_2 == 1 or 2 or 3:
        shown = int(input(" [-] do you want to see the process? (0 - No, 1 - Yes)"))

    # code for bubble sorting
    if selection_2 == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Unsorted List: {temp_numbers}")
        bubblesort(numbers, (False if shown == 0 else True))
        print(numbers)
        menu = int(input(" [-] Back to Main Menu (0) or Back to Sort Menu (1)"))

    # code for insertion sorting
    if selection_2 == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(temp_numbers)
        insertion(numbers, (False if shown == 0 else True))
        print(numbers)
        menu = int(input(" [-] Back to Main Menu (0) or Back to Sort Menu (1)"))

    # code for selection sorting
    if selection_2 == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(temp_numbers)
        selection(numbers, (False if shown == 0 else True))
        print(numbers)
        menu = int(input(" [-] Back to Main Menu (0) or Back to Sort Menu (1)"))

    # after each sort asked if wanting to go to main menu
    if menu == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        main()

    # after each sort asked if wanting to go to second menu / sorting menu
    if menu == 1:
        sec_menu()


if __name__ == '__main__':
    main()
