# This program uses a loop to display a
# table showing the numbers 1 through 10
# and their squares.

# Print the table headings.
print('Number\tSquare')
print('--------------')

# Print the numbers 1 through 10
# and their squares.
for number in range(1, 11):
    square = number**2
    print (number, '\t', square)

'''
for number in [1,2,3,4,5,6,7,8,9,10]:
    square = number**2
    print (number, '\t', square)
'''
