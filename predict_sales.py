# This is a code for WebApp for predicting the sales.

import pickle
import streamlit as st
with open('sales_predictor.pickle', 'rb') as file:
    model = pickle.load(file)

print(model)

st.title('Sales Predictor')

TV = st.number_input(label ='Enter how many ads were broadcasted through TV: ')
radio = st.number_input(label = 'Enter how many ads were broadcasted through radio: ')
newspaper = st.number_input(label = 'Enter how many ads were posted in newspaper: ')


if st.button('Submit'):
    
    y_pred = model.predict([[TV, radio, newspaper]])
    st.write('Sales: ',y_pred[0])