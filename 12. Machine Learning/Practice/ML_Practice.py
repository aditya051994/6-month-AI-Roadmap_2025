import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[8,9,7,10])
plt.ylabel('Number')
plt.xlabel('Age')
plt.show()
##-----------------------------------------------

import pandas as pd
import numpy as np

dataset=pd.read_csv(r'C:\DataScience-GenerativeAI-AgenticAI\Practical\DS-GenAi-AgenticAI-Bootcamp\6-month-AI-Roadmap_2025\6. Shared\Data_ML.csv')

X=dataset.iloc[:,0:3].values
y=dataset['Purchased'].values

from sklearn.impute import SimpleImputer
imputer=SimpleImputer(strategy='mean')

imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])

from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
encoder.fit(X[:,0])
X[:,0]=encoder.fit_transform(X[:,0])

y=encoder.fit_transform(dataset['Purchased'].values)


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2,random_state=0)





