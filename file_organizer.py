import os
import shutil

# Function to organize files by extension
def organize_files_by_extension(folder_path):
    # Check if the provided path is valid
    if not (os.path.isdir(folder_path)):
        print("**The provided path is not valid**")
        return
    
    # List all files and folders in the given directory
    items = os.listdir(folder_path)

    for item in items:
        item_path = os.path.join(folder_path, item)

        # Skip if it's a folder
        if (os.path.isdir(item_path)):
            continue

        # Get the file extension 
        _, extension = os.path.splitext(item)
        extension = extension[1:]   # Remove the dot from extension

        if (extension == ""):
            extension = "no_extension"

        # Create a folder for the extension if it doesn't exist
        target_folder = os.path.join(folder_path, extension)
        if not (os.path.exists(target_folder)):
            os.makedirs(target_folder)

        # Move the file to the corresponding folder
        shutil.move(item_path, os.path.join(target_folder, item))

    print("**Files organized successfully**")

# Main program
print("**Welcome to the File Organizer**")

# Ask the user to input the folder path
folder_to_organize = input("Enter the full path of the folder you want to organize: ")

# Call the function
organize_files_by_extension(folder_to_organize)