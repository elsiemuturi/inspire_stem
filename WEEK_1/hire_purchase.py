#program to calculate hire purchase
# Date :21/02/2024
# Name: Elsie Muturi
cash_price = float(input("enter cash price: "))
deposit = float(input("enter deposit: "))
r = float(input("enter rate: "))
n = float(input("enter number of installments: "))
p = cash_price - deposit
hp = p * (( 1 + r ) ** n )
print("principal" ,p)
print("hire_purchase" ,hp)
