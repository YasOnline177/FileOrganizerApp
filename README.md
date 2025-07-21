# File Organizer App 

This is a simple terminal-based File Organizer tool written in Python. It helps users automatically organize files in a selected folder by their file extension. Each file is moved into a subfolder based on its type (e.g., `.jpg` files will go into a folder named `jpg`).

---

## Features

- Organizes files in a directory by file extension
- Automatically creates folders for each file type
- Moves files into corresponding folders
- Handles files without extensions
- Ignores subfolders

---

## How to Use 

1. **Make sure Python 3 is installed** on your system.
2. **Download or clone this repository**.
3. Open a terminal or IDE and run the Python script.
4. **Enter the full path** of the folder you want to organize when prompted.
5. The program will organize all the files in that folder into subfolders by extension.

---

## Example

If the folder has:
    image.jpg
    document.pdf
    archive.zip
    note.txt

After running the script, the folder will look like this:
    jpg/
    image.jpg
    pdf/
    document.pdf
    zip/
    archive.zip
    txt/
    note.txt

---

## Note 

- Files without extensions will be moved into a folder named `no_extension`.
- Subfolders inside the target folder will be ignored.
- This tool does not delete or modify any file content. Only organizes them.

# Author

Created by a first-year Computer Science undergraduate as a part of a personal learning project to strengthen Python skills.