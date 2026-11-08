
import streamlit as st
import joblib
import pandas as pd

# Load trained model
rf_model = joblib.load('rf_model.pkl')

# Page configuration
st.set_page_config(
    page_title="Water Potability Prediction",
    page_icon="💧",
    layout="centered"
)

st.title("💧 Water Potability Prediction")
st.write("Enter water quality values to predict whether water is potable or not.")

st.divider()

# Input fields
st.subheader("Water Quality Parameters")

ph = st.number_input("pH", value=7.0)
hardness = st.number_input("Hardness", value=200.0)
solids = st.number_input("Solids", value=20000.0)
chloramines = st.number_input("Chloramines", value=7.0)
sulfate = st.number_input("Sulfate", value=300.0)
conductivity = st.number_input("Conductivity", value=400.0)
organic_carbon = st.number_input("Organic Carbon", value=10.0)
trihalomethanes = st.number_input("Trihalomethanes", value=60.0)
turbidity = st.number_input("Turbidity", value=4.5)

# Prediction button
if st.button("Predict Water Quality", use_container_width=True):

    input_data = pd.DataFrame([[
        ph,
        hardness,
        solids,
        chloramines,
        sulfate,
        conductivity,
        organic_carbon,
        trihalomethanes,
        turbidity
    ]], columns=[
        'ph',
        'Hardness',
        'Solids',
        'Chloramines',
        'Sulfate',
        'Conductivity',
        'Organic_carbon',
        'Trihalomethanes',
        'Turbidity'
    ])

    prediction = rf_model.predict(input_data)

    st.divider()
    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.success("Water is Potable")
    else:
        st.error("Water is Not Potable")
