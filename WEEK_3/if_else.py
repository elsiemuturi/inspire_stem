age = 17

if age > 18:
    print("You are allowed to drink")
if age < 18:
    print("You are not allowed to drink")

salary = 45000
if salary > 30000 and salary < 50000:
    salary = salary * 0.1 + salary
    print(salary)

home_county = "Embu"
if home_county == "Embu" or home_county =="Kisumu":
    print("You get a bursary.")

grade = int(input("enter grade: "))
print("enter grade: " ,grade)
if grade >= 84 and grade <=90 :
    print("You get cash")
elif grade >=50 and grade <=83 :
    print("You win a math set")
else grade <50 :
    print("Repeat math set")
