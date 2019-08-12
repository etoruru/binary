def binary(number):
    if not number:
        return '0'
    binary_number = ''
    while number:
        bit = number % 2
        binary_number = str(bit) + binary_number
        number = number // 2
    return binary_number



