
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

data_set = []

# List all json files
data_files = glob.glob(dataPath + "*.json")

# Concat json files into a list of dataframes
for file in data_files:

    data = pd.read_json(dataPath + '20190207_transactions.json', orient='columns', lines=True)
    data_set.append(data)

# Integrate dataframes into one dataframe    
data_sef_df = pd.concat(data_set)

# Select product ids
products = pd.DataFrame(data_sef_df["products"].tolist())

# Print frequency of products
print(' How many times a product  \n', products.count())
