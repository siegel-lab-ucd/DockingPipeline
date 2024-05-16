# GetScripts Usage Documentation

GetScripts is a Python utility designed to copy specific files related to protein structures from a source directory to a target directory. It is particularly useful for researchers and bioinformaticians who work with protein data and require an efficient way to transfer multiple files across directories.

## Table of Contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Usage](#usage)
4. [Protein List Customization](#protein-list-customization)
5. [Customizing Source and Target Directories](#customizing-source-and-target-directories)
6. [Execution](#execution)
7. [Completion Message](#completion-message)

---

### Introduction

This script automates the process of copying files from a predetermined list of protein names. Each protein has its own folder under a common base directory, and the script will copy files from a source directory to these protein folders.

---

### Requirements

Before running the script, ensure that the following prerequisites are met:

- Python is installed on your system.
- The necessary permissions to read from the source directory and write to the target directory are granted.
- The source directory contains subdirectories named after the proteins listed in the script.

---

### Usage

The script is designed to be used with minimal interaction. The primary action required from the user is to run the script after customizing the protein list, source directory, and target directory according to their needs.

---

### Protein List Customization

The `proteins` list contains the default protein names. To customize:

1. Open the script in a text editor.
2. Locate the `proteins` array.
3. Modify the list to include the protein names relevant to your work.

Example:
```python
proteins = [
    "protein1", "protein2", "protein3", # Add your protein names here
]
```

---

### Customizing Source and Target Directories

By default, the script assumes a specific location for the source (`rosettafold_base`) and uses the current working directory as the target (`base_dir`).

To customize these paths:

1. Open the script in a text editor.
2. Locate the `rosettafold_base` and `base_dir` variables.
3. Update the paths to match your directory structure.

Example:
```python
base_dir = "/path/to/your/target/directory"
rosettafold_base = "/path/to/your/source/directory"
```

---

### Execution

To execute the script:

1. Navigate to the directory containing the script.
2. Run the script using Python.

Example command:
```bash
python getscripts.py
```

---

### Completion Message

Upon successful execution, the script will print a message for each file copied, indicating the source and target locations. When all specified files have been copied, it prints a final completion message.

---

**Note**: The script does not copy subdirectories or backup files (those ending with a tilde `~`). Ensure that only the files you want to be copied are in the source subdirectories.