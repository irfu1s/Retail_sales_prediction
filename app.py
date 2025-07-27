import streamlit as st
import pandas as pd
import pickle

# Load model
with open("xgboost_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page config
st.set_page_config(page_title="Retail Sales Prediction", layout="centered")
st.title("🛍️ Retail Sales Predictor")
st.write("Enter store and date details below to predict weekly sales.")

# Inputs
store_id = st.number_input("Store ID", min_value=1, max_value=45, value=1)
dept = st.number_input("Department", min_value=1, max_value=99, value=1)
year = st.number_input("Year", min_value=2010, max_value=2025, value=2012)
month = st.number_input("Month", min_value=1, max_value=12, value=1)
week = st.number_input("Week", min_value=1, max_value=52, value=1)
day = st.number_input("Day", min_value=1, max_value=31, value=1)
day_of_week = st.selectbox("Day of Week", [0, 1, 2, 3, 4, 5, 6])  # 0 = Monday
temperature = st.number_input("Temperature (°F)", value=70.0)
fuel_price = st.number_input("Fuel Price (USD)", value=3.0)
is_promo = st.checkbox("Promotion Active?", value=False)
size = st.number_input("Store Size (sqft)", value=150000)

# Store Type one-hot encoding
store_type = st.selectbox("Store Type", ['A', 'B', 'C'])
type_a = 1 if store_type == 'A' else 0
type_b = 1 if store_type == 'B' else 0
type_c = 1 if store_type == 'C' else 0

# Convert boolean to int
is_promo = int(is_promo)

# Final Input DataFrame
input_df = pd.DataFrame({
    "Store_ID": [store_id],
    "Dept": [dept],
    "Year": [year],
    "Month": [month],
    "Week": [week],
    "Day": [day],
    "DayOfWeek": [day_of_week],
    "Temperature": [temperature],
    "Fuel_Price": [fuel_price],
    "IsPromo": [is_promo],
    "Size": [size],
    "Type_A": [type_a],
    "Type_B": [type_b],
    "Type_C": [type_c]
})

# Predict
if st.button("Predict Weekly Sales"):
    try:
        prediction = model.predict(input_df)[0]
        st.success(f"📈 Predicted Weekly Sales: **${prediction:,.2f}**")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
