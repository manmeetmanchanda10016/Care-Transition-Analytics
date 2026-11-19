# 📊 Care Transition Efficiency & Placement Outcome Analytics

### Data Analytics | Machine Learning | Time Series Forecasting | Streamlit

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)](https://pandas.pydata.org/)
[![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikitlearn)](https://scikit-learn.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?logo=plotly)](https://plotly.com/)

**🚀 [Explore Live Dashboard](https://care-transition-analytics-2jkqewg2ozdtjdyy8f8svx.streamlit.app/)** | **💻 [GitHub Repository](https://github.com/manmeetmanchanda10016/Care-Transition-Analytics)**

---

## 📌 Project Overview

**Care Transition Efficiency & Placement Outcome Analytics** is a data analytics and time-series forecasting project designed to explore historical trends in the U.S. Department of Health and Human Services (HHS) Unaccompanied Alien Children (UAC) Program.

The project analyzes aggregate population and movement data across different stages of the care transition process.

It combines exploratory data analysis, statistical analysis, machine learning, and time-series forecasting to understand historical patterns and evaluate forecasting approaches.

### 🎯 Key Objectives

- Analyze historical trends in the HHS care population.
- Explore relationships between CBP and HHS operational indicators.
- Identify significant changes in population patterns.
- Develop and compare machine learning models.
- Experiment with statistical time-series forecasting techniques.
- Evaluate models using chronological validation.
- Build and deploy an interactive Streamlit dashboard.

---

## 🖥️ Live Application

**Explore the deployed application:**

### [🚀 OPEN CARE TRANSITION ANALYTICS DASHBOARD](https://care-transition-analytics-2jkqewg2ozdtjdyy8f8svx.streamlit.app/)

The dashboard provides interactive visualizations, historical analysis, model comparisons, and forecasting functionality.

---

## 📑 Table of Contents

1. [Dataset](#-dataset)
2. [Project Workflow](#-project-workflow)
3. [Data Preprocessing](#-data-preprocessing)
4. [Exploratory Data Analysis](#-exploratory-data-analysis)
5. [Feature Engineering](#-feature-engineering)
6. [Techniques Used](#-techniques-used)
7. [Models Implemented](#-models-implemented)
8. [Model Evaluation](#-model-evaluation)
9. [Time Series Forecasting](#-time-series-forecasting)
10. [Interactive Dashboard](#-interactive-streamlit-dashboard)
11. [Technology Stack](#-technology-stack)
12. [Project Structure](#-project-structure)
13. [Installation and Setup](#-installation-and-setup)
14. [Limitations](#-limitations)
15. [Future Improvements](#-future-improvements)
16. [Author](#-author)

---

## 📂 Dataset

**Dataset:** HHS Unaccompanied Alien Children Program

**File:** `HHS_Unaccompanied_Alien_Children_Program.csv`

### Dataset Information

| Parameter | Value |
|---|---:|
| Original observations | 1,170 |
| Original columns | 6 |
| Observations after removing empty rows | 720 |
| Historical date range | Jan 12, 2023 – Dec 21, 2025 |
| Daily observations after interpolation | 1,075 |
| Target variable | Children in HHS Care |

### Dataset Features

| Feature | Description |
|---|---|
| Date | Observation date |
| Children apprehended and placed in CBP custody | Children entering CBP custody |
| Children in CBP custody | Children currently in CBP custody |
| Children transferred out of CBP custody | Children transferred from CBP custody |
| Children in HHS Care | Children currently in HHS care |
| Children discharged from HHS Care | Children discharged from HHS care |

---

## 🔄 Project Workflow

The project follows a structured data science workflow:

```mermaid
flowchart TD
    A["HHS Dataset"] --> B["Data Cleaning"]
    B --> C["Exploratory Data Analysis"]
    C --> D["Feature Engineering"]
    D --> E["Machine Learning Models"]
    D --> F["Time Series Analysis"]
    E --> G["Model Evaluation"]
    F --> G
    G --> H["Model Comparison"]
    H --> I["ARIMA Forecasting"]
    I --> J["Streamlit Dashboard"]
```

---

## 🧹 Data Preprocessing

The dataset underwent the following preprocessing steps:

1. Removed completely empty rows.
2. Converted the Date column into datetime format.
3. Sorted observations chronologically.
4. Converted comma-separated numerical values into numeric data types.
5. Checked for missing values and duplicate observations.
6. Created a daily time series using time-based interpolation.
7. Prepared chronological training and testing datasets.

**Important:** The original dataset contains irregularly spaced observations. Daily interpolation generates estimated values between recorded dates. These interpolated observations are not actual daily measurements.

---

## 📈 Exploratory Data Analysis (EDA)

Exploratory analysis was performed to understand population trends and relationships between operational indicators.

### Techniques Used

- Descriptive statistical analysis
- Time-series trend visualization
- Distribution analysis
- Correlation analysis
- Correlation heatmaps
- Rolling averages
- Historical population comparisons
- Before-and-after January 2025 comparison
- Welch's two-sample t-test

### Key Observations

- The HHS care population increased during parts of 2023 and early 2024.
- A substantial decline was observed around January 2025.
- Several operational indicators showed simultaneous changes.
- Discharges from HHS care showed a strong positive correlation with the HHS care population.

**Note:** Correlation does not imply causation. The dataset alone cannot establish the reason behind the observed population changes.

---

## ⚙️ Feature Engineering

Feature engineering was performed to capture historical patterns and temporal dependencies.

### Features Created

| Feature | Description |
|---|---|
| HHS_lag_1 | Previous observation |
| HHS_lag_2 | Population two observations earlier |
| HHS_lag_3 | Population three observations earlier |
| Rolling Mean 3 | Average of previous three observations |
| Rolling Mean 7 | Average of previous seven observations |
| CBP Indicators | Operational variables |
| Target | Next recorded HHS care population |

Rolling features were calculated using shifted values to avoid directly including the current target observation.

---

## 🧠 Techniques Used

### 1. Data Cleaning and Preprocessing

- Missing value analysis
- Duplicate detection
- Datetime conversion
- Numeric type conversion
- Time-based interpolation
- Chronological train-test splitting
- Median imputation
- Feature scaling using StandardScaler

### 2. Exploratory Data Analysis

- Descriptive statistics
- Correlation matrix
- Heatmaps
- Time-series visualization
- Rolling averages
- Distribution analysis
- Structural change exploration
- Welch's two-sample t-test

### 3. Statistical Time Series Analysis

- Augmented Dickey-Fuller (ADF) Test
- First-order differencing
- Autocorrelation Function (ACF)
- Partial Autocorrelation Function (PACF)
- Akaike Information Criterion (AIC)
- Ljung-Box Test
- Durbin-Watson Test
- Jarque-Bera Test
- Residual analysis
- Forecast confidence intervals

### 4. Model Validation and Optimization

- Chronological train-test split
- TimeSeriesSplit cross-validation
- GridSearchCV
- Hyperparameter tuning
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score
- Naive baseline comparison

---

## 🤖 Models Implemented

Multiple machine learning and statistical forecasting models were experimented with and evaluated.

### A. Machine Learning Models

| No. | Model | Library |
|---:|---|---|
| 1 | Linear Regression | Scikit-learn |
| 2 | Ridge Regression | Scikit-learn |
| 3 | Lasso Regression | Scikit-learn |
| 4 | Decision Tree Regressor | Scikit-learn |
| 5 | Random Forest Regressor | Scikit-learn |
| 6 | Extra Trees Regressor | Scikit-learn |
| 7 | Gradient Boosting Regressor | Scikit-learn |
| 8 | XGBoost Regressor | XGBoost |
| 9 | LightGBM Regressor | LightGBM |

### B. Statistical Time Series Models

| No. | Model | Configuration / Purpose |
|---:|---|---|
| 1 | Naive Forecast | Last observed value |
| 2 | ARIMA | Multiple candidate orders |
| 3 | ARIMA(2,1,1) | ARIMA experiment |
| 4 | ARIMA(3,1,3) | Selected forecasting model |
| 5 | SARIMA | (1,1,1) × (1,0,1,7) |
| 6 | ARIMAX | ARIMA with external variables |
| 7 | Auto-ARIMA | Automatic order selection |
| 8 | Holt Linear Trend | Exponential smoothing |
| 9 | Damped Holt Trend | Damped trend forecasting |

### C. Hyperparameter Optimization

Machine learning experiments included:

- GridSearchCV
- TimeSeriesSplit
- Multiple hyperparameter combinations
- MAE-based model selection

---

## 📊 Model Evaluation

Models were evaluated using different validation strategies. Results from different evaluation protocols should not be compared directly.

### 1. Machine Learning – Original Irregular Series

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 17.60 | 21.60 | 0.9849 |
| Ridge Regression | 38.30 | 42.43 | 0.9419 |
| Lasso Regression | 27.19 | 32.55 | 0.9658 |
| Decision Tree | 58.66 | 72.98 | 0.8281 |
| Random Forest | 56.87 | 73.32 | 0.8265 |
| Extra Trees | 57.22 | 73.03 | 0.8279 |
| Gradient Boosting | 69.65 | 87.55 | 0.7526 |
| XGBoost | 84.20 | 116.60 | 0.5611 |
| LightGBM | 70.25 | 92.05 | 0.7265 |

### 2. Time Series – Five-Fold Chronological Validation

The following results use 30-step open-loop test windows.

| Model | Average MAE | Average RMSE |
|---|---:|---:|
| ARIMA(3,1,3) | 31.55 | 37.98 |
| ARIMA(2,1,1) | 34.14 | 41.84 |
| Damped Holt | 35.71 | 45.25 |
| Holt Linear Trend | 84.32 | 98.09 |
| Naive Forecast | 60.07 | 71.11 |

### 3. Rolling One-Step Evaluation

| Model | MAE | RMSE |
|---|---:|---:|
| ARIMA(2,1,1) | 4.54 | 6.11 |
| Daily Linear Regression | 6.42 | 7.93 |
| SARIMA | 6.88 | 8.62 |
| ARIMAX with actual test exogenous variables | 3.96 | 5.12 |

**Evaluation Note:**

Rolling one-step evaluation updates predictions using actual observations as they become available. It is different from forecasting an entire future horizon without observing new data.

The ARIMAX rolling result also uses actual test-period external variables, which would not be available in advance for a real future forecast.

---

## 🔮 Time Series Forecasting

The deployed application uses an **ARIMA(3,1,3)** forecasting model.

The model was trained using the available historical daily HHS care population series.

### Forecasting Features

- 7-day forecast
- 14-day forecast
- 21-day forecast
- 30-day forecast
- User-selectable forecast horizon
- Forecast visualization
- Confidence intervals
- Historical versus predicted population comparison

### Forecasting Workflow

```mermaid
flowchart TD
    A["Historical HHS Care Data"] --> B["Daily Time Series"]
    B --> C["Fit ARIMA(3,1,3)"]
    C --> D["Generate Forecast"]
    D --> E["Calculate Confidence Intervals"]
    E --> F["Visualize Forecast"]
```

ARIMA(3,1,3) was selected after comparing candidate configurations and evaluating chronological validation performance.

**Model selection limitation:** The final ARIMA order was also selected using the full historical series, so its cross-validation performance may be optimistic.

---

## 🖥️ Interactive Streamlit Dashboard

The project includes a multi-page Streamlit application designed to make the analysis accessible through an interactive interface.

### Dashboard Pages

| Page | Functionality |
|---|---|
| Dashboard | Project overview and key indicators |
| Data Analysis | Historical trends and exploratory analysis |
| Model Comparison | Compare forecasting approaches and metrics |
| Forecasting | Generate forecasts for different horizons |
| About Project | Project methodology, scope, and details |

### Dashboard Features

- Dark-themed interface
- Interactive Plotly visualizations
- Historical trend exploration
- Model performance comparison
- User-selectable forecast horizon
- Forecast confidence intervals
- Automatically loaded dataset and saved model

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Manipulation | Pandas, NumPy |
| Visualization | Plotly, Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Gradient Boosting | XGBoost, LightGBM |
| Statistical Modeling | Statsmodels, pmdarima |
| Statistical Testing | SciPy |
| Dashboard | Streamlit |
| Model Persistence | Joblib |
| Deployment | Streamlit Community Cloud |
| Version Control | Git, GitHub |

---

## 📁 Project Structure

```text
Care-Transition-Analytics/
│
├── app.py
│
├── HHS_Unaccompanied_Alien_Children_Program.csv
│
├── arima_331_model.pkl
│
├── requirements.txt
│
└── README.md
```

---

## 🚀 Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/manmeetmanchanda10016/Care-Transition-Analytics.git
```

### 2. Navigate to the Project Directory

```bash
cd Care-Transition-Analytics
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## ⚠️ Limitations

- The dataset contains aggregate program-level observations, not individual-level records.
- It cannot predict individual placement outcomes, sponsor reunification, or individual case decisions.
- Daily observations created through interpolation are estimates, not independently recorded daily measurements.
- A substantial change around January 2025 may reflect operational or reporting changes; its cause cannot be determined from the available data.
- Future forecasts are based on historical patterns and may not account for policy, operational, or external changes.
- Forecast accuracy can vary depending on the validation method and forecast horizon.
- The historical dataset ends on December 21, 2025.
- The deployed model does not automatically incorporate newer observations.

---

## 🔭 Future Improvements

- Integrate regularly updated official datasets.
- Evaluate rolling-origin multi-horizon forecasting.
- Explore additional forecasting architectures.
- Add automated model retraining.
- Improve uncertainty quantification.
- Add more detailed model diagnostics.
- Develop monitoring for forecast performance over time.

---

## 👨‍💻 Author

### Manmeet Singh Manchanda

**Computer Science and Engineering**  
Thapar Institute of Engineering & Technology  
Thapar CSE – 2029 Batch

[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github)](https://github.com/manmeetmanchanda10016)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/manmeet-singh-manchanda-7b395a37)

---

⭐ **If you find this project interesting, consider giving the repository a star!**

**Built with Python, Machine Learning, Statistical Analysis, and Streamlit.**
