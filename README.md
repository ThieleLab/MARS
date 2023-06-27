# MARS (Microbial Abundances Retrieved from Sequencing data)

MARS (Microbial Abundance Processing and Analysis) is a Python-based tool designed to process and analyze microbial abundance data. It merges input files, splits the merged data into taxonomic groups, renames taxa, checks the presence of the renamed taxa in AGORA2, normalizes the data, calculates metrics, and saves the resulting dataframes. MARS also supports stratification of the data based on a provided stratification file. The main goal of this project is to provide an easy-to-use function for researchers.

## Features

- Data Merging: MARS can merge two input files into a single dataframe.
- Taxonomic Grouping: MARS splits the merged data into taxonomic groups (Kingdom, Phylum, Class, Order, Family, Genus, Species).
- Taxa Renaming: MARS renames the taxa in the dataframe.
- AGORA2 Presence Check: MARS checks the presence of the renamed taxa in AGORA2.
- Data Normalization: MARS normalizes the dataframes.
- Metric Calculation: MARS calculates metrics for the renamed and present dataframes.
- Stratification: MARS supports stratification of the data based on a provided stratification file. It calculates metrics for each group in the stratification.
- Data Saving: MARS saves the resulting dataframes if an output path is provided.

## Installation

1. Clone this repository:
```
git clone https://github.com/ThieleLab/MARS.git
```

2. Change to the project directory:
```
cd mars-project
```

3. Install the required packages using pip:
```
pip install -r requirements.txt
```

## Usage

Import the main function from the `main` module in your Python script:

```python
from MARS.main import process_microbial_abundances
```

Call the `process_microbial_abundances()` function with the required parameters:

```python
result_dataframes = process_microbiome_data(
    file_path1="path/to/your/input_file1.txt",
    file_path2="path/to/your/input_file2.txt",
    output_path=None,
    cutoff=None,
    output_format="csv",
    stratification_file=None
)
```

Here's what the arguments do:

- `input_file1` and `input_file2`: These are the two input files that you want to merge.
- `output_path` (optional): This is the path where you want to save the resulting dataframes.
- `cutoff` (optional): This is the cutoff value used when normalizing the dataframes.
- `output_format` (optional): This is the format in which you want to save the resulting dataframes. The default is "csv".
- `stratification_file` (optional): This is the path to a stratification file. If provided, MARS will calculate metrics for each group in the stratification.

Replace `"path/to/your/input_file1.txt"` and `"path/to/your/input_file2.txt"` with the paths to your input files, and `"path/to/your/output_folder"` with the path to the folder where you want to save the processed dataframes.

## Project Structure

The main components of the project are:

- `main.py`: Contains the main function that processes and analyzes the microbial abundances.
- `operations.py`: Contains functions for various operations such as splitting, renaming, checking against AGORA2, and calculating metrics.
- `utils.py`: Contains utility functions used throughout the project.
- `tests/`: Contains test files for the project, including `test.py` for testing the main function and example files in `test_files`.

## Contributing

To contribute to this project, please open an issue on the GitHub repository with a description of the problem or the feature you would like to add. Once the issue is discussed and approved, you can create a pull request with your changes.