import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.graphics.api as smg
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, classification_report, confusion_matrix
from sklearn.metrics import roc_auc_score
import data_utils
import data
import Feature_Selection

def main():
    data_fs,target = Feature_Selection.Feature_select()
 #   print(data2.info())
    data_fs = data_fs.fillna(method='bfill')

    #correltaion analysis
    columns_names = pd.Series(data_fs.columns)
    smg.plot_corr(data_fs.corr(), xnames=columns_names)

    pd.plotting.scatter_matrix(data_fs, marker='O')

    #Drop one of the 2 features whose correlation is above 0.9
    corr_matrix=data_fs.corr().abs()
    mask=np.triu(np.ones_like(corr_matrix, dtype=bool))
    tri_df = corr_matrix.mask(mask)
    to_drop = [c for c in tri_df.columns if any(tri_df[c]>0.9)]
    data_fs = data_fs.drop(to_drop, axis=1)

    X = data_fs
    y = target

    (X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.20, random_state=1)
    lr = LogisticRegression()
    lr.fit(X_train, y_train)
    y_pred = lr.predict(X_test)
    y_prob = lr.predict_proba(X_test)[:1]
    # fpr,tpr,thresholds  = roc_curve(y_test,y_prob)

    print(confusion_matrix(y_test,y_pred))
    print(classification_report(y_test,y_pred))
    # print(roc_auc_score(y_test,y_prob))
    print(f"\n train accuracy: {lr.score(X_train, y_train)}\n")
    print(f"test accuracy: {lr.score(X_test, y_test)}\n")
    print(f"Intercept per class: {lr.intercept_}\n")
    print(f"Coeficients per class: {lr.coef_}\n")
    print(f"Available classes: {lr.classes_}\n")
    print(f"Named Coeficients for class 1: {pd.DataFrame(lr.coef_[0], data_fs.columns)}\n")
    print(f"Number of iterations generating model: {lr.n_iter_}")
    # print(fpr)
main()
