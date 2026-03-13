import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("Compo.pkl", "rb"))

st.title("Aluminium Composite Strength Prediction")

st.write("Predict Tensile Strength of Aluminium Matrix Composites using Random Forest ML Model")

# Input features

reinforcement = st.selectbox(
    "Reinforcement Type",
    ["Al2O3", "B4C", "SiC"]
)

reinforcement_map = {"Al2O3": 0, "B4C": 1, "SiC": 2}
reinforcement_encoded = reinforcement_map[reinforcement]

reinforcement_percent = st.number_input("Reinforcement wt %", 0.5, 5.0, 1.0)

particle_size = st.number_input("Particle Size (nm)", 20, 200, 50)

temperature = st.number_input("Processing Temperature (°C)", 650, 780, 700)

stirring_speed = st.number_input("Stirring Speed (rpm)", 300, 700, 400)

density = st.number_input("Density (g/cm³)", 2.6, 2.9, 2.7)

hardness = st.number_input("Hardness (HV)", 80, 180, 120)

wear_rate = st.slider(
    "Wear Rate (mm³/Nm)",
    min_value=0.000001,
    max_value=0.000008,
    value=0.000003,
    step=0.000001
)

# Prediction button

if st.button("Predict Tensile Strength"):

    input_data = np.array([[reinforcement_encoded,
                            reinforcement_percent,
                            particle_size,
                            temperature,
                            stirring_speed,
                            density,
                            hardness,
                            wear_rate]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Tensile Strength: {prediction[0]:.2f} MPa")
