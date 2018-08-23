import pandas as pd
import warnings

warnings.simplefilter(action='ignore')

df = pd.read_csv('/home/praveen/Working_files/Category_Work/shuffle_cat_channel_meta.csv', header=None)

for row in df.values:
    print(row[2])