# Nikshith Singh Varma
# 1001667758
#
# To print the factorial of number
n=int(input("Enter a Non-Negative number"))
if n > 0:
    fact=1
    for i in range(1, n+1):
        fact = fact*i
    print(" ", n, "! = ", fact)
elif n == 0:
    fact = 0
    print(" ", n, "! = ", fact)
else:
    print("Enter a valid input")
