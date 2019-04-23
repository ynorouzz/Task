
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
product_id_counts = products.count()
print(' How many times a product  \n', product_id_counts)

# Get a product_id from the input
print('Enter the product id to find the number of sales:')
product_id = input()

# Search given product_id in product counts
found = search_product(product_id_counts, product_id)
if found:
    print('This product sold {0} times'.format(found))
else:
    print('Product id did not find')
