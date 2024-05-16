# Documentation for `organizecleanedpdbs.py`

The `organizecleanedpdbs.py` script is designed to organize Protein Data Bank (PDB) files that end with '_A.pdb' by moving them into designated directories and renaming them for consistency and ease of use. The script should be run in a directory containing subdirectories with PDB files.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Output](#output)
- [Example](#example)
- [Contact](#contact)

## Prerequisites

Before running `organizecleanedpdbs.py`, ensure that you have the following:
- Python installed on your system
- A directory containing subdirectories of PDB files to be organized

## Usage

To use `organizecleanedpdbs.py`, follow these steps:

1. Navigate to the directory containing the script.
2. Ensure the directory also contains subdirectories with PDB files that you want to organize.
3. Run the script using the following command:

```bash
python organizecleanedpdbs.py
```

The script will automatically identify PDB files ending with '_A.pdb' in the subdirectories of the current working directory.

## Output

Upon successful execution, the script will:
- Create a new directory for each protein named `[protein_name]_cleaned`.
- Move the corresponding '_A.pdb' file into the new directory.
- Rename the '_A.pdb' file by removing the '_A' suffix, resulting in `[protein_name].pdb`.

The script also prints a confirmation message once all applicable files have been processed:

```
All applicable files have been moved to their respective '_cleaned' folders and renamed.
```

## Example

Given the following directory structure before running the script:

```
current_working_directory/
├── protein1/
│   ├── protein1_A.pdb
│   └── protein1_B.pdb
└── protein2/
    ├── protein2_A.pdb
    └── protein2_X.pdb
```

After running the script, the structure will be updated to:

```
current_working_directory/
├── protein1/
│   └── protein1_B.pdb
├── protein1_cleaned/
│   └── protein1.pdb
├── protein2/
│   └── protein2_X.pdb
└── protein2_cleaned/
    └── protein2.pdb
```

## Contact

For questions or issues regarding the `organizecleanedpdbs.py` script, please contact the maintainer at [insert_contact_information].