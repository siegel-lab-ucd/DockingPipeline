# Protein Modeling and Docking Workflow

## Table of Contents
1. [Downloading FASTA Files](#downloading-fasta-files)
2. [Folding Proteins](#folding-proteins)
3. [Organizing PDB Files](#organizing-pdb-files)
4. [Cleaning PDB Files](#cleaning-pdb-files)
5. [Organizing Cleaned PDB Files](#organizing-cleaned-pdb-files)
6. [Relaxing Structures](#relaxing-structures)
7. [Selecting Lowest Energy Models](#selecting-lowest-energy-models)
8. [Preparing for Docking](#preparing-for-docking)
9. [Docking Process](#docking-process)
10. [Final Steps](#final-steps)


## File Locations
```
main_folder/
├── getfastas.py
├── run_esmfold.sh
└── pdbs/
    ├── bulkrelax.py
    ├── organizecleanedpdbs.py
    ├── organizeenergies.py
    ├── organizepdbs.py
    └── lowest_energies/
        ├── makeresultsfolder.sh
        └── getscripts.py
```
## Downloading FASTA Files
First, you need to download the FASTA files for all of the proteins you are using. Since we are getting them for this project from a list from PDB, we can use the script `get_fastas.py` documents for which can be found [here](docs/getfastas.md). Run the script using:
```bash
python get_fastas.py
```
If you are using this workflow for another project, procure the FASTA files yourself.

## Folding Proteins
Once you have all of the FASTA files, you can fold them using the script `run_esmfold.sh` documents for which can be found [here](docs/run_esmfold.md). Run the script using:
```bash
bash run_esmfold.sh $fastapath $outputdirectory
```

## Organizing PDB Files
Your PDB files might be disorganized, so you can use the `organizepdbs.py` script to organize everything. The script can be found [here](docs/organizepdbs.md). Run the script using:
```bash
python organizepdbs.py
```

## Cleaning PDB Files
Next, everything needs to be cleaned. Use the script `cleanpdbs.sh` documents for which can be found [here](docs/cleanpdbs.md). Run the script using:
```bash
bash cleanpdbs.sh
```

## Organizing Cleaned PDB Files
Once everything is cleaned, we need to get them in the appropriate folders. This can be done with `organizecleanedpdbs.py` documents for which can be found [here](docs/organizecleanedpdbs.md). Run the script using:
```bash
python organizecleanedpdbs.py
```
This will create new folders with the `_cleaned` tag for our later relaxing.

## Relaxing Structures
Next, we need to relax everything. We can use the script `bulkrelax.py` documents for which can be found [here](docs/bulkrelax.md). Run the script using:
```bash
python bulkrelax.py
```
This will submit SLURM jobs for each of the PDB files to relax them. **IMPORTANT:** Only do this step once, as it looks for PDB files within the cleaned folder. If you have new PDB files from your first run, it will submit a job for those too, potentially flooding CACAO. If you need to redo this step, delete everything in the cleaned folders and start from the cleaning step again.

## Selecting Lowest Energy Models
Now we need to get the lowest energy model from the relaxed structures. This can be done using the script `organizeenergies.py` documents for which can be found [here](docs/organizeenergies.md). Run the script using:
```bash
python organizeenergies.py
```
This script moves the lowest energy model to its own folder for docking.

## Preparing for Docking
Next, we need to get the docking scripts from the other files. This can be done using the `getscripts.py` script documents for which can be found [here](docs/getscripts.md) in the `lowest_energies` folder. If you are copying this pipeline for your own proteins, you can view them in the `docking_scripts` folder and view their documentation [here](docs/dockingscripts.md).

## Docking Process
Remember, for docking, we need to have a results folder ready. You can use the `makeresultsfolder.sh` script documents for which can be found [here](docs/makeresultsfolder.md). Run the script using:
```bash
bash makeresultsfolder.sh
```
If you prefer, you can create the results folder yourself before starting the docking.

Next, you need to merge your new protein with the ligand. There is no script for this step. We recommend using PyMOL:
1. Open the new protein file first (due to limitations with Rosetta).
2. Open the existing protein/ligand complex.
3. Align them.
4. Delete the existing protein.
5. Export the newly modeled protein complexed with the original ligand as a molecule under a PDB file.
6. Upload that back to the cluster and edit the `run.sh` file to include the name of the new PDB. 
7. Add `#SBATCH --array=1-10` at the bottom of the list of SLURM commands so that it runs in an array.

## Final Steps
Finally, add the header to your PDB file by typing the following command:
```bash
cat headerfile inputpdb > outputfilename
```
If you are doing this with your own proteins, you must do this yourself.

To complete the process, run the following command:
```bash
sbatch run.sh
```
Wait for everything to finish, and you're done!
 
