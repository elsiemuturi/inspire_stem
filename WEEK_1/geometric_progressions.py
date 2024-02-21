# progam to show n terms in a geometric progression
a = int(input("The first term is:"))
r = int(input("The common ratio is:"))
n = int(input("The number of terms is:"))
for i in range(1 , n + 1):
    t_n = a * r **(i - 1)
    print(t_n)

#program for arithmetic progressions
a = int(input("The first term is:"))
d = int(input("The common difference is:"))
n = int(input("The number of terms is:"))
for i in range(1 , n + 1):
    t_n = a * d **(i - 1)
    print(t_n)
