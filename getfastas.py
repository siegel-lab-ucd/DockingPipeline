import requests

# List of PDB IDs to search for
pdb_ids = [
    "1eh5", "1h2j", "1hqd", "1jcl", "1ju3", "1ney", "1ogx", "1oh0", "1oif", "1oim",
    "1p6o", "1tqh", "1w6y", "1xpz", "2gke", "2jaj", "2jie", "2nlr", "3ia2", "3veu",
    "4fua", "6cpa"
]

# Base URL for fetching sequence data from PDB
base_url = "https://www.rcsb.org/fasta/entry/"

for pdb_id in pdb_ids:
    # Fetch the FASTA sequence for the current PDB ID
    response = requests.get(f"{base_url}{pdb_id}")
    if response.status_code == 200:
        # Open a file named after the PDB ID to write the FASTA sequence
        with open(f"{pdb_id}.fasta", "w") as fasta_file:
            fasta_file.write(response.text)
    else:
        print(f"Failed to fetch data for PDB ID: {pdb_id}")

print("Individual FASTA file creation for each protein completed.")

