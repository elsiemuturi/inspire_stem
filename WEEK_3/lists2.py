friends = ["Sharon" , "Halona" ,"Blessed" , "Laura" , "Vero"]
for friend in friends:
    print(friend)
    
#how to copy one list into another
enemies = friends[:]
print(enemies)

fruits = ["strawberry","kiwi","banana","mango","apple","guava"]
#to slice>> get part of list
print(fruits[0:3])
del fruits[0]
print(fruits)


squares = []#initializes an empty list
for x in range(0,11):
    squares.append(x**2)
    print(squares)

    