import os
import pandas as pd
import matplotlib.pyplot as plt

filenames = [filename for filename in os.listdir() if '.sc' in filename]
score_list = []

for filename in filenames:
    df = pd.read_csv(filename, sep='\s+')  # Use sep='\s+' to handle whitespace separation
    if 'SCORE:' in df.columns:
        del df['SCORE:']
    
    # Check if 'description' column exists to avoid KeyError
    if 'description' in df.columns:
        # Create the 'File Name' column using 'description' values
        df['File Name'] = df['description'].apply(lambda x: f"{x}_") + (df.index + 1).astype(str).str.zfill(4) + ".pdb"
    else:
        print(f"'description' column not found in {filename}. Skipping 'File Name' generation for this file.")
    
    score_list.append(df)

# Concatenate all dataframes into one
df2 = pd.concat(score_list, ignore_index=True)

# Filter rows based on condition
df4 = df2[df2['all_cst'] < .2]

# Sort the filtered dataframe by total_score
df5 = df4.sort_values('total_score')

# Display the final DataFrame
pd.set_option('display.max_rows', None)
print(df5)

# Plot histogram for 'all_cst' column
df2['all_cst'].hist()
plt.show()
