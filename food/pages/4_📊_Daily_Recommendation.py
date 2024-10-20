# pages/4_📊_Daily_Recommendation.py

import streamlit as st
from utils import format_number

st.title("Daily Calorie Recommendation 📊")

# User inputs
age = st.number_input("Enter your age:", min_value=1, max_value=120, value=25)
gender = st.selectbox("Select your gender:", options=["Male", "Female"])
weight = st.number_input("Enter your weight (kg):", min_value=1.0, max_value=300.0, value=70.0)
height = st.number_input("Enter your height (cm):", min_value=50.0, max_value=250.0, value=170.0)
activity_level = st.selectbox("Select your activity level:", options=[
    "Sedentary (little or no exercise)",
    "Lightly active (light exercise/sports 1-3 days/week)",
    "Moderately active (moderate exercise/sports 3-5 days/week)",
    "Very active (hard exercise/sports 6-7 days a week)",
    "Extra active (very hard exercise/sports & physical job)"
])
weight_goal = st.selectbox("Select your weight goal:", options=[
    "Lose weight",
    "Maintain current weight",
    "Gain muscle weight"
])

def calculate_bmr(gender, weight, height, age):
    if gender == "Male":
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

def calculate_daily_calories(bmr, activity_level):
    activity_multipliers = {
        "Sedentary (little or no exercise)": 1.2,
        "Lightly active (light exercise/sports 1-3 days/week)": 1.375,
        "Moderately active (moderate exercise/sports 3-5 days/week)": 1.55,
        "Very active (hard exercise/sports 6-7 days a week)": 1.725,
        "Extra active (very hard exercise/sports & physical job)": 1.9
    }
    return bmr * activity_multipliers[activity_level]

def calculate_daily_total_fat(daily_calories):
    st.write((daily_calories * 0.30) / 9 + " g")

def calculate_daily_saturated_fat(daily_calories):
    st.write((daily_calories * 0.6) / 9 + " g")

def calculate_daily_trans_fat(daily_calories):
    st.write((daily_calories * 0.01) / 9 + " g")

def calculate_daily_cholesterol():
    st.write(300 + " mg")

def calculate_daily_sodium():
    st.write(2300 + " mg")

def calculate_daily_total_carbohydrates(daily_calories):
    st.write((daily_calories * 0.50) / 4 + " mg")

def calculate_dietary_fiber():
    st.write(27.5 + " g")

def calculate_total_sugars(daily_calories):
    st.write((daily_calories * 0.05) / 4 + " g")

def calculate_total_protein(body_weight, weight_goal):
    if weight_goal == "Lose weight":
        st.write(body_weight * 0.8 + " g")
    
    if weight_goal == "Maintain current weight":
        st.write(body_weight * 1.0 + " g")

    if weight_goal == "Gain muscle weight":
        st.write(body_weight * 1.2 + " g")

if st.button("Calculate Recommended Daily Calories"):
    bmr = calculate_bmr(gender, weight, height, age)
    daily_calories = calculate_daily_calories(bmr, activity_level)
    calculate_daily_total_fat(daily_calories)
    calculate_daily_saturated_fat(daily_calories)
    calculate_daily_trans_fat(daily_calories)
    calculate_daily_cholesterol()
    calculate_daily_sodium()
    calculate_daily_total_carbohydrates(daily_calories)
    calculate_daily_dietary_fiber()
    calculate_daily_total_sugars(daily_calories)
    calculate_daily_total_protein(weight, weight_goal)
    st.write(f"**Your Recommended Daily Calorie Intake:** {daily_calories:.2f} kcal")
