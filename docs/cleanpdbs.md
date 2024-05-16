# `cleanpdbs` Documentation

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Output](#output)
- [Troubleshooting](#troubleshooting)

## Overview

The `cleanpdbs` script is a utility for batch processing Protein Data Bank (PDB) files located within subdirectories of the current working directory. It automates the cleaning of these files by invoking a Python script, `clean_pdb.py`, specifically on chain A of each PDB file discovered.

## Prerequisites

Before using the `cleanpdbs` script, ensure you meet the following requirements:

1. **Python 2:** The script `clean_pdb.py` is executed with Python 2. Make sure Python 2 is installed on your system.
2. **clean_pdb.py**: Ensure the `clean_pdb.py` script is located at `/share/siegellab/software/kschu/Rosetta/tools/protein_tools/scripts/`. This path is hardcoded in the script.
3. **PDB Files**: Have your PDB files organized within subdirectories of the directory from where you will run `cleanpdbs`.
4. **File Permissions**: Ensure `cleanpdbs` is executable. You can set the executable permission with the following command:
   ```
   chmod +x cleanpdbs
   ```

## Usage

To use the `cleanpdbs` script, follow these steps:

1. **Open Terminal**: Navigate to the terminal on your system.
2. **Change Directory**: Use the `cd` command to navigate to the directory that contains `cleanpdbs`.
3. **Execute Script**: Run the script by typing `./cleanpdbs` into the terminal.

The script will automatically search for all `.pdb` files within the current directory and its subdirectories, then proceed to clean each file by running the `clean_pdb.py` script on chain A.

## Output

Upon execution, `cleanpdbs` will produce the following output:

- A confirmation message that the cleaning process has started.
- A list of all found `.pdb` files that will be processed.
- A message for each file processed, indicating the file is being processed.
- A final message indicating the cleaning process is complete.

The cleaned PDB files will be the output of the `clean_pdb.py` script, which usually generates cleaned versions of the PDB files. These files should be located in the same directory as the original PDB files.

## Troubleshooting

If you encounter issues with the `cleanpdbs` script, consider the following troubleshooting steps:

- **Check Python Version**: Make sure Python 2 is installed and accessible from the command line.
- **Script Location**: Verify the `clean_pdb.py` script exists at the specified path.
- **File Permissions**: Confirm `cleanpdbs` and `clean_pdb.py` are both executable.
- **No PDB Files Found**: Ensure that there are `.pdb` files within the directory and its subdirectories.

For any other issues not covered here, check the error messages provided in the terminal for clues about what might have gone wrong.

Remember that this documentation focuses on the usage of the `cleanpdbs` script rather than its internal workings. If further customization or understanding of the underlying script `clean_pdb.py` is required, consult the documentation or source code for that specific script.