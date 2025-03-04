# Protein Modeling and Docking Pipeline

A comprehensive pipeline for protein modeling with ESMFold and docking with Rosetta.

## Overview

This pipeline automates the process of:
1. Retrieving protein sequences from PDB
2. Folding proteins using ESMFold
3. Cleaning and organizing PDB structure files
4. Performing structure relaxation
5. Running docking simulations
6. Filtering and analyzing results

## Prerequisites

- Python 3.6+
- Pandas
- Matplotlib
- PyMOL (for protein-ligand visualization)
- Access to SLURM-based compute cluster with Rosetta installed
- ESMFold (local or via API)

## Pipeline Steps

### 1. Download FASTA Files

Download protein sequences in FASTA format:

```bash
python getfastas.py
```

For detailed documentation, see [docs/getfastas.md](docs/getfastas.md).

### 2. Fold Protein Structures

Generate 3D protein structures using ESMFold:

```bash
bash run_esmfold.sh /path/to/fasta/files /path/to/output/directory
```

For detailed documentation, see [docs/run_esmfold.md](docs/run_esmfold.md).

### 3. Organize PDB Files

Organize the generated structures:

```bash
python pdbs/organizepdbs.py
```

For detailed documentation, see [docs/organizepdbs.md](docs/organizepdbs.md).

### 4. Clean PDB Files

Remove extraneous information and prepare files for Rosetta:

```bash
bash pdbs/cleanpdbs.sh
```

For detailed documentation, see [docs/cleanpdbs.md](docs/cleanpdbs.md).

### 5. Organize Cleaned PDB Files

Sort and organize the cleaned structures:

```bash
python pdbs/organizecleanedpdbs.py
```

This creates directories with the `_cleaned` suffix. For detailed documentation, see [docs/organizecleanedpdbs.md](docs/organizecleanedpdbs.md).

### 6. Relax Structures

Submit jobs to relax the protein structures using Rosetta:

```bash
python pdbs/bulkrelax.py
```

⚠️ **IMPORTANT:** Only run this once! Running it multiple times will submit duplicate jobs. If you need to redo this step, first delete all files in the cleaned folders.

For detailed documentation, see [docs/bulkrelax.md](docs/bulkrelax.md).

### 7. Select Lowest Energy Models

Identify and extract the lowest energy structures:

```bash
python pdbs/organizeenergies.py
```

For detailed documentation, see [docs/organizeenergies.md](docs/organizeenergies.md).

### 8. Prepare for Docking

Get required docking scripts and files:

```bash
python pdbs/lowest_energies/getscripts.py
```

For detailed documentation, see [docs/getscripts.md](docs/getscripts.md).

### 9. Create Results Directory

Prepare the output directory for docking results:

```bash
bash pdbs/lowest_energies/makeresultsfolder.sh
```

For detailed documentation, see [docs/makeresultsfolder.md](docs/makeresultsfolder.md).

### 10. Prepare Protein-Ligand Complex

Using PyMOL, prepare the protein-ligand complex:

1. Open the folded protein file
2. Open the template protein-ligand complex
3. Align the proteins
4. Delete the template protein, keeping only the ligand
5. Save the new complex as a PDB file
6. Update `docking_scripts/run.sh` with the correct PDB filename

### 11. Add PDB Header

Add the required header information to your PDB:

```bash
cat docking_scripts/1eh5.header your_model.pdb > your_model_with_header.pdb
```

### 12. Run Docking

Submit the docking job to the cluster:

```bash
cd docking_scripts
sbatch run.sh
```

### 13. Filter Results

Once docking is complete, filter and analyze the results:

```bash
python filter.py
# OR
python gettop5.py
```

The `gettop5.py` script extracts the top 5 models by energy score and copies them to a `top5` directory.

## Directory Structure

```
DockingPipeline/
├── getfastas.py              # Download FASTA files
├── run_esmfold.sh            # Run ESMFold for structure prediction
├── filter.py                 # Simple filter for docking results
├── gettop5.py                # Extract top 5 models by energy
├── docking_scripts/          # Rosetta docking configuration files
├── docs/                     # Detailed documentation
└── pdbs/                     # Scripts for PDB processing
    ├── bulkrelax.py          # Structure relaxation
    ├── cleanpdbs.sh          # PDB cleaning script
    ├── organizecleanedpdbs.py # Sort cleaned PDBs
    ├── organizeenergies.py    # Extract lowest energy models
    ├── organizepdbs.py        # Sort generated PDBs
    └── lowest_energies/       # Scripts for final processing
        ├── makeresultsfolder.sh
        └── getscripts.py
```

## Troubleshooting

- If jobs fail on the cluster, check SLURM output logs in the `logs` directory
- Ensure all file paths are correct before running each step
- For issues with structure alignment, try different alignment methods in PyMOL
