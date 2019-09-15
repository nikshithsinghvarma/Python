# Nikshith Singh Varma
# 1001667758
#
# To print Stage of life according to age given as input

age = float(input("Enter Age"))
if age > 0 and age <= 1:
    print("The Person is Infant")
elif age > 1 and age < 13:
    print("The Person is Child")
elif age >= 13 and age < 20:
    print("The Person is Teenager")
elif age >= 20:
    print("The Person is Adult")
else:
    print("Enter a valid Input for Age")
