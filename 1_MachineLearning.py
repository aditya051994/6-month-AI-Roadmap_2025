import pandas as pd
import numpy as np

data_set=pd.read_csv(r'C:\Users\a864911\Downloads\Data.csv')
data_set
X=data_set.iloc[:,:-1]
Y=data_set.iloc[:,-1:]

from sklearn.impute import SimpleImputer

imputer=SimpleImputer()

imputer=imputer.fit(X[:,1:3])
X[:, 1:3] = imputer.transform(X[:,1:3]) 













