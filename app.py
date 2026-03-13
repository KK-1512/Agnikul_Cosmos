import streamlit as st
import pickle
import numpy as np

# Load trained Random Forest model
model = pickle.load(open("compo.pkl", "rb"))

st.title("Composite Material Strength Prediction")

st.write("Predict tensile strength of Aluminium Matrix Composites using Machine Learning")

# Reinforcement type selection
reinforcement = st.selectbox(
    "Reinforcement Type",
    ["Al2O3", "B4C", "SiC"]
)

# Encode reinforcement type
reinforcement_map = {"Al2O3": 0, "B4C": 1, "SiC": 2}
reinforcement_encoded = reinforcement_map[reinforcement]

reinforcement_percent = st.slider("Reinforcement wt %", 0.5, 5.0, 1.0)

particle_size = st.slider("Particle Size (nm)", 20, 200, 50)

temperature = st.slider("Processing Temperature (°C)", 650, 780, 700)

stirring_speed = st.slider("Stirring Speed (rpm)", 300, 700, 400)

density = st.slider("Density (g/cm³)", 2.6, 2.9, 2.7)

hardness = st.slider("Hardness (HV)", 80, 180, 120)

wear_rate = st.slider("Wear Rate", 0.000001, 0.000008, 0.000003)

# Combine inputs
input_data = np.array([[reinforcement_encoded,
                        reinforcement_percent,
                        particle_size,
                        temperature,
                        stirring_speed,
                        density,
                        hardness,
                        wear_rate]])

# Prediction button
if st.button("Predict Tensile Strength"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Tensile Strength: {prediction[0]:.2f} MPa")
