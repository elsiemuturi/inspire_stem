# progam to show n terms in a geometric progression
#20/02/2024
a = int(input("The first term is:"))
r = int(input("The common ratio is:"))
n = int(input("The number of terms is:"))
n_t = (a * r ** (n-1))
print("The number of terms" ,n_t)

#program for arithmetic progressions
a = int(input("The first term is:"))
d = int(input("The common difference is:"))
n = int(input("The number of terms is:"))
n_t = (a + (n - 1) * d)
print("The number of terms" ,n_t)