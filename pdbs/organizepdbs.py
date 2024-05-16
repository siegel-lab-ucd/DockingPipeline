import os
import shutil

# Get the current working directory
cwd = os.getcwd()

# List all files in the current directory
files = os.listdir(cwd)

# Filter for files that end with .pdb
pdb_files = [file for file in files if file.endswith('.pdb')]

# Iterate over the pdb files
for pdb in pdb_files:
    # Extract the first 4 characters and convert to lower case
    new_file_name = pdb[:4].lower() + '.pdb'
    
    # Rename the file
    os.rename(os.path.join(cwd, pdb), os.path.join(cwd, new_file_name))
    
    # Extract the name without the .pdb extension
    folder_name = new_file_name[:-4]
    
    # Create a new path for the folder
    new_folder_path = os.path.join(cwd, folder_name)
    
    # Check if the folder already exists, if not, create it
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
    
    # Move the renamed pdb file into its respective folder
    shutil.move(os.path.join(cwd, new_file_name), new_folder_path)

print("All PDB files have been renamed and moved to their respective folders.")
