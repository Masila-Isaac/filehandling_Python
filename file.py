try:
    # Open the file in write mode to create it and write initial content
    with open('my_file.txt', 'w') as file:
        file.write("Hello,my nam e is Isaac Masila!\n")
        file.write(" Am aged 18 years \n")
        file.write(" And am in my quest of python learning!\n")
    print("created and written successfully.")
except PermissionError:
    print("Error: Permission denied when writing to file.")
except Exception as e:
    print(f"An error occurred: {e}")

# File reading and displaying contents
try:
    # Open the file in read to display the content
    with open('my_file.txt', 'r') as file:
        print("\nContents of 'my_file.txt' after writing:")
        print(file.read())
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: Permission denied when reading the file.")
except Exception as e:
    print(f"An error occurred: {e}")

# File appending
try:
    # Open the file in append mode to add more lines
    with open('my_file.txt', 'a') as file:
        file.write("add more notes about isaac.\n")
        file.write("0795195136 is my number\n")
        file.write("Appending is easy!\n")
    print("\nContent appended successfully.")
except PermissionError:
    print("Error: Permission denied when appending to the file.")
except Exception as e:
    print(f"An error occurred: {e}")

# Final file reading to show updated content
try:
    # Open the file again in read mode to display the updated content
    with open('my_file.txt', 'r') as file:
        print("\nContents of 'my_file.txt' after appending:")
        print(file.read())
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: Permission denied when reading the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("\nFile handling operations completed.")
