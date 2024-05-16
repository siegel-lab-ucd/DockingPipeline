#!/bin/bash
#SBATCH --job-name=dock4real
#SBATCH --output=logs
#SBATCH --mem 4G
#SBATCH --nodes 1
#SBATCH --time 1-0
#SBATCH --array=1-10

/share/siegellab/kschu/software/Rosetta/main/source/bin/rosetta_scripts.default.linuxgccrelease -database /share/siegellab/software/kschu/Rosetta/main/database @flags -overwrite -parser:protocol docking_new.xml -s esm_lig.pdb -out:path:all results -nstruct 100 -suffix _$SLURM_ARRAY_TASK_ID -score:weights ref2015_cst

