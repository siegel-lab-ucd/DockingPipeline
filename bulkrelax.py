import os
import subprocess

initial_working_dir = os.getcwd()

for path, subdirs, files in os.walk(initial_working_dir):
    # Check if "_cleaned" is in the folder name
    if "_cleaned" in path:
        for name in files:
            # Check for .pdb files (not specifically ending with "_A.pdb")
            if name.endswith(".pdb"):
                filename = os.fsdecode(name)
                print('Generating Files for: ' + filename)
                submit_script_path = os.path.join(path, 'submit.sh')
                with open(submit_script_path, 'w') as submit_script:
                    submit_script.write('#!/bin/bash -l\n')
                    submit_script.write('#SBATCH -J ' + filename + '\n')
                    submit_script.write('#SBATCH -t 3000\n')
                    submit_script.write('#SBATCH -n 4\n')
                    submit_script.write('#SBATCH --mem 16GB\n')
                    submit_script.write('#SBATCH -p production\n')
                    submit_script.write('#SBATCH --output=log.txt\n')
                    submit_script.write('#SBATCH --array=1-4\n\n')
                    submit_script.write('/share/siegellab/software/kschu/Rosetta/main/source/bin/relax.default.linuxgccrelease -database /share/siegellab/software/kschu/Rosetta/main/database -overwrite -nstruct 50 -ex1 -ex2 -use_input_sc -flip_HNQ -no_optH false -user_tag $SLURM_ARRAY_TASK_ID -out:suffix $SLURM_ARRAY_TASK_ID -relax:constrain_relax_to_start_coords -relax:coord_constrain_sidechains -relax:ramp_constraints false -in:file:s ' + filename + ' -out:path:all relax_results\n')

                # Change directory to where submit.sh is located
                os.chdir(path)

                # Submit the job using sbatch
                subprocess.call(['sbatch', submit_script_path], cwd=path)

                new_output = os.path.join(path, 'relax_results')
                if not os.path.exists(new_output):
                    os.makedirs(new_output)
                    print('Results folder not found for ' + name + '...creating...')

                # Change back to the initial working directory
                os.chdir(initial_working_dir)

print('Complete!')

