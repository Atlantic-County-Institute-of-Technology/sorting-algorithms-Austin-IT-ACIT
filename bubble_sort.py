# Austin Vaneman 10/14/25

# sorting action - swap
# traversal - loop


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