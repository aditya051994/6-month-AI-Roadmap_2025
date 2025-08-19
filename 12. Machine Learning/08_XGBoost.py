import pandas as pd
import numpy as np
dataset=pd.read_csv(r'C:\DataScience-GenerativeAI-AgenticAI\Practical\DS-GenAi-AgenticAI-Bootcamp\6-month-AI-Roadmap_2025\6. Shared\Churn_Modelling.csv')

X=dataset.iloc[:,3:-1].values
y=dataset.iloc[:,-1].values


#Label Encoding
from sklearn.preprocessing import LabelEncoder
LE=LabelEncoder()
X[:,2]=LE.fit_transform(X[:,2])


#To hide city names we encodes this with onHotEncoding
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct=ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[1])],remainder="passthrough")
X=np.array(ct.fit_transform(X))

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2,random_state=0)

#XG boost
from xgboost import XGBClassifier
classifier = XGBClassifier() 
classifier.fit(X_train, Y_train)

