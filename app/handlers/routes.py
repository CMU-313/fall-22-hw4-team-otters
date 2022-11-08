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
        { 'age': 0, 'absences': 0, 'health': 0 }
    ]

    @app.route('/applicants', methods=['GET', 'POST'])
    def applicants():
        if request.method == "GET":
            return jsonify(attributes[-1]), 200
        if request.method == "POST":
            result = {}
            applicant = request.get_json()
            if 'age' in applicant and 'absences' in applicant and 'health' in applicant:
                result['age'] = applicant['age']
                result['absences'] = applicant['absences']
                result['health'] = applicant['health']
                attributes.append(result)
                return "Successfully added new applicant attributes: " + jsonify(attributes[-1]), 200
            else:
                return "Invalid input: dictionary should contain 'age', 'absences', and 'health' attributes", 400


    @app.route('/predict', methods=['GET'])
    def predict():
        query_df = pd.DataFrame({
            'age': pd.Series(attributes[-1]['age']),
            'health': pd.Series(attributes[-1]['health']),
            'absences': pd.Series(attributes[-1]['absences'])
        })
        query = pd.get_dummies(query_df)
        prediction = clf.predict(query)
        return jsonify(np.asscalar(prediction))
