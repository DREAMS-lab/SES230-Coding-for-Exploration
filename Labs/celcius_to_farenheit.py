a = 5
def convert_celcius_to_farenheit(c_int):
    b = 10
    FARENHEIT_CONST = 32
    farenheit_val = 1.8*c_int + FARENHEIT_CONST
    return farenheit_val

print(a)
print(b)
print(FARENHEIT_CONST)
print(convert_celcius_to_farenheit(100))
print(convert_celcius_to_farenheit(50))
print(convert_celcius_to_farenheit(0))



