searchable_numbers = [1, 3, 5, 7, 9, 12, 14, 21, 34, 45, 60]
target_number = 60
counter = 1
for number in searchable_numbers:
    if number == target_number:
        print(counter)
        break
    counter = counter + 1

print(counter)

