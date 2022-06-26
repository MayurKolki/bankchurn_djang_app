from django.shortcuts import render,request
from django.http import HttpResponse
from django import forms
import jsonify
import requests
import pickle
import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
model = pickle.load(open('C:/Users/mayur/Desktop/bank_churn_complete_module/bankchurn_logit_model.pkl','rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('C:/Users/mayur/Desktop/bank_churn_complete_module/templates/index.html')
standard_to = StandardScaler()

@app.route('/predict',methods=['POST'])
def predict(request):
   # return render(request, 'bankchurn_app/index.html')
   #Fuel_Type_Diesel=0
    if request.method == 'POST':
        creditscore = int(request.form['creditscore'])
        age = int(request.form['age'])
        tenure = int(request.form['tenure'])
        balance=float(request.form['balance'])
        salary=int(request.form['salary'])
        active=request.form['active']
        if(active=='active'):
                active=1
                
        else:
            active=0

        
        country_Germany=request.form['country_Germany']
        if(country_Germany=='yes'):
            country_Germany=1
        else:
            country_Germany=0	
        country_Spain=request.form['country_Spain']
        if(country_Spain=='yes'):
            country_Spain=1
        else:
            country_Spain=0
        gender_Male=request.form['gender_Male']
        if(gender_Male=='female'):
            gender_Male=0
        else:
            gender_Male=1



        prediction=model.predict([[creditscore,age,tenure,balance,salary,active,country_Germany,country_Spain,gender_Male]])
        output=round(prediction[0],2)
        if output<0.5:
            return render('C:/Users/mayur/Desktop/bank_churn_complete_module/templates/index.html',prediction_text="Sorry you are not eligible")
        else:
            return render('C:/Users/mayur/Desktop/bank_churn_complete_module/templates/index.html',prediction_text="you can get credit up to  {} thousands".format(output*100))
    else:
        return render('C:/Users/mayur/Desktop/bank_churn_complete_module/templates/index.html')

   # return HttpResponse("Hello, world. You're at the bankchurn_app index.")
