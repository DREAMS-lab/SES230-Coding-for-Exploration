def decimal2binary(decimal_value):
    binary_str = ""
    remainder = 0
    MAX_POWER = 7
    for k in range(MAX_POWER, -1, -1):
        power_val = 2 ** k
        remainder = decimal_value % power_val
        divisor = decimal_value // power_val
        if (remainder != 0 and divisor != 0) or (remainder == 0 and divisor == 1):
            binary_str = binary_str + "1"
            decimal_value = remainder
        else:
            binary_str = binary_str + "0"
    return binary_str

def binary2decimal(binary_str):
    decimal_value = 0
    binary_len = len(binary_str)
    for k in range(binary_len - 1, -1, -1):
        binary_digit = int(binary_str[k])
        power = binary_len - 1 - k
        decimal_value = decimal_value + binary_digit * (2 ** power)
    return decimal_value

# for number in range(0, 100):
#     binary = decimal2binary(number)
#     print(number, binary, binary2decimal(binary))


# binary card game a.k.a Mind Reader
def binary_card_game():
    print("Think of a number between 1-100")
    decimal_guess = 0
    ctr = 0
    for k in range(0, 7):
        for number in range(0, 101):
            binary_str = decimal2binary(number)
            bit_position = int(binary_str[7 - k])
            if bit_position == 1:
                print(number, end=', ')
                ctr = ctr + 1
                if ctr % 10 == 0:
                    print('')
        existence = input("\nIs the number in this set? y/n:")
        if existence is 'y':
            decimal_guess = decimal_guess + 2 ** k
            print(decimal_guess)
    return decimal_guess



guess = binary_card_game()
print("The number in your mind is ", guess, "!")


