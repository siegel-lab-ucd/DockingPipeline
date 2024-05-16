#!/bin/bash

#SBATCH --partition=gpu-jbsiegel
#SBATCH --time=72:00:00
#SBATCH --gres=gpu:1
#SBATCH --mem=32G
#SBATCH --ntasks=8
#SBATCH --output=output.txt
#SBATCH --error=error.txt

if [ $# -lt 2 ]; then
    echo "Usage: $0 <fasta_file_path> <output_directory>"
    exit 1
fi

# Activate the conda environment
export TORCH_HOME=/share/siegellab/aian/scripts/torch_cache

# Activate the conda environment
. "/toolbox/softwares/anaconda3/etc/profile.d/conda.sh"
conda activate /share/siegellab/aian/scripts/Miniconda/envs/esmfold

# Run the Python script with the FASTA file path and output directory as arguments
python /share/siegellab/aian/scripts/esmfold.py "$1" "$2"
