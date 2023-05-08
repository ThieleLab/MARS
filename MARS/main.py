from MARS.utils import merge_files, normalize_dataframes, save_dataframes
from MARS.operations import split_taxonomic_groups, rename_taxa, check_presence_in_agora2

def process_microbial_abundances(input_file1, input_file2, output_path, output_format="csv"):
    merged_dataframe = merge_files(input_file1, input_file2)
    taxonomic_dataframes = split_taxonomic_groups(merged_dataframe)
    renamed_dataframes = rename_taxa(taxonomic_dataframes)
    normalized_dataframes = normalize_dataframes(renamed_dataframes)
    present_dataframes, absent_dataframes = check_presence_in_agora2(normalized_dataframes)

    dataframe_groups = {'normalized': normalized_dataframes, 'present': present_dataframes, 'absent': absent_dataframes}

    # Save the resulting DataFrames if output_path is provided
    if output_path is not None:
        save_dataframes(dataframe_groups, output_path, output_format)
    else:
        raise ValueError("Output path must be specified.")