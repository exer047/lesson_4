numbers = [12, 12515, -21412, -5, 10, -1234]

def f(numbers):
    for element in range(len(numbers)):
        if element == len(numbers) - 1:
            break
        elif numbers[element] < 0 and numbers[element + 1] < 0:
            numbers[element] = numbers[element + 2]
        elif numbers[element] < 0:
            numbers[element] = numbers[element + 1]
    return numbers

print(f(numbers))
