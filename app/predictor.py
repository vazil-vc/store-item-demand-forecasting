import joblib

model = joblib.load("models/sales_forecasting_model.pkl")


def predict_sales(df):
    prediction = model.predict(df)
    return prediction