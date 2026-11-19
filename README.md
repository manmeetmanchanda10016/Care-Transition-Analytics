# 📊 Care Transition Efficiency & Placement Outcome Analytics

An interactive data analytics and time-series forecasting application designed to analyse historical trends in the population of children in HHS care and estimate future population levels.

Built using Python, Streamlit, Pandas, Plotly and Statistical Forecasting Models.

## 🚀 Project Overview

This project explores historical HHS care population patterns and examines relationships between children entering and leaving the care system.

It combines exploratory data analysis, statistical modelling and interactive visualizations to provide insights into aggregate population trends.

The application also provides a 30-day forecasting interface powered by a trained ARIMA model.

## 🎯 Objectives

- Analyse historical trends in the HHS care population.
- Examine relationships between CBP transfers, HHS discharges and population levels.
- Develop time-series forecasting models.
- Compare different statistical and machine-learning approaches.
- Generate 30-day population forecasts.
- Present results through an interactive Streamlit dashboard.

## 📂 Dataset

**Dataset:** HHS Unaccompanied Alien Children Program

The dataset includes:

- Date
- Children apprehended and placed in CBP custody
- Children in CBP custody
- Children transferred out of CBP custody
- Children in HHS Care
- Children discharged from HHS Care

The dataset contains aggregate observations rather than individual-level records.

## 🧠 Models Evaluated

The following models were evaluated:

- Linear Regression
- ARIMA
- SARIMA
- ARIMAX
- Holt Linear Trend
- Damped Trend

## 🏆 Model Performance

The best-performing model in the 30-day time-series cross-validation comparison was **ARIMA (3,1,3)**.

| Metric | Result |
|---|---:|
| MAE | 31.55 |
| RMSE | 37.98 |

The model comparison also includes ARIMA (2,1,1), Damped Trend, ARIMAX, Naive Forecast and Holt Linear Trend.

## 📊 Application Features

### 1. Dashboard
- Key population statistics
- Historical HHS population trends
- Important project insights
- Recent dataset observations

### 2. Data Analysis
- Historical trend visualization
- Correlation matrix
- Dataset exploration

### 3. Model Comparison
- MAE and RMSE comparison
- 30-day cross-validation results
- Rolling one-step evaluation results

### 4. Forecasting
- Trained ARIMA (3,1,3) model
- Adjustable forecast horizon
- Forecast visualization
- Confidence intervals
- Downloadable forecast results

### 5. About Project
- Project objectives
- Dataset information
- Model descriptions

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Programming |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Plotly | Interactive visualizations |
| Statsmodels | Time-series modelling |
| Scikit-learn | Machine learning experiments |
| Streamlit | Web application |
| Joblib | Model serialization |

## 📁 Project Structure

```text
Care-Transition-Analytics/
│
├── app.py
├── arima_331_model.pkl
├── HHS_Unaccompanied_Alien_Children_Program.csv
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/manmeetmanchanda10016/Care-Transition-Analytics.git
```

### 2. Navigate to the project directory

```bash
cd Care-Transition-Analytics
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## ☁️ Deployment

The application is designed for deployment using **Streamlit Community Cloud**.

The dataset and trained model are loaded automatically from the project files. Users do not need to upload the CSV or model manually.

## ⚠️ Limitations

- The dataset contains aggregate population counts, not individual-level placement records.
- The application cannot predict individual placement outcomes or sponsor reunification.
- The available dataset ends on December 21, 2025.
- Forecasts are based on the historical endpoint and do not represent live 2026 observations.
- The ARIMA (3,1,3) model order was selected using the full dataset, so its cross-validation performance may be optimistic.

## 🔮 Future Scope

- Incorporate more recent data.
- Improve structural change detection.
- Explore additional forecasting approaches.
- Improve prediction interval reliability.
- Develop more advanced interactive analytics.

## 👨‍💻 Author

**Manmeet Singh Manchanda**

Computer Science and Engineering

Thapar Institute of Engineering and Technology

GitHub: [manmeetmanchanda10016](https://github.com/manmeetmanchanda10016)

---

⭐ If you find this project interesting, consider starring the repository!