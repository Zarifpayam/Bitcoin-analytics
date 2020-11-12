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
    data2 = Feature_Selection.Feature_select()
 #   print(data2.info())
    target = data2.pop('pd')
    data2 = data2.fillna(method='bfill')
  #  print('data2info',data2.info())
    columns_names = pd.Series(data2.columns)
    smg.plot_corr(data2.corr(), xnames=columns_names)
    plt.show()

    X = data2
    y = target

    (X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.25, random_state=1)
    lr = LogisticRegression()
    lr.fit(X_train, y_train)
    y_pred = lr.predict(X_test)
    y_prob = lr.predict_proba(X_test)[:1]
    # fpr,tpr,thresholds  = roc_curve(y_test,y_prob)

    print(confusion_matrix(y_test,y_pred))
    print(classification_report(y_test,y_pred))
    # print(roc_auc_score(y_test,y_prob))
    print(f"\ntrain error: {lr.score(X_train, y_train)}\n")
    print(f"test error error: {lr.score(X_test, y_test)}\n")
    print(f"Intercept per class: {lr.intercept_}\n")
    print(f"Coeficients per class: {lr.coef_}\n")
    print(f"Available classes: {lr.classes_}\n")
    print(f"Named Coeficients for class 1: {pd.DataFrame(lr.coef_[0], columns_names)}\n")
    print(f"Number of iterations generating model: {lr.n_iter_}")
    # print(fpr)
main()
