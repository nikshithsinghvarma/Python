# This program demonstrates a simple for loop
# that uses a list of numbers.

print('I will display the numbers 1 through 5.')
'''for num in [1, 2, 3, 4, 5]:
    print(num)

for n in ['1', '2', '3', '4', '5']:
    print(n)

for num in [1.0, 2.0, 3.0, 4.0, 5.3]:
    print(num)
for num in [1, 'two', 3, 4, 5]:
    print(num)

'''
for num in (1, 2, 3, 4, 5):
    if num==3:
        continue
    print(num)

x = 0
while x<10:    
    x=x+1
    if x==5:
        break
    print(x)

