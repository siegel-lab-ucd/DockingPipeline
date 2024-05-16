import os
import shutil

# List of protein names
proteins = [
    "1eh5", "1h2j", "1hqd", "1jcl", "1ju3", "1ney", 
    "1ogx", "1oh0", "1oif", "1oim", "1p6o", "1tqh", 
    "1w6y", "1xpz", "2gke", "2jaj", "2jie", "2nlr", 
    "3ia2", "3veu", "4fua", "6cpa"
]

# Base directory where the script is run (adjust as necessary)
base_dir = os.getcwd()

# Path to the RosettaFold_ligand directories
rosettafold_base = "/share/siegellab/software/kschu/RoseTTAFold/benchmark/monomer/RosettaFold_ligand"

# Loop through each protein
for protein in proteins:
    source_dir = os.path.join(rosettafold_base, protein, "model1")
    target_dir = os.path.join(base_dir, protein)
    
    if os.path.exists(source_dir):
        # Only copy files, not directories, and ignore backup files
        for file_name in os.listdir(source_dir):
            if not file_name.endswith("~"):  # Ignore backup files
                source_file = os.path.join(source_dir, file_name)
                if os.path.isfile(source_file):
                    target_file = os.path.join(target_dir, file_name)
                    shutil.copy2(source_file, target_file)
                    print(f"Copied {file_name} from {source_dir} to {target_dir}")
                else:
                    print(f"Skipped {file_name} because it is a directory, not a file.")
    else:
        print(f"Source directory does not exist: {source_dir}")

# Print completion message
print("All specified files have been copied to their respective protein folders.")

