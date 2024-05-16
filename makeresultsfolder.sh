#!/bin/bash

# Loop through each item in the current directory
for d in */ ; do
    # Check if it's a directory
    if [ -d "$d" ]; then
        # Check if the 'results' directory does not exist
        if [ ! -d "${d}results" ]; then
            # Create the 'results' directory
            mkdir "${d}results"
            echo "Created 'results' directory in $d"
        else
            echo "'results' directory already exists in $d"
        fi
    fi
done
