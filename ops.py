"""Helper functions.

@author Zhenye Na 05/21/2018

"""


# from tqdm import tqdm
# import matplotlib.pyplot as plt

import numpy as np
import pandas as pd


# import matplotlib
# matplotlib.use('Agg')

def read_data_nasdaq(input_path, debug=True):
    """
    Read nasdaq stocks data.

    Args:
        input_path (str): directory to nasdaq dataset.

    Returns:
        X (np.ndarray): features.
        y (np.ndarray): ground truth.

    """
    df = pd.read_csv(input_path, nrows=250 if debug else None)
    X = df.loc[:, [x for x in df.columns.tolist() if x != 'NDX']].to_numpy()
    y = np.array(df.NDX)

    return X, y

def read_data(input_path, debug=True):
    """Read nasdaq stocks data.

    Args:
        input_path (str): directory to nasdaq dataset.

    Returns:
        X (np.ndarray): features.
        y (np.ndarray): ground truth.

    """
    df = pd.read_csv(input_path)
    df_no_date = df.drop(["Close",'Date'], axis=1)
    X = df_no_date.values
    y = df['Close'].values
    return X, y
