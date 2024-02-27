#strings in python
#Date : 22/02/2024
#Name ; ELSIE MUTURI 

city = ("nairobi")

  #convert to uppercase

print(city)
print("\n")# \ prints a new line
print(city.upper())
#convert to lowercase
city = ("NAIROBI")
print(city)
print("\n")# \ prints a new line
print(city.lower())
#removing trailing white spaces
town = (" Kiambu ")
print(town)
print("\t")# \ prints as tab
print(town.strip())

#adding two strings also known as concurtination
f_name = ("Lydia ")
s_name = ("Supet ")

full_name = f_name + s_name
print(full_name)


city = ("NAIROBI")

print(city[0]) #N
print(city[-1])
print(city[-2])
print(city[3])
print(city[4])
print(city[5])
print(city[6])
# to reverse a string use a -(negative sign)
# words that can be reads the same backwords and forewords = palindrome

#replacing characters
fruit = ("Orange")
print(fruit.replace("O","Y"))

subject = ("Physical,Sciences")
print(subject.split(","))


age = 30
height = 165
print("I am {0} years old and {1} height" ,.format{age , height})






