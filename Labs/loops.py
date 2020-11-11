# friends = ['Frodo', 'Gandalf', 'Legolas', 'Pippin', 'Sauron']
#
#
# for friend in friends:
#     print(friend)

# for i in [5,4,3,2,1]:
#     print(i)


#
# 35! /( 2!*33!)
#
# 17*35



def compute_sums(list_of_numbers):
    for number in list_of_numbers:
        sum = 0
        for i in range(1,number+1):
            sum = sum + i
        print(number, sum)

compute_sums([2,3,7,4,5])

