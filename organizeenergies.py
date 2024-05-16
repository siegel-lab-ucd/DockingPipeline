import os
import pandas as pd
import shutil

# Set the directory where the script is running
base_dir = os.getcwd()

# Create a directory for the lowest energy pdbs if it doesn't exist
lowest_energies_dir = os.path.join(base_dir, "lowest_energies")
if not os.path.exists(lowest_energies_dir):
    os.makedirs(lowest_energies_dir)

# Loop through each directory in the base directory
for dirname in os.listdir(base_dir):
    if "_cleaned" in dirname:
        relax_results_path = os.path.join(base_dir, dirname, "relax_results")
        if os.path.exists(relax_results_path):
            lowest_score = float('inf')
            lowest_score_file = None
            
            # Loop through each file in the relax_results directory
            for filename in os.listdir(relax_results_path):
                if filename.endswith(".sc"):
                    # Read the score file
                    filepath = os.path.join(relax_results_path, filename)
                    try:
                        # Adjusted to skip the initial lines and to correctly parse the header
                        score_data = pd.read_csv(filepath, delim_whitespace=True, skiprows=1, header=None)
                        score_data.columns = score_data.iloc[0]  # Set the first row as header
                        score_data = score_data[1:]  # Remove the header row from the data
                        score_data['total_score'] = pd.to_numeric(score_data['total_score'], errors='coerce')  # Convert total_score to numeric, coercing errors

                        # Check for rows where total_score could not be converted
                        if score_data['total_score'].isnull().any():
                            print(f"Non-numeric total_score values found in {filepath}")

                        # Find the row with the lowest total_score
                        min_row = score_data.loc[score_data['total_score'].idxmin()]
                        if min_row['total_score'] < lowest_score:
                            lowest_score = min_row['total_score']
                            lowest_score_file = min_row['description'] + ".pdb"
                    except Exception as e:
                        print(f"Error reading {filepath}: {e}")
            
            # If a lowest score file was found, copy it to the lowest_energies directory
            if lowest_score_file:
                source_file = os.path.join(relax_results_path, lowest_score_file)
                dest_file = os.path.join(lowest_energies_dir, lowest_score_file)
                shutil.copy2(source_file, dest_file)
                print(f"Copied {lowest_score_file} to {lowest_energies_dir}")
            else:
                print(f"No valid .sc files found in {relax_results_path}")

# Organize the lowest energy PDB files into their respective folders
for pdb_file in os.listdir(lowest_energies_dir):
    if pdb_file.endswith(".pdb"):
        # Extract the first four characters as the protein name
        protein_name = pdb_file[:4]
        protein_dir = os.path.join(lowest_energies_dir, protein_name)
        
        # Create a directory for the protein if it doesn't exist
        if not os.path.exists(protein_dir):
            os.makedirs(protein_dir)
        
        # Move the PDB file to the new directory
        shutil.move(os.path.join(lowest_energies_dir, pdb_file), os.path.join(protein_dir, pdb_file))
        print(f"Moved {pdb_file} to {protein_dir}")

# Print completion message
print("All lowest energy PDB files have been copied and organized into their respective protein folders.")

