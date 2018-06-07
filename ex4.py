numbers = [12, 12515, -21412, 5, -10, 1234]

def f(numbers):
    for element in range(len(numbers)):
        if numbers[element] < 0:
            numbers[element] = "More then zero"
        elif 0 < numbers[element] < 100:
            numbers[element] = "Less then hundred"
        elif numbers[element] > 100:
            numbers[element] = "More then hundred"
    return numbers

print(f(numbers))
