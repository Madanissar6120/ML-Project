
import streamlit as st
import pickle

st.set_page_config(page_title="Crop Recommendation System", page_icon="🌱")

@st.cache_resource
def load_model():
    with open("agriculture.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

st.title("🌱 Crop Recommendation System")

col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N)", min_value=0, max_value=150, value=50)
    P = st.number_input("Phosphorous (P)", min_value=0, max_value=150, value=50)
    K = st.number_input("Potassium (K)", min_value=0, max_value=210, value=50)
    temperature = st.number_input("Temperature (°C)", min_value=5.0, max_value=50.0, value=25.0)

with col2:
    humidity = st.number_input("Humidity (%)", min_value=10.0, max_value=100.0, value=60.0)
    ph = st.number_input("pH", min_value=1.0, max_value=9.0, value=6.5)
    rainfall = st.number_input("Rainfall (mm)", min_value=10.0, max_value=300.0, value=100.0)

if st.button("Predict Crop"):
    try:
        prediction = model.predict([[N, P, K, temperature, humidity, ph, rainfall]])
        st.success(f"Recommended Crop: {prediction[0]}")
    except Exception as e:
        st.error(f"Prediction Error: {e}")
