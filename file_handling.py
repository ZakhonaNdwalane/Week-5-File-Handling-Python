
# File Creation
def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hello, this is the first line.\n")
            file.write("This is the second line with number: 42\n")
            file.write("And this is the third line with a float: 3.14\n")
        print("File created and written successfully!")
    except Exception as e:
        print(f"Error while creating or writing to the file: {e}")

#File Reading and Display
def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
        print("File contents:")
        print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print(f"Error while reading the file: {e}")

#File Appending
def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("This is an appended line.\n")
            file.write("Here is another appended line with number: 100\n")
            file.write("And one more with a special character: @\n")
        print("Text appended to the file successfully!")
    except Exception as e:
        print(f"Error while appending to the file: {e}")

#Error Handling with try, except, and finally
def safe_file_operations():
    try:
        create_file()
        append_to_file()
        read_file()
    except FileNotFoundError:
        print("File not found error occurred.")
    except PermissionError:
        print("Permission error occurred.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File operations completed.")

# Running the operations
if __name__ == "__main__":
    safe_file_operations()
