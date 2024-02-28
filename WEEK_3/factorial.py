#factorials using the for loop
#Date:26/02/2024
#Name :Elsie Muturi
factorial_numbers = 1
max_value = int(input("Enter maximum value: "))
for x in range(1,max_value + 1):
    factorial_numbers = factorial_numbers * x
    print(factorial_numbers)


#even numero
for i in range(0,20,2):#,2 skips values in steps of two
    print(i)
#odd numero
for i in range(1,20,2):#,2 skips values in steps of two
    print(i)

