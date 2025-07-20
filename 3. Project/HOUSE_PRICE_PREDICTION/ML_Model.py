import pandas as pd
from  sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle 

# We build this model for Linear Regression
df=pd.read_csv(r'C:\Users\a864911\OneDrive - ATOS\Desktop\GenAi+AgenticAI\Mechine Learning\HOUSING REGRESSOR\USA_Housing.csv')
#print(df.isnull().sum())

X=df.drop(columns=["Address","Price"])
y=df['Price']

X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2,random_state=0)

models={
    'LinearRegression':LinearRegression()
}

result=[]

#Loop on model
for name,model in models.items():
    model.fit(X_train,Y_train)  

    #Pickle model 
    with open(f'{name}.pkl', 'wb') as f:
        pickle.dump(model, f)  

print("Models have been trained and saved as pickle files. Evaluation results have been saved to model_evaluation_results.csv.")



