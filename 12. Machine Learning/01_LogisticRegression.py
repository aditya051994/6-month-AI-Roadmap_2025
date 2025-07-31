import pandas as pd
import numpy as np

dataframe=pd.read_csv(r'C:\DataScience-GenerativeAI-AgenticAI\Practical\DS-GenAi-AgenticAI-Bootcamp\6-month-AI-Roadmap_2025\6. Shared\logitic classification.csv')

## find dependent and independent 
X=dataframe.iloc[:,3:4]
y=dataframe['Purchased']

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.20,random_state=50)

##Feature Scaling
from sklearn.preprocessing import StandardScaler
standard_scaler=StandardScaler()
X_train=standard_scaler.fit_transform(X_train)
X_test=standard_scaler.transform(X_test)

#with normalizae 68%
#from sklearn.preprocessing import Normalizer
#normalize=Normalizer()
#X_train=normalize.fit_transform(X_train)
#X_test=normalize.fit_transform(X_test)

from sklearn.linear_model import LogisticRegression
logistic_regression=LogisticRegression()
logistic_regression.fit(X_train,Y_train)



y_pred=logistic_regression.predict(X_test)

compare_df=pd.DataFrame(
    {     'Actual Value': Y_test,
     'Predicted':y_pred
     }
    )

## Confusion Matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(Y_test,y_pred)
print(cm)


##Accuracy of model
from sklearn.metrics import accuracy_score
ac=accuracy_score(Y_test, y_pred)
print("accuracy",ac)

##Classification report
from sklearn.metrics import classification_report
class_report=classification_report(Y_test,y_pred)
print(class_report)


 


































