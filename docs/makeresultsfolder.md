# `makeresultsfolder` Script Documentation

The `makeresultsfolder` script is a simple utility for automatically creating a subdirectory named `results` within each directory located in the same directory as the script. This documentation will guide you through how to use the `makeresultsfolder` script.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Output](#output)
- [Examples](#examples)

## Prerequisites

Before you can use the `makeresultsfolder` script, ensure that you have the following:

- A Unix-like operating system (e.g., Linux, macOS)
- Bash shell available (usually available by default on Unix-like systems)
- Write permissions in the directory where you want to create the `results` subdirectories

## Usage

To use the script, follow these steps:

1. Open your terminal application.
2. Navigate to the directory containing the `makeresultsfolder` script.
3. Ensure that the script has execute permissions. If not, you can add execute permissions with the following command:
   ```
   chmod +x makeresultsfolder
   ```
4. Run the script by typing `./makeresultsfolder` into the terminal and pressing Enter.

The script doesn't require any arguments. It will automatically scan the current directory for other directories and create a `results` subdirectory within each one that doesn't already have one.

**Note:** The script only creates the `results` folder in directories that are at the same level as the script itself. It does not recurse into subdirectories.

## Output

When you run the `makeresultsfolder` script, it will output a message for each directory it processes. There are two possible messages:

- `Created 'results' directory in <directory_name>/` if the script successfully creates a `results` directory.
- `'results' directory already exists in <directory_name>/` if a `results` directory already exists.

## Examples

Here's an example of how to use the `makeresultsfolder` script:

Suppose you have the following directory structure:

```
projects/
├── project1/
├── project2/
└── makeresultsfolder
```

After running the `makeresultsfolder` script, the structure will look like this:

```
projects/
├── project1/
│   └── results/
├── project2/
│   └── results/
└── makeresultsfolder
``` 

The script will output:

```
Created 'results' directory in project1/
Created 'results' directory in project2/
```

If the `results` directory already exists in one of the project directories, the output for that directory would be:

```
'results' directory already exists in project1/
```

That's all you need to know to start using the `makeresultsfolder` script to organize your projects with a standardized `results` subdirectory.