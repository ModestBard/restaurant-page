# 1. The script imports necessary modules: `os`, `Path` from `pathlib`, and `logging`.

# 2. A `setup_logging()` function is defined to configure basic logging settings.

# 3. The main functionality is in the `rename_jpg_files()` function:
#    - It uses the current working directory to find JPG files.
#    - It searches for files with extensions .jpg, .JPG, .jpeg, and .JPEG.
#    - Duplicate files are removed from the list.
#    - If no JPG files are found, it displays a warning message.
#    - It prints the list of found JPG files and asks for user confirmation before proceeding.
#    - Files are renamed to a numerical sequence (e.g., 1.jpg, 2.jpg, etc.).
#    - The script handles potential naming conflicts and logs any errors during the renaming process.

# 4. The `if __name__ == "__main__":` block:
#    - Sets up logging.
#    - Calls the `rename_jpg_files()` function.
#    - Keeps the console window open after execution (useful when run by double-clicking).

# 5. Throughout the script, there are various error handling and logging statements to capture and report any issues that may occur during execution.

# This script provides a user-friendly way to batch rename JPG files in a directory to a numerical sequence, with built-in safeguards and error handling.

import os
from pathlib import Path
import logging

def setup_logging():
    """Set up logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def rename_jpg_files():
    """
    Rename all jpg files in the current directory to numerical sequence
    Handles both .jpg and .JPG extensions and removes duplicates
    """
    try:
        # Use current directory
        folder = Path.cwd()
        
        # Print current working directory
        print(f"Current working directory: {folder}")
            
        # Get all jpg files with case-insensitive extensions
        jpg_files = []
        for ext in ['*.jpg', '*.JPG', '*.jpeg', '*.JPEG']:
            jpg_files.extend(list(folder.glob(ext)))
        
        # Remove duplicates by converting to set of unique paths
        jpg_files = sorted(set(jpg_files))
        
        if not jpg_files:
            logging.warning("No jpg files found in current directory")
            print("\nNo jpg files found!")
            print("Make sure this script is in the same folder as your images.")
            print("Supported extensions: .jpg, .JPG, .jpeg, .JPEG")
            print(f"Files in directory: {[f.name for f in folder.iterdir() if f.is_file()]}")
            return
            
        # Get the total number of files for padding
        total_files = len(jpg_files)
        padding_length = len(str(total_files))
        
        print(f"\nFound {total_files} unique jpg files:")
        for file in jpg_files:
            print(f"- {file.name}")
        
        # Ask for confirmation
        response = input("\nProceed with renaming these files? (y/n): ")
        if response.lower() != 'y':
            print("Operation cancelled by user")
            return
        
        print("\nRenaming files...")
        
        # Create a temporary mapping of old to new names
        rename_map = {}
        for index, file_path in enumerate(jpg_files, start=1):
            new_name = file_path.parent / f"{str(index).zfill(padding_length)}.jpg"
            rename_map[file_path] = new_name
            
        # Perform the renaming
        for old_path, new_path in rename_map.items():
            try:
                # Check if target name already exists
                if new_path.exists() and old_path != new_path:
                    logging.error(f"Cannot rename {old_path} to {new_path}: Target file already exists")
                    print(f"Error: Cannot rename {old_path.name} to {new_path.name}: File already exists")
                    continue
                    
                old_path.rename(new_path)
                print(f"Renamed: {old_path.name} → {new_path.name}")
                logging.info(f"Renamed {old_path.name} to {new_path.name}")
                
            except Exception as e:
                logging.error(f"Error renaming {old_path}: {str(e)}")
                print(f"Error renaming {old_path.name}: {str(e)}")
                
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Set up logging
    setup_logging()
    
    print("Starting to rename JPG files in current directory...")
    # Rename files
    rename_jpg_files()
    print("\nFinished renaming files. Check the logs for details.")
    
    # Keep console window open if run by double-clicking
    input("\nPress Enter to exit...")