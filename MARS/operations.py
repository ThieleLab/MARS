import pandas as pd
import json
import os

def split_taxonomic_groups(merged_df):
    """
    Split the taxonomic groups in the index of the input DataFrame and create separate DataFrames for each taxonomic level.

    Args:
        merged_df (pd.DataFrame): The input DataFrame with taxonomic groups in the index.

    Returns:
        dict: A dictionary with keys as taxonomic levels and values as the corresponding DataFrames.
    """

    levels = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']

    # Reset the index and split the index column into separate columns for each taxonomic level
    taxonomic_levels_df = merged_df.reset_index()
    taxonomic_split_df = taxonomic_levels_df['Taxon'].str.split('; ', expand=True)
    taxonomic_split_df = taxonomic_split_df.fillna('') # deals with cases of empty string instead of np.nan
    taxonomic_split_df.columns = levels

    # Concatenate genus and species names if both are present, otherwise leave species column unchanged
    taxonomic_split_df['Species'] = taxonomic_split_df.apply(
        lambda row: row['Genus'] + '_' + row['Species'] if row['Species'] != '' else row['Species'],
        axis=1
    )

    # Concatenate the taxonomic_split_df and the abundance data from taxonomic_levels_df
    taxonomic_levels_df = pd.concat([taxonomic_split_df, taxonomic_levels_df.iloc[:, 1:]], axis=1)

    # Initialize a dictionary to store DataFrames for each taxonomic level
    taxonomic_dfs = {}

    # Iterate through the taxonomic levels and create a DataFrame for each level
    for level in levels:
        level_df = taxonomic_levels_df[[level] + list(taxonomic_levels_df.columns[len(levels):])]
        level_df = level_df.rename(columns={level: 'Taxon'})

        # Set the 'Taxon' column as the index and remove rows with an empty string in the 'Taxon' column
        level_df = level_df.set_index('Taxon')
        level_df = level_df.loc[level_df.index != '']

        # Add the DataFrame to the dictionary
        taxonomic_dfs[level] = level_df

    return taxonomic_dfs

def rename_taxa(taxonomic_dfs):
    """
    Rename taxa in the taxonomic DataFrames by applying alterations, specific alterations, and homosynonyms.

    Args:
        taxonomic_dfs (dict): A dictionary with keys as taxonomic levels and values as the corresponding DataFrames.

    Returns:
        dict: A dictionary with keys as taxonomic levels and values as the renamed DataFrames.
    """

    resources_dir = os.path.join(os.path.dirname(__file__), 'resources')
    renaming_json_path = os.path.join(resources_dir, 'renaming.json')

    # Read the dictionaries from the JSON file
    with open(renaming_json_path, 'r') as f:
        loaded_dicts = json.load(f)

    # Access the dictionaries
    alterations, specific_alterations, homosynonyms = loaded_dicts

    renamed_dfs = {}

    for level, df in taxonomic_dfs.items():
        renamed_df = df.copy()

        # Apply alterations
        for pattern in alterations:
            renamed_df.index = renamed_df.index.str.replace(pattern, '', regex=True)

        # Apply specific alterations
        for pattern, replacement in specific_alterations.items():
            renamed_df.index = renamed_df.index.str.replace(pattern, replacement, regex=True)

        # Apply homosynonyms
        for pattern, replacement in homosynonyms.items():
            renamed_df.index = renamed_df.index.str.replace(pattern, replacement, regex=True)

        # Add the renamed DataFrame to the dictionary
        renamed_dfs[level] = renamed_df

    return renamed_dfs

def check_presence_in_agora2(dataframes):
    """
    Check if entries from the input DataFrames are in the AGORA2 DataFrame under the same level column.
    Split the input DataFrames into two DataFrames: present and absent. Renormalize both DataFrames.
    Add "pan" prefix to the index of the present DataFrame if the level is "Species".

    Args:
        dataframes (dict): A dictionary containing the input DataFrames to be checked against AGORA2.

    Returns:
        dict: A dictionary containing the present and absent DataFrames, renormalized, for each taxonomic level.
    """

    resources_dir = os.path.join(os.path.dirname(__file__), 'resources')
    agora2_path = os.path.join(resources_dir, 'AGORA2.parquet')

    agora2_df = pd.read_parquet(agora2_path)

    present_dataframes, absent_dataframes = {}, {}
    for level, input_df in dataframes.items():
        # Remove "_" from the index of the input DataFrame and find entries present in AGORA2
        present_mask = input_df.index.str.replace('_', ' ').isin(agora2_df[level])
        present_df = input_df.loc[present_mask]

        # Add "pan" prefix to the index of the present DataFrame if the level is "Species"
        if level == 'Species':
            present_df.index = 'pan' + present_df.index

        # Find entries absent in AGORA2
        absent_mask = ~present_mask
        absent_df = input_df.loc[absent_mask]

        # Renormalize both DataFrames
        present_df = present_df.div(present_df.sum(axis=0), axis=1)
        absent_df = absent_df.div(absent_df.sum(axis=0), axis=1)

        present_dataframes[level] = present_df
        absent_dataframes[level] = absent_df

    return present_dataframes, absent_dataframes
