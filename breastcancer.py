print('Breast cancer')
# testing everything out#

#import libraries and dependecies 
import pandas as pd 
from pathlib import Path 


#read the csv files into Data frames
breastcancer_path = Path('/Users/danish/Desktop/breast-cancer-analysis/breast+cancer+wisconsin+diagnostic/wdbc.data')
breastcancer = pd.read_csv(breastcancer_path, header=None)


#Display data
breastcancer.head()


