#29/02/2024
#function>>block of code running as a unit
#built in functions eg print
#user defined functions

#initializing a functon>>aka defining=def
def print_name():#function that lacks parameters
    print("My name is Elsie Muturi ")
#calling the function
print_name()
print_name()

def print_details(name,age,id,gender):#function with parameters
    print("I am {0},{1} years old. My id no is {2}. I am a {3}." .format(name,age,id,gender))

print_details("Elsie","18","12345678","female")
print_details("Jamie","27","87654321","male")

#how to return from a function
def sum_nums(x,y):
    return x + y
z = sum_nums(10,20)
print(z)

def prod_nums(x,y):
    return x * y
z = prod_nums(10,20)
print(z)

print(prod_nums(3,12))

#using for loop inside a function
def print_odds(first_number,last_number):
    for i in range(first_number,last_number,2):
        print(i)
print_odds(1,20)

def print_odds(first_number,last_number):
    for i in range(first_number,last_number):
        print(i %2)
print_odds(1,20)



