import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("study_planner_model.pkl")

# Title
st.title("AI Study Planner")
st.write("Predict your focus level based on your study schedule and energy.")

# User inputs
start_hour= st.number_input("Start Hour(0-23)", min_value=0, max_value=23, value=18)
end_hour= st.number_input("End Hour(0-23)", min_value=0, max_value=23, value=20)
energy_level = st.slider("Energy Level (1-5)", min_value=1, max_value=5, value=3)

# Prediction button
# if st.button("Predict Focus Level"):
#     input_data = pd.DataFrame({
#         'start_hour': [start_hour],
#         'end_hour': [end_hour],
#         'energy_level': [energy_level]
#     })
#     prediction = model.predict(input_data)
#     st.success(f"Predicted Focus Level: {prediction[0]:.2f} / 5")

from calendar_helper import create_event

if st.button("Predict Focus Level", key="focus_button"):
    input_data = pd.DataFrame({
        'start_hour': [start_hour],
        'end_hour': [end_hour],
        'energy_level': [energy_level]
    })
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Focus Level: {prediction:.2f} / 5")

    if prediction >= 4.0:
        if st.button("Add to Google Calendar"):
            create_event(start_hour, end_hour)
            st.info("Study session added to your Google Calendar!")

import datetime

if st.button("Add to Google Calendar", key="calendar_button"):
    now = datetime.datetime.now()
    start_time = (now + datetime.timedelta(days=1)).replace(hour=10, minute=0).isoformat()
    end_time = (now + datetime.timedelta(days=1)).replace(hour=12, minute=0).isoformat()

    link = create_event(
        summary="📚 Study Session",
        start_time=start_time,
        end_time=end_time,
        description="Scheduled by AI Study Planner"
    )
    st.success(f"Event created! [Open in Google Calendar]({link})")
