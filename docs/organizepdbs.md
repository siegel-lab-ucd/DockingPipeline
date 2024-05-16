# OrganizePDBs Documentation

OrganizePDBs is a Python script designed to help users organize their PDB (Protein Data Bank) files into separate folders. This document provides instructions on how to use the script to automate the process of renaming and categorizing PDB files in a directory.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Example](#example)
- [Output](#output)

## Prerequisites

Before using OrganizePDBs, ensure you have the following:

- Python installed on your system
- PDB files present in the directory where the script will be executed

## Usage

To use OrganizePDBs, follow these steps:

1. Place the `organizepdbs` Python script in the directory containing your PDB files.
2. Open a terminal or command prompt window.
3. Navigate to the directory containing the script and your PDB files.
4. Run the script by executing the command `python organizepdbs`.

Upon execution, the script will perform the following actions:

- Identify all files in the current directory that have a `.pdb` extension.
- Rename each PDB file by taking the first four characters of its original name, converting them to lower case, and ensuring the `.pdb` extension is retained.
- Create a new folder for each renamed PDB file, using the file's new name (without the extension) as the folder name.
- Move each renamed PDB file into its corresponding new folder.

## Example

Imagine your directory contains the following PDB files:

```
1ABC.pdb
2XYZ.pdb
3DEF.pdb
```

After running the OrganizePDBs script, your directory will be structured as follows:

```
1abc/
    1abc.pdb
2xyz/
    2xyz.pdb
3def/
    3def.pdb
```

## Output

Once the script has finished running, it will print the following message to the console:

```
All PDB files have been renamed and moved to their respective folders.
```

This indicates that all PDB files found in the directory have been successfully renamed and organized into their new folders.

For any questions or issues regarding the usage of OrganizePDBs, please refer to this documentation or the comments within the script file.