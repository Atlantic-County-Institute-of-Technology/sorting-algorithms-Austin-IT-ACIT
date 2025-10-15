# Austin Vaneman 10/14/25
# import random
# values = [random.randint(1, 100) for i in range(10)]


def insertion(numbers):
    for i in range(1, len(numbers)):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and temp < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
            numbers[j + 1] = temp
    return numbers


# if __name__ == '__main__':
#     print(values)
#     numbers = insertion(values)
#     print(values)

# sorting action - insert
# traversal -
