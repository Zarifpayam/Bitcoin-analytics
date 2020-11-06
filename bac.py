from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
feature_names = iris.feature_names

# features(X) and target(y) are already separated
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.DataFrame(iris.target, columns=['iris'])
X['iris']= y
df = pd.DataFrame(np.c_[iris['data'], iris['target']],columns= np.append(iris['feature_names'], ['target']))
#df = pd.DataFrame(data=np.c_[iris.data, iris.target], columns=iris.feature_names + ['target'])
df.to_csv(r'C:\Users\User\Desktop\wine22.csv', index = False)
#X.to_csv(r'C:\Users\User\Desktop\X.csv', index = False)
