import streamlit as st
import requests

st.set_page_config(
    page_title="Sales Forecasting",
    page_icon="📈",
    layout="centered"
)

st.title("📈 Store Item Demand Forecasting")

st.write("Enter the details below.")

col1, col2 = st.columns(2)

with col1:
    store = st.number_input("Store", 1, 10)

with col2:
    item = st.number_input("Item", 1, 50)

col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Year", value=2018)

with col2:
    month = st.number_input("Month", 1, 12)

col1, col2 = st.columns(2)

with col1:
    day = st.number_input("Day", 1, 31)

with col2:
    quarter = st.number_input("Quarter", 1, 4)

st.divider()

st.subheader("📊 Historical Features")

weekend = st.selectbox(
    "Weekend",
    ["No", "Yes"]
)

is_weekend = 1 if weekend == "Yes" else 0

col1, col2 = st.columns(2)

with col1:
    lag_1 = st.number_input("Lag 1")

with col2:
    lag_7 = st.number_input("Lag 7")

col1, col2 = st.columns(2)

with col1:
    lag_30 = st.number_input("Lag 30")

with col2:
    rolling_mean_7 = st.number_input("Rolling Mean 7")

rolling_mean_30 = st.number_input("Rolling Mean 30")

predict_button = st.button(
    "🚀 Predict Sales",
    use_container_width=True
)
if predict_button:

    data = {
        "store": store,
        "item": item,
        "year": year,
        "month": month,
        "day": day,
        "quarter": quarter,
        "is_weekend": is_weekend,
        "lag_1": lag_1,
        "lag_7": lag_7,
        "lag_30": lag_30,
        "rolling_mean_7": rolling_mean_7,
        "rolling_mean_30": rolling_mean_30
    }

    try:
        with st.spinner("Predicting..."):
            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json=data
            )

            response.raise_for_status()

            result = response.json()
            prediction = result["predicted_sales"]

        st.divider()
        st.subheader("📈 Prediction")

        st.metric(
            label="Predicted Sales",
            value=f"{prediction:.2f} Units"
        )

    except Exception:
        st.error("❌ Could not connect to FastAPI. Make sure the backend is running.")
