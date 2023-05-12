# -*- coding: utf-8 -*-
"""
Created on Fri May 12 20:08:01 2023

@author: saad4
"""

from flask import Flask, render_template, request
import joblib
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

pre_process = PolynomialFeatures(degree=3)

app = Flask(__name__, template_folder='templates')


@app.route('/')
def student():
    return render_template("index.html")


def ValuePredictor(to_predict_list):
    print(to_predict_list)
    to_predict = pre_process.fit_transform([to_predict_list])
    loaded_model = joblib.load('model.sav')
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = round(float(ValuePredictor(to_predict_list)), 2)
        return render_template("index.html", result=result)


if __name__ == '__main__':
    app.run(debug=False)