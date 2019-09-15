# This program demonstrates an argument being
# passed to a function.


def main():
    value = 5
    show_double(value) # function call
    
# The show_double function accepts an argument
# and displays double its value.
def show_double(value):
    result = value * 2
    print(result)

# Call the main function.
main()
