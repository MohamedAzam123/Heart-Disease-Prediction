import streamlit as st 
import pandas as pd 
import numpy as np 
import pickle as pk
import os



data = pk.load(open(('heart_pred.sav'),'rb'))
scaler = pk.load(open(('heart_scaler.sav'),'rb'))

st.title('توقع الشخص مصاب بمرض القلب ام لا')




sex_map = {'m':1,'f':0}
ChestPainType_map = {'asy':0,'nap':2,'ata':1,'ta':3}
RestingECG_map = {'normal':1,'lvh':0,'st':2}
ExerciseAngina_map = {'n':0,'y':1}
ST_Slope_map = {'flat':1,'up':2,'down':0}

age = st.number_input('age')
sex = st.selectbox('gender',options=list(sex_map.keys()))
ChestPainType = st.selectbox('ChestPainType',options=list(ChestPainType_map.keys()))
RestingBP = st.number_input('RestingBP')
Cholesterol = st.number_input('Cholesterol')
FastingBS = st.selectbox('FastingBS',[0,1])
RestingECG = st.selectbox('RestingECG',options=list(RestingECG_map.keys()))
MaxHR = st.number_input('MaxHR')
ExerciseAngina = st.selectbox('ExerciseAngina',options=list(ExerciseAngina_map.keys()))
Oldpeak = st.number_input('Oldpeak')
ST_Slope = st.selectbox('ST_Slope',options=list(ST_Slope_map.keys()))

con = st.button('تحليل')

if con:
    input_data = [age,sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope]
    cols = ['Age','Sex','ChestPainType','RestingBP','Cholesterol','FastingBS','RestingECG','MaxHR','ExerciseAngina','Oldpeak','ST_Slope']
    df = pd.DataFrame([input_data], columns=cols)

    df['Sex'] = df['Sex'].map(sex_map)
    df['ChestPainType'] = df['ChestPainType'].map(ChestPainType_map)
    df['RestingECG'] = df['RestingECG'].map(RestingECG_map)
    df['ExerciseAngina'] = df['ExerciseAngina'].map(ExerciseAngina_map)
    df['ST_Slope'] = df['ST_Slope'].map(ST_Slope_map)

    new_data = scaler.transform(df)
    res = data.predict(new_data)

    if res == 0:
        st.success('معافى')
    else:
        st.error('مصاب')