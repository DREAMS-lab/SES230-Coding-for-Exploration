def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
    return result

N = int(input("Please enter N for which you want the factorial: "))
print(factorial(N))
# print(factorial(6))


