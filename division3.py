# This program divides a number by another number.

def main():
    # Get two numbers.
    try:
        
        num1 = int(input('Enter a number: '))
        num2 = int(input('Enter another number: '))

        # Divide num1 by num2 and display the result.
        result = num1 / num2
        print(num1, 'divided by', num2, 'is', result)
    except ZeroDivisionError as e:
        print('error', e)
            

# Call the main function.
main()
