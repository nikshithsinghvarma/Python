# Nikshith Singh Varma
# 1001667758
#
# To print discount and total amount according to quantity
quantity = int(input("Enter the Quantity of Product"))
totalPrice = float(quantity*99)
discount = 0.0
if quantity <= 0:
    print("Enter a valid Quantity")
else:
    print("Total Price Before Discount is :", totalPrice)
    if quantity >= 10 and quantity <= 19:
        print("10% Discount Received")
        discount = 0.1
    elif quantity >= 20 and quantity <= 49:
        print("20% Discount Received")
        discount = 0.2
    elif quantity >= 50 and quantity <= 99:
        print("30% Discount Received")
        discount = 0.3
    elif quantity >= 100:
        print("40% Discount Received")
        discount = 0.4
    else:
        print("No Discount Received.To receive Discount Quantity must be greater than 10 ")
    totalPriceAfterDiscount=totalPrice-totalPrice*discount
    print("Total Price After Discount is :",totalPriceAfterDiscount)

