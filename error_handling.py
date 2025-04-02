# Asking user for a filename and handling errors
filename = input("Please enter the filename: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File content successfully read!")
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except PermissionError:
    print(f"Error: You do not have permission to read '{filename}'.")
except Exception as e:
    print(f"An error occurred: {e}")
