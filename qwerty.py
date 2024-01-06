def unique_numbers(numbers):
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers


numbers = [1, 2, 5, 2, 3, 1, 4, 5, 3, 4]
unique_numbers = unique_numbers(numbers)
print(unique_numbers)


