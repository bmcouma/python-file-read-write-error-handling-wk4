# Reading content from one file and writing to another
try:
    with open('input.txt', 'r') as file:
        content = file.read()
        modified_content = content.upper()  # Modify content (e.g., make it uppercase)

    with open('output.txt', 'w') as new_file:
        new_file.write(modified_content)

    print("File written successfully!")

except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
