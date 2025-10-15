# Austin Vaneman 10/14/25

import random
from bubble_sort import bubblesort
from insertion_sort import insertion

numbers = [random.randint(1, 100) for i in range(10)]


def main():
    temp_numbers = numbers[:]
    while True:

        print(numbers)
        print(temp_numbers)

        # print("this is bubble sort")
        # print(temp_numbers)
        bubblesort(numbers)
        print(temp_numbers)
        # print(numbers)
        # print("this is insertion sort")
        # print(temp_numbers)
        # insertion(numbers)
        # print(numbers)
        temp_something = int(input("something"))


outer_pass = 0
inner_pass = 0

if __name__ == '__main__':
    main()
