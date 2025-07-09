import numpy as np 	#Array		

import matplotlib.pyplot as plt		

import pandas as pd	

# IMPORT THE DATASET

dataset = pd.read_csv(r"C:\Users\a864911\Downloads\Data.csv")

# INDEPENDENT VARIABLE
X = dataset.iloc[:, :-1].values	
# DEPENDENT VARIABLE
y = dataset.iloc[:,3].values  

# SKLEARN FILL MISSING NUMERICAL VALUE
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy="most_frequent") 

imputer = imputer.fit(X[:,1:3]) 

X[:, 1:3] = imputer.transform(X[:,1:3]) 

from sklearn.preprocessing import LabelEncoder
labelEncoder_y=LabelEncoder()
labelEncoder_x=LabelEncoder()

Y=labelEncoder_y.fit_transform(y)
X[:,0]=labelEncoder_x.fit_transform(X[:,0])

from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

#Implement Stats using above dataset
#Mean
print(dataset.mean())




    










