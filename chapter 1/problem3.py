import os

# Specify the directory path ('.' represents the current directory)
directory_path = '/'

try:
    # Get the list of all files and directories
    contents = os.listdir(directory_path)

    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' was not found.")
except PermissionError:
    print(f"Error: Permission denied to access '{directory_path}'.")
