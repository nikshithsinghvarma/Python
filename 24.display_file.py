# This program displays the contents
# of a file.

def main():
    try:
        # Get the name of a file.
        filename = input('Enter a filename: ')

        # Open the file.
        infile = open(filename, 'r')

        # Read the file's contents.
        contents = infile.read()

        # Display the file's contents.
        print(contents)

        # Close the file.
        infile.close()
    except IOError as err:
        print(err)

# Call the main function.
main()

