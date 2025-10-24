# Austin Vaneman 10/16/25

def selection(numbers, shown):
    for i in range(len(numbers)):
        temp = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[temp]:
                temp = j
            if shown:
                print(numbers)
        numbers[i], numbers[temp] = numbers[temp], numbers[i]
    return numbers
# sorting action - select
