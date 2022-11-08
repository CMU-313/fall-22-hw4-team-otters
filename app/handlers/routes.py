import this
from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np
import os

def configure_routes(app):

    this_dir = os.path.dirname(__file__)
    model_path = os.path.join(this_dir, "model.pkl")
    clf = joblib.load(model_path)

    @app.route('/')
    def hello():
        return "try the predict route it is great!"

    attributes = [
        { 'health': 0, 'absences': 0, 'age': 0, 'failures': 0, 'Dalc': 0, 'internet_int': 0, 
          'higher_int': 0, 'paid_int': 0, 'studytime': 0, 'address_int': 0 }
    ]

    @app.route('/applicants', methods=['GET', 'POST'])
    def applicants():
        if request.method == "GET":
            return jsonify(attributes[-1]), 200
        if request.method == "POST":
            result = {}
            applicant = request.get_json()
            if ('health' in applicant and 'absences' in applicant and 'age' in applicant 
            and 'failures' in applicant and 'Dalc' in applicant and 'internet_int' in applicant 
            and 'higher_int' in applicant and 'paid_int' in applicant and 'studytime' in applicant
            and 'address_int' in applicant):
                result['health'] = applicant['health']
                result['absences'] = applicant['absences']
                result['age'] = applicant['age']
                result['failures'] = applicant['failures']
                result['Dalc'] = applicant['Dalc']
                result['internet_int'] = applicant['internet_int']
                result['higher_int'] = applicant['higher_int']
                result['paid_int'] = applicant['paid_int']
                result['studytime'] = applicant['studytime']
                result['address_int'] = applicant['address_int']
                attributes.append(result)
                return jsonify(attributes[-1]), 200
            else:
                return "Invalid input: dictionary should contain 'health', 'absences', 'age', 'failures', \
                    'Dalc', 'internet_int', 'higher_int', 'paid_int', 'studytime', and 'address_int' attributes.", 400


    @app.route('/predict', methods=['GET'])
    def predict():
        #use entries from the query string here but could also use json
        query_df = pd.DataFrame({
            'health': pd.Series(attributes[-1]['health']),
            'absences': pd.Series(attributes[-1]['absences']),
            'age': pd.Series(attributes[-1]['age']),
            'failures': pd.Series(attributes[-1]['failures']),
            'Dalc': pd.Series(attributes[-1]['Dalc']),
            'internet_int': pd.Series(attributes[-1]['internet_int']),
            'higher_int': pd.Series(attributes[-1]['higher_int']),
            'paid_int': pd.Series(attributes[-1]['paid_int']),
            'studytime': pd.Series(attributes[-1]['studytime']),
            'address_int': pd.Series(attributes[-1]['address_int'])
        })
        query = pd.get_dummies(query_df)
        prediction = clf.predict(query)
        return jsonify(np.ndarray.item(prediction)), 200
