#to find sum of first 20 numbers using the for loop
#Date : 26/02/2024
#
sum_numbers = 0
max_value = int(input("Enter maximum value: "))
for x in range(0,max_value + 1):
    sum_numbers = sum_numbers + x
    print(sum_numbers)

