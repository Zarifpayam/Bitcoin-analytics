import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import data_utils

def main():
    data = data_utils.create_data_object()

    target = data.pop('pd')
    data = data.fillna(method='ffill')
    columns_names = pd.Series(data.columns)
    print(columns_names)
    X = data
    Y = target
    print(f'Dataset X shape: {X.shape}')
    print(f'Dataset y shape: {Y.shape}')

    (X_train, X_test, y_train, y_test) = train_test_split(X, Y, test_size=0.35, random_state=1)
    lr = LogisticRegression()
    lr.fit(X_train, y_train)

    print(f"Intercept per class: {lr.intercept_}\n")
    print(f"Coeficients per class: {lr.coef_}\n")

    print(f"Available classes: {lr.classes_}\n")
    print(f"Named Coeficients for class 1: {pd.DataFrame(lr.coef_[0], columns_names)}\n")

    print(f"Number of iterations generating model: {lr.n_iter_}")

main()
