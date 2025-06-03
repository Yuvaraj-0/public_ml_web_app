#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 21:23:28 2025

@author: yuvaraj
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Load the models
diabetes_path = os.path.join(current_dir, 'diabetes_prediction.sav')
heart_path = os.path.join(current_dir, 'heart_disease_model.sav')
parkinsons_path = os.path.join(current_dir, 'parkinsons_model.sav')

# Load the models
diabetes_model = pickle.load(open(diabetes_path, 'rb'))
heart_disease_model = pickle.load(open(heart_path, 'rb'))
parkinsons_model = pickle.load(open(parkinsons_path, 'rb'))
# Load the models

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        menu_title='Multiple Disease Prediction System',
        options=['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson Prediction'],
        default_index=0)

if (selected == 'Diabetes Prediction'):
    st.title('Diabetes predcition suing ML')
    Pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, step=1)
    Glucose = st.number_input('Glucose', min_value=0, max_value=300)
    BloodPressure = st.number_input('Blood Pressure', min_value=0, max_value=200)
    SkinThickness = st.number_input('Skin Thickness', min_value=0, max_value=100)
    Insulin = st.number_input('Insulin', min_value=0, max_value=900)
    BMI = st.number_input('BMI', min_value=0.0, max_value=70.0, format="%.2f")
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=3.0, format="%.3f")
    Age = st.number_input('Age', min_value=0, max_value=120, step=1)

if st.button('Predict'):
    input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
    prediction = diabetes_model.predict([input_data])

    if prediction[0] == 1:
        st.success('The person is likely to have diabetes.')
    else:
        st.success('The person is unlikely to have diabetes.')

  
if selected == 'Heart Disease Prediction':
    st.subheader('Heart Disease Prediction')

    Age = st.number_input('Age', 0, 120, 0)
    Sex = st.number_input('Sex (1 = male; 0 = female)', 0, 1, 0)
    Cp = st.number_input('Chest Pain Type (0-3)', 0, 3, 0)
    Trestbps = st.number_input('Resting Blood Pressure', 0, 300, 0)
    Chol = st.number_input('Serum Cholesterol (mg/dl)', 0, 600, 0)
    Fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', 0, 1, 0)
    Restecg = st.number_input('Resting ECG results (0-2)', 0, 2, 0)
    Thalach = st.number_input('Max Heart Rate Achieved', 0, 250, 0)
    Exang = st.number_input('Exercise Induced Angina (1 = yes; 0 = no)', 0, 1, 0)
    Oldpeak = st.number_input('ST depression induced by exercise', 0.0, 10.0, 0.0)
    Slope = st.number_input('Slope of the peak exercise ST segment (0-2)', 0, 2, 0)
    Ca = st.number_input('Number of major vessels (0-4) colored by fluoroscopy', 0, 4, 0)
    Thal = st.number_input('Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect)', 1, 3, 1)

    if st.button('Predict Heart Disease'):
        input_data = [Age, Sex, Cp, Trestbps, Chol, Fbs, Restecg, Thalach, Exang, Oldpeak, Slope, Ca, Thal]
        prediction = heart_disease_model.predict([input_data])
        st.success('Heart Disease Positive' if prediction[0] == 1 else 'Heart Disease Negative')
if (selected == 'Parkinson Prediction'):
    st.title('Parkinson Prediction')
    MDVP_Fo = st.number_input('MDVP:Fo(Hz)', format="%.6f")
    MDVP_Fhi = st.number_input('MDVP:Fhi(Hz)', format="%.6f")
    MDVP_Flo = st.number_input('MDVP:Flo(Hz)', format="%.6f")
    MDVP_Jitter_percent = st.number_input('MDVP:Jitter(%)', format="%.6f")
    MDVP_Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', format="%.6f")
    MDVP_RAP = st.number_input('MDVP:RAP', format="%.6f")
    MDVP_PPQ = st.number_input('MDVP:PPQ', format="%.6f")
    Jitter_DDP = st.number_input('Jitter:DDP', format="%.6f")
    MDVP_Shimmer = st.number_input('MDVP:Shimmer', format="%.6f")
    MDVP_Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', format="%.6f")
    Shimmer_APQ3 = st.number_input('Shimmer:APQ3', format="%.6f")
    Shimmer_APQ5 = st.number_input('Shimmer:APQ5', format="%.6f")
    MDVP_APQ = st.number_input('MDVP:APQ', format="%.6f")
    Shimmer_DDA = st.number_input('Shimmer:DDA', format="%.6f")
    NHR = st.number_input('NHR', format="%.6f")
    HNR = st.number_input('HNR', format="%.6f")
    RPDE = st.number_input('RPDE', format="%.6f")
    DFA = st.number_input('DFA', format="%.6f")
    spread1 = st.number_input('spread1', format="%.6f")
    spread2 = st.number_input('spread2', format="%.6f")
    D2 = st.number_input('D2', format="%.6f")
    PPE = st.number_input('PPE', format="%.6f")
 
    if st.button('Predict Parkinson'):
        input_data = [
            MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter_percent, MDVP_Jitter_Abs, MDVP_RAP,
            MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5,
            MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE
        ]
        prediction = parkinsons_model.predict([input_data])
        st.success('Parkinson Disease Positive' if prediction[0] == 1 else 'Parkinson Disease Negative')
