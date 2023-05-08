# MARS (Microbial Abundances Retrieved from Sequencing data)

MARS is a Python-based project designed to process and analyze microbial abundances, primarily relying on the pandas library. The main goal of this project is to provide an easy-to-use function for researchers to merge, process, and analyze microbial abundances.

## Features

- Merge two input files and perform various operations on the merged data.
- Split the merged data into separate taxonomic groups (Kingdom, Phylum, Class, Order, Family, Genus, Species).
- Normalize the data and perform various checks based on the AGORA2 resource.
- Save the processed dataframes for future use in other projects.

## Installation

1. Clone this repository:
```
git clone https://github.com/timhunuig/MARS.git
```

2. Change to the project directory:
```
cd MARS
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
    output_path="path/to/your/output_folder",
    output_format="csv"
)
```

Replace `"path/to/your/input_file1.txt"` and `"path/to/your/input_file2.txt"` with the paths to your input files, and `"path/to/your/output_folder"` with the path to the folder where you want to save the processed dataframes.

## Project Structure

The main components of the project are:

- `main.py`: Contains the main function that processes and analyzes the microbial abundances.
- `operations.py`: Contains functions for various operations such as splitting, renaming, and checking against AGORA2.
- `utils.py`: Contains utility functions used throughout the project.
- `tests/`: Contains test files for the project, including `test_operations.py` for testing the main function.

## Contributing

To contribute to this project, please open an issue on the GitHub repository with a description of the problem or the feature you would like to add. Once the issue is discussed and approved, you can create a pull request with your changes.