# GetFASTAs Documentation

This document serves as a guide for users to understand and utilize the `getfastas` script, which is designed to fetch FASTA sequence data for a predefined list of protein structures based on their PDB IDs from the RCSB Protein Data Bank (PDB).

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Output](#output)
- [Troubleshooting](#troubleshooting)

## Introduction

The `getfastas` script automates the process of downloading FASTA sequence data for a collection of protein structures identified by their PDB IDs. This is particularly useful for researchers or bioinformaticians who need to work with the amino acid sequences of a specific subset of proteins without manually visiting the PDB website for each entry.

## Requirements

Before you use the `getfastas` script, ensure that you have the following prerequisites:

- Python installed on your system.
- The `requests` library installed in your Python environment. If you do not have it installed, you can install it using pip:

  ```shell
  pip install requests
  ```

## Usage

To use the `getfastas` script, follow these steps:

1. **Prepare PDB ID List**: Edit the `pdb_ids` list within the script to include the PDB IDs of the protein structures you wish to download FASTA sequences for.

    ```python
    pdb_ids = [
        "1eh5", "1h2j", "1hqd", ... , "6cpa"
    ]
    ```

2. **Run the Script**: Execute the script in your Python environment. You can run the script from the command line using:

    ```shell
    python getfastas.py
    ```

   Replace `getfastas.py` with the actual path to the script if it's located in a different directory.

3. **Check Output**: Upon successful execution, the script will generate a `.fasta` file for each PDB ID in the current working directory.

## Output

For each valid PDB ID provided in the `pdb_ids` list, the `getfastas` script will create a separate file with a `.fasta` extension. The name of each file corresponds to its PDB ID. For example, if `1eh5` is in the list of PDB IDs, you will find a `1eh5.fasta` file in the directory where you ran the script.

Each FASTA file contains the protein sequence data in the following format:

```
>Header Information
SEQUENCE
```

If a PDB ID fails to fetch data, you will see a message printed to the console indicating the failure:

```
Failed to fetch data for PDB ID: <pdb_id>
```

## Troubleshooting

- **Missing Python or Requests Library**: Ensure that you have Python and the `requests` library installed.
- **Network Issues**: Check your internet connection if you are unable to fetch data from PDB.
- **PDB ID Errors**: Verify that the PDB IDs in your list are correct and are available in the RCSB PDB database.
- **Script Permissions**: Make sure that you have the necessary permissions to execute the script and write files to the directory.

If you encounter any issues or have questions regarding the `getfastas` script, please refer to the official documentation for Python and the `requests` library or contact the maintainers of the RCSB PDB database.