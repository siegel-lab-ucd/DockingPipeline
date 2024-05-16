# BulkRelax Documentation

BulkRelax is a Python script designed to automate the process of setting up and submitting multiple protein relaxation jobs using Rosetta software on systems with SLURM workload management installed. This script will walk through the current directory and its subdirectories to find directories with "_cleaned" in their names. It will then generate a SLURM submission script for each `.pdb` file it finds in these directories and submit the job to the queue.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
  - [Starting the Script](#starting-the-script)
  - [Output](#output)
- [SLURM Script Configuration](#slurm-script-configuration)
- [Additional Notes](#additional-notes)

## Prerequisites

- Python 3.x installed on your system.
- Access to a Unix-like operating system with SLURM workload manager.
- Installed Rosetta software with the required database.
- Write permissions in the directory where the script is executed and its subdirectories.

## Usage

### Starting the Script

To use BulkRelax, follow these steps:

1. Place the `bulkrelax.py` script in the root directory from which you want to start the recursive search for `.pdb` files inside "_cleaned" directories.

2. Ensure that you are in the same directory as the `bulkrelax.py` file or provide the full path when calling it.

3. Run the script using Python:

```sh
python bulkrelax.py
```

The script will automatically:

- Search for subdirectories containing "_cleaned" in their name.
- Identify `.pdb` files within these directories.
- Create a `submit.sh` SLURM submission script for each `.pdb` file.
- Submit the job to the SLURM queue.
- Create an output directory named `relax_results` within the same directory as the `.pdb` file if it does not exist.

### Output

For each `.pdb` file, the script will generate a `submit.sh` file and print a message indicating that the files are being generated for the specific `.pdb` file. If an output directory named `relax_results` does not exist, it will create one and print a message stating that the folder is being created.

## SLURM Script Configuration

The SLURM submission script (`submit.sh`) created by BulkRelax has the following default configuration:

- The job name is set to the name of the `.pdb` file.
- The job's time limit is set to 3000 minutes.
- The job requests 4 cores.
- The job requests 16GB of memory.
- The job is submitted to the 'production' partition.
- The output is written to a file named `log.txt`.
- An array of 4 tasks is created, allowing multiple instances to run in parallel.
- The Rosetta relax application is configured with several options and the `.pdb` file as input.

## Additional Notes

- The script must be run by a user with sufficient privileges to submit jobs to SLURM and write to the directory structure.
- The script assumes that the Rosetta software and databases are located at a specific path (`/share/siegellab/software/kschu/Rosetta/main/`). Ensure that this path is correct for your system or modify the script accordingly.
- The script changes the working directory temporarily to submit jobs and then reverts to the original working directory. Ensure that this behavior is compatible with your workflow.

This documentation covers the basic usage of the BulkRelax script. For any modifications or troubleshooting, users should have a good understanding of Python, SLURM, and the Rosetta software suite.