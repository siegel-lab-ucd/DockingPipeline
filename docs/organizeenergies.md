# Documentation for `organizeenergies` Script

The `organizeenergies` script is designed to process and organize protein structure files based on their energy scores. It searches for specific directories containing energy score files, identifies the file with the lowest energy, and then organizes the corresponding protein structure files (PDB) into designated folders.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Usage](#usage)
3. [Output](#output)
4. [Troubleshooting](#troubleshooting)

## Prerequisites

Before using the `organizeenergies` script, please ensure the following requirements are met:

- Python 3 is installed on your system.
- The `pandas` library is installed in your Python environment. You can install it using `pip install pandas`.
- The script and the directories containing the energy score files (with `_cleaned` suffix) and the corresponding PDB files are located in the same base directory.

## Usage

1. **Place Script in Base Directory**:  
   Copy the `organizeenergies` script to the base directory, which contains subdirectories of protein data with `_cleaned` suffix.

2. **Executing the Script**:  
   Run the script using the following command in the terminal:

   ```bash
   python organizeenergies.py
   ```

3. **Automatic Directory Creation**:  
   The script will automatically create a `lowest_energies` directory within the base directory if it does not already exist.

4. **Processing Directories**:  
   The script will loop through each subdirectory that contains `_cleaned` in its name and look for the `relax_results` subdirectory within it.

5. **Identifying and Organizing Lowest Energy PDBs**:  
   Within each `relax_results` directory, the script will identify the `.sc` file with the lowest total energy score and copy its corresponding `.pdb` file to the `lowest_energies` directory.

6. **Organizing PDBs into Protein Folders**:  
   After copying, the script will organize the PDB files into folders named after the first four characters of the file (assumed to be the protein name).

## Output

Once the script has been executed, the following actions will have occurred:

- A new directory called `lowest_energies` exists in the base directory.
- Each PDB file with the lowest energy score is copied to the `lowest_energies` directory.
- Each PDB file in the `lowest_energies` directory is moved to a folder named after the protein it represents.
- The console will display messages for each copied and moved PDB file, as well as a completion message at the end.

## Troubleshooting

- If no valid `.sc` files are found in a `relax_results` directory, a message will be printed to the console.
- If there is an error reading a `.sc` file, an error message will be printed to the console along with the file path.
- If non-numeric total_score values are encountered, a message will be printed to the console indicating the file with the issue.

Should you encounter any issues, check the console messages for specific file-related errors and verify the directory structure and file formats are as expected. If the problem persists, ensure that the prerequisites are correctly installed and that the script has appropriate permissions to read from and write to the directories.