import pandas as pd
import zipfile

# Read the csv file present in "../DataSet/data.csv"
DATA_FILE="../DataSet/data.zip"
id1=""
id2="0000"

data=pd.read_csv(DATA_FILE,compression='zip')
pd.set_option('display.max_rows', data.shape[0]+1)

print(data.size)