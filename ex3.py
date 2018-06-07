numbers = [1, 2, 3, 5, 9]
def avr_number(number):
    number_summ = 0
    for element in number:
        number_summ += element
    return number_summ / len(number)

def avr_number_2(numbers):
    return sum(numbers) / len(numbers)

print(avr_number(numbers))