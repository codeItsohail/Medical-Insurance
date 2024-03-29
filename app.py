from flask import Flask,render_template, url_for, request
from flask import jsonify
from utils import MedicalInsurance
import config
import pandas as pd
import json

# Initialize Flask Application
app = Flask(__name__)

# Load the dataset to get dropdown options
# dataset = pd.read_csv(r'data\medical_insurance.csv')

with open(config.CATEGORICAL_COL , 'r') as f:
    categorical_col_data = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/gender_options')
def gender_options():

    return jsonify(categorical_col_data['gender'])

@app.route('/api/children_options')
def children_options():
    # children_column = dataset['children']
    
    # # Handle non-numeric values or missing values
    # try:
    #     children_values = list(map(int, children_column.dropna().unique()))
    # except ValueError:
    #     return jsonify({"error": "Invalid or non-numeric values in the 'children' column."})

    return jsonify(categorical_col_data['children'])

# @app.route('/api/filtered_children_options')
# def filtered_children_options():
#     children_column = dataset['children']
    
#     try:
#         children_values = list(map(int, children_column.dropna().unique()))
#     except ValueError:
#         return jsonify({"error": "Invalid or non-numeric values in the 'children' column."})

#     return jsonify(children_values)

@app.route('/api/smoker_options')
def smoker_options():
    # return jsonify(list(dataset['smoker'].unique()))
    return jsonify(categorical_col_data['smoker'])

@app.route('/api/region_options')
def region_options():
    # return jsonify(list(dataset['region'].unique()))
    return jsonify(categorical_col_data['region'])


@app.route('/api/predict', methods=['POST'])
def predict():
    # data = request.get_json()

    # Preprocess the input data
    age = request.form.get('age')
    bmi = request.form.get('bmi')
    gender = request.form.get('gender')
    children = eval(request.form.get('children'))
    smoker = request.form.get('smoker')
    region = request.form.get('region')

    med_ins = MedicalInsurance()
    prediction = med_ins.get_predicted_charges(age,gender,bmi,children,smoker,region)
    # Make the prediction
  
    return jsonify({'prediction': prediction[0]})


if __name__ == "__main__":

    app.run(host='0.0.0.0',port=7070,debug=False)