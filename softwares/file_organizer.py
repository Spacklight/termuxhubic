#!/usr/bin/env python3
"""
File Organizer - Automatically sorts files by type
Usage:
  python file_organizer.py [folder_path]
  python file_organizer.py ~/Downloads
"""

import os
import shutil
import sys

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".csv"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
    "Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".php", ".rb", ".go"],
    "Executables": [".apk", ".exe", ".msi", ".deb", ".rpm"]
}

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"❌ Error: Folder '{folder_path}' does not exist!")
        return
    
    if not os.path.isdir(folder_path):
        print(f"❌ Error: '{folder_path}' is not a folder!")
        return
    
    print(f"📂 Organizing: {folder_path}")
    print("=" * 50)
    
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    if not files:
        print("✅ Folder is already empty!")
        return
    
    moved_count = 0
    
    for filename in files:
        if filename == "file_organizer.py":
            continue
            
        source_path = os.path.join(folder_path, filename)
        category = get_category(filename)
        
        category_folder = os.path.join(folder_path, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
            print(f"📁 Created folder: {category}")
        
        destination_path = os.path.join(category_folder, filename)
        
        if os.path.exists(destination_path):
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(destination_path):
                new_filename = f"{base}_{counter}{ext}"
                destination_path = os.path.join(category_folder, new_filename)
                counter += 1
        
        shutil.move(source_path, destination_path)
        print(f"✅ Moved: {filename} → {category}/")
        moved_count += 1
    
    print("=" * 50)
    print(f"🎉 Done! Organized {moved_count} files.")

def main():
    print("🗂️  File Organizer - Auto-sort your files")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
    else:
        folder_path = os.getcwd()
        print(f"💡 No folder specified. Using current directory: {folder_path}")
        print("💡 Tip: python file_organizer.py ~/Downloads")
        print()
    
    organize_folder(folder_path)

if __name__ == "__main__":
    main()
