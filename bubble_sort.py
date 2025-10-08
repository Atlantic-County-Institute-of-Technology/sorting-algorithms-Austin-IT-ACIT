# import random
#
# numbers = [random.randint(1, 100) for i in range(10)]
#
# outer_pass = 0
# inner_pass = 0

# print(numbers)
def bubblesort(numbers):
    for i in range(len(numbers)):
        # outer_pass += 1
        for j in range(0, len(numbers) - i - 1):
            # inner_pass += 1
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers
#
# print(numbers)
# print(f"There was {outer_pass} outer passes || {inner_pass} inner passes")