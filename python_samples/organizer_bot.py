import os
import shutil

# 🚀 Automation Script: File Organizer
# Author: Saeed Ali
# Description: This script scans a folder and organizes files into subfolders based on their extensions.

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"❌ The directory {directory} does not exist.")
        return

    # List of all files in the directory
    files = os.listdir(directory)

    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]  # Remove the dot (e.g., .pdf -> pdf)

        if os.path.exists(os.path.join(directory, file)) and extension:
            # Create a folder for the extension if it doesn't exist
            target_folder = os.path.join(directory, extension.upper() + "_Files")
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            # Move the file
            shutil.move(os.path.join(directory, file), os.path.join(target_folder, file))
            print(f"✅ Moved: {file} -> {target_folder}")

if __name__ == "__main__":
    # Example Usage:
    # Change 'target_dir' to the folder you want to clean up
    target_dir = "./Downloads_Test" 
    print("🤖 Starting Cleanup Bot...")
    organize_files(target_dir)
    print("🎉 Cleanup Complete!")