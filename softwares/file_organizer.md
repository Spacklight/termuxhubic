# File Organizer

## Description
Automatically sorts files in a folder by type (Images, Documents, Videos, Audio, Archives, Code, Executables).

## Features
- ✅ Zero installations required (uses only Python built-in libraries)
- ✅ Smart categorization based on file extensions
- ✅ Handles duplicate filenames safely
- ✅ Creates organized subfolders automatically
- ✅ Works on any folder (Downloads, Documents, etc.)

## How to Use in Termux

### Step 1: Download the script
```bash
curl -O https://raw.githubusercontent.com/spacklight/termuxhubic/main/softwares/file_organizer.py
```

### Step 2: Make it executable
```bash
chmod +x file_organizer.py
```

### Step 3: Run it on any folder
```bash
# Organize your Downloads folder
python file_organizer.py ~/Downloads

# Or organize any other folder
python file_organizer.py ~/Documents
```

## Requirements
- Python 3.x (pre-installed in Termux)
- No additional packages needed

## What It Does
- Scans the specified folder
- Creates subfolders: Images, Documents, Videos, Audio, Archives, Code, Executables, Others
- Moves files into their appropriate folders
- Handles duplicate filenames by adding _1, _2, etc.

## Example Output
