import pandas as pd
import numpy as np

def run():
    df = pd.read_csv('../data/sales_data.csv')
    print(df.head())