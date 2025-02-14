import pandas as pd

def filter_expenses(expense_df, start_date=None, end_date=None):
    """
    Filters the expense DataFrame based on the provided criteria.

    Parameters:
    - expense_df (pd.DataFrame): The DataFrame containing expense records.
    - start_date (str): The start date (YYYY-MM-DD) for the filter range (inclusive).
    - end_date (str): The end date (YYYY-MM-DD) for the filter range (inclusive).
    - category (str): The category to filter by.
    - min_amount (float): The minimum amount for the filter range.
    - max_amount (float): The maximum amount for the filter range.

    Returns:
    - pd.DataFrame: A DataFrame containing the filtered expenses.
    """
    filtered_df = expense_df.copy()

    if start_date:
        filtered_df = filtered_df[filtered_df['date'] >= start_date]
    if end_date:
        filtered_df = filtered_df[filtered_df['date'] <= end_date]


    return filtered_df
