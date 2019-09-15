# Nikshith Singh Varma
# 1001667758
#
# To print days of week according to input

day = int(input("Enter a number"))
dayOne = "Monday"
dayTwo = "Tuesday"
dayThree = "Wednesday"
dayFour = "Thursday"
dayFive = "Friday"
daySix = "Saturday"
daySeven = "Sunday"
if day == 1:
    print(dayOne)
elif day == 2:
    print(dayTwo)
elif day == 3:
    print(dayThree)
elif day == 4:
    print(dayFour)
elif day == 5:
    print(dayFive)
elif day == 6:
    print(daySix)
elif day == 7:
    print(daySeven)
else:
    print("Enter Valid Input Between 1 to 7")
