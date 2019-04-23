import glob
import pandas as pd


def integrate_data(dataPath):
    """
    Read json files from the directory and return data as dataframe

    :param dataPath: the relative path of json data files
    :return data_sef_df: a dataframe of json files with two columns (customer_id, list of product_ids)
            products: a dataframe that is extracted all product_ids from data_sef_df
    """
    data_set = []

    # List all json files
    data_files = glob.glob(dataPath + "*.json")

    # Concat json files into a list of dataframes
    for json_file in data_files:
        data = pd.read_json(json_file, orient='columns', lines=True)
        data_set.append(data)

    # Integrate dataframes into one dataframe
    data_sef_df = pd.concat(data_set)

    # Select product ids
    products = pd.DataFrame(data_sef_df["products"].tolist())
    
    # Convert column names from int to string    
    products.columns = products.columns.astype(str)

    return data_sef_df, products

def data_cleaning(df):
    """
    Remove columns and rows if all items are NULL
    :param df: input datafarme
    :return df: cleaned dataframe
    """
    df = df.dropna(how='all')
    
    return df


def search_product(df, product_id):
    """
    Search product_id in count of products
    :param df: product counts per product_id
    :param df: product_id as string
    """
    if product_id in df.index:

        return df[product_id]

    else:

        return -1
