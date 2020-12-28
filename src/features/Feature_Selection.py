from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import chi2
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.graphics.api as smg
from sklearn.model_selection import train_test_split
import data

def Feature_select():
    data2 = data.create_data_object()
    target = data2.pop('pd')
    data2 = data2.fillna(method='bfill')

    #finding the optimal number of best features
    train_accuracy = []
    test_accuracy = []

        # apply SelectKBest F-score test to extract top n best features
    for n in np.arange(1, len(data2.columns)):
        bestfeatures = SelectKBest(score_func=f_classif, k = n)
        fit = bestfeatures.fit(data2, target)
        dfscores = pd.DataFrame(fit.scores_)
        dfcolumns = pd.DataFrame(data2.columns)

        #concat two dataframes for better visualization of the score function result
        featureScores = pd.concat([dfcolumns,dfscores],axis=1)
        featureScores.columns = ['Specs','Score']  #naming the dataframe columns
        featureScores = featureScores.nlargest(n,'Score')
        fs_variablies = list(featureScores['Specs'].values)
        data_fs = pd.DataFrame(data2[fs_variablies])

        #Drop one of the 2 features whose correlation is above 0.9
        corr_matrix=data_fs.corr().abs()
        mask=np.triu(np.ones_like(corr_matrix, dtype=bool))
        tri_df = corr_matrix.mask(mask)
        to_drop = [c for c in tri_df.columns if any(tri_df[c]>0.9)]
        data_fs = data_fs.drop(to_drop, axis=1)

        X = data_fs
        y = target

        (X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.25, random_state=1)
        lr = LogisticRegression()
        lr.fit(X_train, y_train)
        train_accuracy.append(lr.score(X_train, y_train))
        test_accuracy.append(lr.score(X_test, y_test))

    print(train_accuracy)
    Optimal_train_n = 1+train_accuracy.index(max(train_accuracy))
    print(Optimal_train_n)
    Optimal_test_n = 1+test_accuracy.index(max(test_accuracy))

    bestfeatures = SelectKBest(score_func=f_classif, k=Optimal_train_n)
    fit = bestfeatures.fit(data2, target)
    dfscores = pd.DataFrame(fit.scores_)
    dfcolumns = pd.DataFrame(data2.columns)

    # concat two dataframes for better visualization of the score function result
    featureScores = pd.concat([dfcolumns, dfscores], axis=1)
    featureScores.columns = ['Specs', 'Score']  # naming the dataframe columns
    featureScores = featureScores.nlargest(Optimal_train_n, 'Score')
    print(featureScores.nlargest(Optimal_train_n, 'Score'))  # print 10 best features.
    fs_variablies = list(featureScores['Specs'].values)
    data_fs = pd.DataFrame(data2[fs_variablies])



    return data_fs,target
