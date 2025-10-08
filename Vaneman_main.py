# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
from bubble_sort import bubblesort

numbers = [random.randint(1, 100) for i in range(10)]

outer_pass = 0
inner_pass = 0

if __name__ == '__main__':
    print(numbers)
    bubblesort(numbers)
    print()
