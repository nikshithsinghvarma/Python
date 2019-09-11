# This program gets an item's original price and
# calculates its sale price, with a 20% discount.
DISCOUNT = 0.2
# Get the item's original price.
original_price = float(input("Enter the item's original price: "))

# Calculate the amount of the discount.
discount = original_price * DISCOUNT

# Calculate the sale price.
sale_price = original_price - discount

# Display the sale price.
print('The sale price is', sale_price)
