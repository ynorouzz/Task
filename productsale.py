
import pandas as pd
from data_preprocessing import integrate_data

dataPath = './Data/'

################################ 
# Process single json file
################################

# Load json data to dataframe
data = pd.read_json(dataPath+'20190207_transactions.json', orient='columns', lines=True)

# Select product ids
products = pd.DataFrame(data["products"].tolist())

# Print frequency of products
print(' How many times a product  \n', products.count())

################################ 
# Extend to multiple json files
################################

data_sef_df, products = integrate_data(dataPath)

#  Print frequency of products
print(' How many times a product  \n', products.count())
