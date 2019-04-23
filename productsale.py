
# import matplotlib
# matplotlib.use('TkAgg')  # TkAgg
# import matplotlib.pyplot as plt
import pandas as pd
# import json
# import numpy as np

dataPath = './Data/'

# Load json data to dataframe
data = pd.read_json(dataPath+'20190207_transactions.json', orient='columns', lines=True)



