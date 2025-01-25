import numpy as np
import pandas as pd


# write a function to read the csv file, if there is only one row or one column, return a list of the data, otherwise return and an empty list.
def read_csv(file_path: str):
    """read the csv file, if there is only one row or one column, return a list of the data, otherwise return and an empty list.

    Args:
        file_path (str): the path of the csv file.

    Returns:
        list : a list of the data in the csv file.
    """
    data = pd.read_csv(file_path)
    if data.shape[0] == 1:
        return data.values.tolist()[0]
    elif data.shape[1] == 1:
        return data.values.tolist()
    else:
        return []
    
# Convert table data in Markdown format to Excel format.
def markdown_to_excel(markdown: str, file_path: str):
    """Convert table data in Markdown format to Excel format.

    Args:
        markdown (str): the table data in Markdown format.
        file_path (str): the path of the Excel file.

    Returns:
        DataFrame: the table data in DataFrame format.
    """
    # Split the markdown data into rows.
    rows = markdown.strip().split('\n')
    # Split the rows into columns.
    # If the elements in the row are '----', it means the previous row is the header.
    if rows[1][1:5] == '----':
        header = rows[0].split('|')[1:-1]
        rows = rows[2:]
    # The following rows are the data.
    data = [row.split('|')[1:-1] for row in rows]
    # Create a DataFrame.
    df = pd.DataFrame(data, columns=header)
    # Save the DataFrame to an Excel file.
    df.to_excel(file_path, index=False)
    return df
    
    