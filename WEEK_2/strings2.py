#len gives the number of characters including the spaces
name = "Elsie Muturi"
print(len(name))
print(f"My full name is {name}")#f and { } prints a string


#printin a string %s
activity = "dancing"
print("My hobby is %s" %(activity))
#printing a floating point %5.numberf
height = 1.2346578393
print("My height is %5.4f" %(height))
#printing an integer %d
age = 34
print("My age is %d"% (age))
#printing a character %c


school = " Engineering"
course = " Electrical"
print("I am studying{0} in the school of{1}" .format(course,school))
print("I am studying{course} in the school of{school}}" .format(course = Medicine,school = Humanity))
