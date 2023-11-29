# dropping irrelevant columns from the dataframe
def drop_irrelevant_columns(input_df):
    """
    Removes irrelevant columns from a Pandas DataFrame.

    Args:
        input_df (pd.DataFrame): The input DataFrame containing irrelevant columns.

    Returns:
        pd.DataFrame: A new DataFrame with irrelevant columns removed.
    """
    dtv2 = input_df.drop(columns=["id", "Unnamed: 32"])
    return dtv2
