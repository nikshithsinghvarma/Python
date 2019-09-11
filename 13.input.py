# Get the user's name, age, and income.
name = input('What is your name? ')
age = eval(input('What is your age? '))
income = float(input('What is your income? '))

# Display the data.
print('Here is the data you entered:')
print('Name:', name)
print('Age:', age)
print('Income:${:8.2f}'.format( income))

