def read_and_write_file():
    try:
        # Ask for the input file name
        input_file = input("Enter the name of the file to read: ")

        # Try to open the file
        with open(input_file, "r") as file:
            content = file.read()

        # Convert content to uppercase
        modified_content = content.upper()

        # Ask for the output file name
        output_file = input("Enter the name of the new file to save: ")

        # Write modified content to new file
        with open(output_file, "w") as new_file:
            new_file.write(modified_content)

        print(f"File '{input_file}' has been successfully read and modified content saved to '{output_file}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the function
read_and_write_file()
