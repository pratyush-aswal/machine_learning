# Importing the required Libraries
import pandas as pd 
import numpy as np 
from apyori import apriori

# Loading the dataset
store_data = pd.read_csv('day1.csv')

# Checking the data
print(store_data)