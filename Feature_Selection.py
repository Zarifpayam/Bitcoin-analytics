from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import chi2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.graphics.api as smg
from sklearn.model_selection import train_test_split
import data

def Feature_select():
    data2 = data.create_data_object()
    target = data2.pop('pd')

    # apply SelectKBest Chi2 class to extract top 10 best features
    n = 7
    bestfeatures = SelectKBest(score_func=f_classif, k = n)
    print(bestfeatures)

    fit = bestfeatures.fit(data2, target)
    dfscores = pd.DataFrame(fit.scores_)
    dfcolumns = pd.DataFrame(data2.columns)

    # concat two dataframes for better visualization of the score function result
    featureScores = pd.concat([dfcolumns,dfscores],axis=1)
    featureScores.columns = ['Specs','Score']  #naming the dataframe columns
    featureScores = featureScores.nlargest(n,'Score')
    print(featureScores.nlargest(n,'Score'))  #print 10 best features.
    fs_variablies = list(featureScores['Specs'].values)
    data_fs = pd.DataFrame(data2[fs_variablies])

    return data_fs,target