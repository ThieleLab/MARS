import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from MARS.main import process_microbial_abundances

if __name__ == '__main__':

    test_files_dir = os.path.join(os.path.dirname(__file__), 'test_files')

    file1_path = os.path.join(test_files_dir, 'feature-table.txt')
    file2_path = os.path.join(test_files_dir, 'taxonomy.tsv')
    stratification = os.path.join(test_files_dir, 'stratification_file.csv')

    result_dataframes = process_microbial_abundances(file1_path, file2_path, stratification_file=stratification, output_path=r"/path/to/your/output/folder")
