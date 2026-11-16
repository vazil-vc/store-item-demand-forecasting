# 📈 Store Item Demand Forecasting

A Machine Learning project that predicts daily sales for different stores and items using historical sales data. The project includes data analysis, feature engineering, model training, a FastAPI backend, and a Streamlit frontend.

---

## 🚀 Features

- 📊 Exploratory Data Analysis (EDA)
- 🛠 Feature Engineering
- 🤖 Machine Learning Model Training
- 💾 Model Serialization using Joblib
- ⚡ FastAPI REST API for predictions
- 🎨 Streamlit Web Interface
- 📈 Real-time Sales Prediction

---

## 🧰 Tech Stack

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib

### Backend
- FastAPI
- Uvicorn
- Pydantic

### Frontend
- Streamlit
- Requests

### Visualization
- Matplotlib
- Seaborn

---

## 📂 Project Structure

```text
Store Item Demand Forecasting/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── predictor.py
│   └── schemas.py
│
├── frontend/
│   └── app.py
│
├── models/
│   └── sales_forecasting_model.pkl
│
├── dataset/
│
├── notebook/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

The dataset contains historical daily sales information.

| Feature | Description |
|---------|-------------|
| date | Sales date |
| store | Store ID (1–10) |
| item | Item ID (1–50) |
| sales | Daily sales (Target Variable) |

---

## 🔧 Feature Engineering

The following features were created from the original dataset:

### Date Features

- Year
- Month
- Day
- Quarter
- Is Weekend

### Time-Series Features

- Lag 1
- Lag 7
- Lag 30
- Rolling Mean 7
- Rolling Mean 30

---

## 🤖 Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Save Trained Model
9. Build FastAPI Backend
10. Build Streamlit Frontend

---

## 🌐 API Endpoint

### Home

```
GET /
```

Response

```json
{
    "message": "Sales Forecasting API"
}
```

---

### Predict Sales

```
POST /predict
```

Example Request

```json
{
    "store": 1,
    "item": 5,
    "year": 2018,
    "month": 1,
    "day": 15,
    "quarter": 1,
    "is_weekend": 0,
    "lag_1": 20,
    "lag_7": 18,
    "lag_30": 22,
    "rolling_mean_7": 19.5,
    "rolling_mean_30": 20.3
}
```

Example Response

```json
{
    "predicted_sales": 23.41
}
```

---

## 💻 Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/store-item-demand-forecasting.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI server

```bash
python -m uvicorn app.main:app --reload
```

API Documentation

```
http://127.0.0.1:8000/docs
```

### 4. Start Streamlit

```bash
streamlit run frontend/app.py
```

---

## 📸 Application

### FastAPI

- Interactive Swagger UI available at:

```
http://127.0.0.1:8000/docs
```

### Streamlit

Interactive interface for entering store information and viewing predicted sales.

---

## 📈 Future Improvements

- Automatic calculation of lag and rolling features
- Better UI/UX
- Model comparison (Linear Regression, Random Forest, XGBoost)
- Deployment using Docker
- Cloud deployment (Render/AWS)

---

## 👨‍💻 Author

**Muhammad Vazil V C**

- LinkedIn: https://www.linkedin.com/in/muhammad-vazil-v-c/
- GitHub: https://github.com/YOUR_GITHUB_USERNAME

---

## ⭐ If you found this project useful, consider giving it a star.