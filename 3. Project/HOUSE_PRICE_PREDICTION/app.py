#We will create front end in flask
from flask import Flask, render_template, request
import pandas as pd
import pickle

app=Flask(__name__)

##Load model name
model_names=['LinearRegression']

models = {name: pickle.load(open(f'{name}.pkl', 'rb')) for name in model_names}

@app.route('/')
def index():
    return render_template('index.html', model_names=model_names)

@app.route('/predict', methods=['POST'])
def predict():
     model_name = request.form['model']
     input_data = {
        'Avg. Area Income': float(request.form['Avg. Area Income']),
        'Avg. Area House Age': float(request.form['Avg. Area House Age']),
        'Avg. Area Number of Rooms': float(request.form['Avg. Area Number of Rooms']),
        'Avg. Area Number of Bedrooms': float(request.form['Avg. Area Number of Bedrooms']),
        'Area Population': float(request.form['Area Population'])
     }
     input_df = pd.DataFrame([input_data])
     if model_name in models:
        model = models[model_name]
        #prediction = model.predict(input_df)[0]
        prediction = model.predict(input_df)
        return render_template('results.html', prediction=prediction, model_name=model_name)
     else:
        return jsonify({'error': 'Model not found'}), 400
        

if __name__ == '__main__':
    app.run(debug=True)
    
