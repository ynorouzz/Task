
# import matplotlib
# matplotlib.use('TkAgg')  # TkAgg
# import matplotlib.pyplot as plt
import pandas as pd
# import json
# import numpy as np

dataPath = './Data/'

# Load json data to dataframe
data = pd.read_json(dataPath+'20190207_transactions.json', orient='columns', lines=True)

# Select product ids
products = pd.DataFrame(data["products"].tolist())

# Print frequency of products
print(' How many times a product  \n', products.count())

################################ 
# Extend to multiple json files
################################

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

    return data_sef_df, products


data_sef_df, products = integrate_data(dataPath)
#  Print frequency of products
print(' How many times a product  \n', products.count())
