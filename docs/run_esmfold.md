# `run_esmfold` Documentation

The `run_esmfold` script is a Bash script designed to facilitate the execution of the `esmfold.py` protein folding prediction program on a computing cluster using Slurm Workload Manager. Below is the documentation on how to use this script.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Script Overview](#script-overview)
- [Usage](#usage)
- [SLURM Directives](#slurm-directives)
- [Error Handling](#error-handling)
- [Output](#output)
- [Contact](#contact)

## Prerequisites

Before running the `run_esmfold` script, ensure the following prerequisites are met:

1. Access to a computing cluster with Slurm Workload Manager.
2. Availability of a GPU partition named `gpu-jbsiegel`.
3. The necessary conda environment and `esmfold.py` script located at specified paths.
4. A FASTA file containing protein sequences to be processed.
5. An existing directory where output files will be saved.

## Script Overview

The `run_esmfold` script is a job submission script for Slurm. It sets up various job parameters such as partition name, time limit, GPU usage, memory allocation, number of tasks, and output/error file paths. After configuring the job environment, it checks for the correct number of arguments, activates a conda environment, and runs the `esmfold.py` script with the user-provided FASTA file and output directory.

## Usage

To use the `run_esmfold` script, follow these steps:

1. Load the `run_esmfold` script onto the cluster where you have Slurm access.
2. Ensure you have a FASTA file with protein sequences and an output directory prepared.
3. Submit the script to the Slurm scheduler using the `sbatch` command followed by the script name and required arguments:

```sh
sbatch run_esmfold <fasta_file_path> <output_directory>
```

Replace `<fasta_file_path>` with the full path to your FASTA file and `<output_directory>` with the path to the directory where you want the results to be saved.

## SLURM Directives

The following SLURM directives are used in the script:

- `--partition=gpu-jbsiegel`: Specifies the partition (or queue) for the job.
- `--time=72:00:00`: Sets the maximum time for the job, here it is set to 72 hours.
- `--gres=gpu:1`: Requests one GPU for the job.
- `--mem=32G`: Allocates 32GB of memory for the job.
- `--ntasks=8`: Sets the number of tasks to run in parallel to 8.
- `--output=output.txt`: Specifies the file to which standard output should be written.
- `--error=error.txt`: Specifies the file to which standard error should be written.

## Error Handling

The script checks for the presence of at least two arguments. If the required number of arguments is not provided, it will display a usage message:

```
Usage: $0 <fasta_file_path> <output_directory>
```

and then exits with a status code of 1, indicating that the job has failed due to insufficient arguments.

## Output

The standard output and error of the `esmfold.py` script execution are redirected to the files `output.txt` and `error.txt`, respectively, in the current working directory.

## Contact

For any issues or further assistance with the `run_esmfold` script, please contact the system administrator or the individual responsible for maintaining the `esmfold.py` script within the Siegel Lab.

---

**Note**: The documentation above assumes that the paths and environment settings are correctly configured for the specific cluster and user environment. Adjust the paths and names accordingly if they differ from this documentation.