# 📊 Care Transition Efficiency & Placement Outcome Analytics

### An Interactive Data Analytics & Time-Series Forecasting Platform

<p align="center">

**[🚀 Live Application](https://care-transition-analytics-2jkqewg2ozdtjdyy8f8svx.streamlit.app/)** · **[💻 GitHub Repository](https://github.com/manmeetmanchanda10016/Care-Transition-Analytics)**

</p>

---

## 🌐 Live Demo

**Explore the deployed application:**

[Care Transition Analytics – Streamlit App](https://care-transition-analytics-2jkqewg2ozdtjdyy8f8svx.streamlit.app/)

An interactive dashboard for exploring historical HHS care population trends, analysing relationships between operational variables, comparing forecasting models and generating population forecasts.

---

## 📌 Project Overview

Care Transition Efficiency & Placement Outcome Analytics is a data science project focused on analysing historical trends in the population of children in the U.S. Department of Health and Human Services (HHS) care system.

The project combines exploratory data analysis, statistical time-series modelling, machine-learning experiments and interactive data visualization to understand historical population patterns and estimate future aggregate population levels.

A trained ARIMA forecasting model is integrated into a Streamlit application, allowing users to generate forecasts through an interactive web interface.

**Primary objective:** Develop a data-driven forecasting framework for understanding and estimating aggregate HHS care population trends.

## 🎯 Project Objectives

- Analyse historical trends in children entering and leaving HHS care.
- Examine relationships between CBP transfers, HHS discharges and the HHS care population.
- Identify changes and structural patterns in historical population data.
- Develop statistical and machine-learning forecasting models.
- Compare models using appropriate time-series evaluation techniques.
- Generate 30-day population forecasts.
- Deploy an interactive analytics application using Streamlit.

---

## 📂 Dataset Description

**Dataset:** HHS Unaccompanied Alien Children Program

The dataset contains aggregate observations with the following variables:

| Feature | Description |
|---|---|
| Date | Observation date |
| Children apprehended and placed in CBP custody | Children entering CBP custody |
| Children in CBP custody | Children currently in CBP custody |
| Children transferred out of CBP custody | Children transferred out of CBP custody |
| Children in HHS Care | Aggregate population currently in HHS care |
| Children discharged from HHS Care | Children discharged from HHS care |

### Dataset Processing

The original dataset contained 1,170 rows, including 450 completely empty rows.

After removing fully empty rows:

- Remaining observations: 720
- Original observation period: January 12, 2023 – December 21, 2025
- Duplicate dates: None
- Missing values after cleaning: None

The original observations were irregularly spaced. A daily time series was subsequently constructed using time-based interpolation.

**Important:** The daily series is an interpolated representation of the original observations, not a dataset of independently recorded daily values.

---

## 🛠️ Technologies & Tools

| Technology | Application |
|---|---|
| Python | Core programming |
| Pandas | Data manipulation and preprocessing |
| NumPy | Numerical computation |
| Matplotlib | Statistical visualization |
| Plotly | Interactive charts and dashboards |
| Scikit-learn | Machine-learning models and evaluation |
| Statsmodels | Statistical time-series modelling |
| pmdarima | Automatic ARIMA order selection |
| Joblib | Saving and loading trained models |
| Streamlit | Interactive web application |
| Git & GitHub | Version control and project hosting |
| Streamlit Community Cloud | Application deployment |

---

## 🔬 Techniques & Methodologies

The project applies several data science and forecasting techniques.

### 1. Data Cleaning & Preprocessing

- Removal of completely empty rows.
- Date conversion and chronological sorting.
- Numeric conversion of population values containing commas.
- Missing-value inspection.
- Duplicate-date verification.
- Construction of a daily time series.
- Time-based interpolation of missing dates.
- Chronological train-test splitting.

### 2. Exploratory Data Analysis (EDA)

- Historical trend analysis.
- Time-series visualization.
- Descriptive statistics.
- Correlation analysis.
- Correlation heatmaps.
- Distribution analysis.
- Comparison of population levels across different periods.
- Investigation of potential structural changes.

### 3. Feature Engineering

For the machine-learning experiments, the following features were created:

**Lag Features**
- HHS Lag 1
- HHS Lag 2
- HHS Lag 3

**Rolling Statistics**
- Rolling Mean – 3 observations
- Rolling Mean – 7 observations

**Operational Variables**
- Children apprehended and placed in CBP custody.
- Children in CBP custody.
- Children transferred out of CBP custody.
- Children discharged from HHS care.

These features were used to capture historical population behaviour and relationships with operational variables.

### 4. Statistical Analysis

The following statistical techniques were applied:

- Augmented Dickey-Fuller (ADF) test for stationarity.
- First-order differencing.
- Autocorrelation Function (ACF).
- Partial Autocorrelation Function (PACF).
- Ljung-Box test for residual autocorrelation.
- Durbin-Watson statistic.
- Jarque-Bera residual normality test.
- Residual visualization and diagnostic analysis.
- Structural change investigation.

### 5. Model Optimization & Validation

- Chronological train-test split.
- TimeSeriesSplit cross-validation.
- GridSearchCV hyperparameter tuning.
- ARIMA order selection.
- Auto-ARIMA experimentation.
- Model convergence checks.
- Residual diagnostics.
- Rolling one-step evaluation.
- 30-day open-loop forecasting evaluation.

---

## 🤖 Models Implemented & Evaluated

The project compares statistical forecasting approaches and machine-learning regression models.

### A. Statistical Time-Series Models

| Model | Configuration / Approach |
|---|---|
| ARIMA | ARIMA(1,1,1), ARIMA(2,1,1), ARIMA(1,1,2), ARIMA(2,1,2), ARIMA(3,1,1), ARIMA(1,1,3), ARIMA(3,1,2) and ARIMA(3,1,3) experiments |
| SARIMA | SARIMA(1,1,1)(1,0,1,7) |
| ARIMAX | ARIMAX(3,1,3) with external variables |
| Auto-ARIMA | Automatic ARIMA order selection |
| Holt Linear Trend | Linear trend exponential smoothing |
| Damped Trend | Damped trend exponential smoothing |
| Naive Forecast | Last-observation baseline |

### B. Machine-Learning Regression Models

The following regression algorithms were evaluated:

1. Linear Regression
2. Ridge Regression
3. Lasso Regression
4. Decision Tree Regressor
5. Random Forest Regressor
6. Extra Trees Regressor
7. Gradient Boosting Regressor
8. XGBoost Regressor
9. LightGBM Regressor

### C. Model Optimization

Hyperparameter optimization was performed using:

- GridSearchCV
- TimeSeriesSplit
- Model-specific parameter grids
- MAE-based model selection

For linear models, preprocessing included median imputation and standardization using StandardScaler.

---

## 📊 Model Evaluation Metrics

The following metrics were used to assess forecasting performance:

| Metric | Purpose |
|---|---|
| MAE | Measures average absolute prediction error |
| RMSE | Penalizes larger prediction errors |
| R² Score | Measures explained variance relative to a baseline |
| Ljung-Box | Checks residual autocorrelation |
| Durbin-Watson | Examines residual autocorrelation |

Lower MAE and RMSE values indicate better predictive accuracy.

---

## 🏆 Model Performance Results

### 1. Thirty-Day Time-Series Cross-Validation

The following results represent 30-day forecasting evaluation using five chronological validation folds.

| Model | MAE | RMSE |
|---|---:|---:|
| ARIMA (3,1,3) | **31.55** | **37.98** |
| ARIMA (2,1,1) | 34.14 | 41.84 |
| Damped Trend | 35.71 | 45.25 |
| ARIMAX (Forecasted Exog) | 34.98 | 42.46 |
| Naive Forecast | 60.07 | 71.11 |
| Holt Linear Trend | 84.32 | 98.09 |

**Best-performing model:** ARIMA (3,1,3)

- MAE: 31.55
- RMSE: 37.98

ARIMA (3,1,3) achieved the lowest forecasting error among the compared 30-day models.

**Validation qualification:** Its order was selected using the full dataset before the five-fold evaluation. Consequently, the reported cross-validation performance may be optimistic. A separate fold-wise order-selection experiment was also performed.

### 2. Rolling One-Step Evaluation

| Model | MAE | RMSE |
|---|---:|---:|
| ARIMAX (Actual Exog) | **3.96** | **5.12** |
| ARIMA (2,1,1) | 4.54 | 6.11 |
| Linear Regression | 6.42 | 7.93 |
| SARIMA | 6.88 | 8.62 |

In rolling one-step evaluation, the model receives actual observations as the forecasting process moves forward.

ARIMAX performed best in this evaluation when actual external variables were available.

**Important:** Rolling one-step results must not be directly compared with 30-day open-loop cross-validation results.

### 3. Machine-Learning Model Experiments

Linear Regression achieved the following results on the original irregularly spaced observation series:

| Metric | Result |
|---|---:|
| MAE | 17.60 |
| RMSE | 21.60 |
| R² | 0.98494 |

The original-series baseline achieved an MAE of 18.06 and RMSE of 23.80.

Ridge Regression, Lasso, Decision Tree, Random Forest, Extra Trees, Gradient Boosting, XGBoost and LightGBM were also evaluated.

These experiments used a different data representation and evaluation setup from the daily 30-day forecasting experiments. Their metrics should not be ranked directly against the daily time-series results.

---

## 🔍 Residual Diagnostics & Model Analysis

Residual diagnostics were performed to assess whether the fitted forecasting models captured the underlying time-series structure.

The analysis included:

- Residual time-series plots.
- Residual ACF plots.
- Ljung-Box tests.
- Durbin-Watson statistics.
- Normality and heteroskedasticity checks.

The diagnostics identified remaining residual autocorrelation in several models, indicating that some temporal structure was not fully captured.

The analysis also highlighted a substantial change in population levels around early 2025, suggesting a possible structural change in the data-generating process or reporting patterns.

The available dataset alone cannot establish the cause of this change.

---

## 🖥️ Streamlit Application Features

The final application provides an interactive interface with five sections.

### 1. Dashboard

- Total observation count.
- Latest HHS care population.
- Average population.
- Maximum population.
- Historical population visualization.
- Key analytical insights.

### 2. Data Analysis

- Historical time-series exploration.
- Correlation matrix.
- Dataset preview.
- Interactive Plotly visualizations.

### 3. Model Comparison

- Statistical model performance.
- MAE comparison.
- RMSE comparison.
- 30-day cross-validation results.
- Rolling one-step evaluation results.

### 4. Forecasting Studio

- Trained ARIMA (3,1,3) model.
- Adjustable forecast horizon: 7, 14, 21 or 30 days.
- Historical versus predicted population graph.
- Prediction intervals.
- Forecast results table.
- Downloadable forecast CSV.

### 5. About Project

- Project description.
- Objectives.
- Technologies.
- Model information.
- Dataset limitations.

---

## 📁 Project Structure

```text
Care-Transition-Analytics/
│
├── app.py
│
├── arima_331_model.pkl
│
├── HHS_Unaccompanied_Alien_Children_Program.csv
│
├── requirements.txt
│
└── README.md
```

### File Descriptions

| File | Purpose |
|---|---|
| app.py | Main Streamlit application |
| arima_331_model.pkl | Serialized fitted ARIMA forecasting model |
| HHS_Unaccompanied_Alien_Children_Program.csv | Historical dataset |
| requirements.txt | Python dependencies |
| README.md | Project documentation |

---

## ⚙️ Installation & Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/manmeetmanchanda10016/Care-Transition-Analytics.git
```

### 2. Navigate to the project folder

```bash
cd Care-Transition-Analytics
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The dashboard will open in your browser.

No manual CSV or model upload is required when the project files are present in the application directory.

---

## ☁️ Deployment

The application is deployed using Streamlit Community Cloud.

**Live Application:**

[🚀 Open Care Transition Analytics](https://care-transition-analytics-2jkqewg2ozdtjdyy8f8svx.streamlit.app/)

**GitHub Repository:**

[💻 View Source Code](https://github.com/manmeetmanchanda10016/Care-Transition-Analytics)

The application automatically loads the dataset and serialized forecasting model from its deployed project files.

---

## ⚠️ Limitations

- The dataset contains aggregate population counts rather than individual-level records.
- The project cannot predict individual placement outcomes or sponsor reunification.
- The original observations are irregularly spaced.
- Daily observations were constructed through time-based interpolation.
- Forecast accuracy is affected by changes in historical population patterns.
- Forecasted external variables did not improve 30-day ARIMAX performance over the best ARIMA model in the reported comparison.
- Residual autocorrelation remains in some forecasting models.
- The ARIMA (3,1,3) model order was selected using the full dataset before cross-validation, potentially producing optimistic evaluation results.
- The available dataset ends on December 21, 2025. The deployed model therefore generates historical-endpoint forecasts, not live forecasts from the current date.

---

## 🔮 Future Scope

- Incorporate more recent observations.
- Investigate structural breaks and regime changes.
- Improve external-variable forecasting.
- Explore advanced time-series and hybrid forecasting architectures.
- Improve prediction interval calibration.
- Introduce automated model retraining.
- Add more interactive analytical visualizations.
- Develop a forecasting pipeline that adapts to updated data.

---

## 👨‍💻 Author

**Manmeet Singh Manchanda**

Computer Science and Engineering

Thapar Institute of Engineering and Technology

**GitHub:** [manmeetmanchanda10016](https://github.com/manmeetmanchanda10016)

---

## ⭐ Acknowledgement

This project was developed as an application of data science, statistical modelling, machine learning and interactive analytics to aggregate HHS care population data.

If you find this project interesting, consider starring the repository!

---

*Built with Python, Statistical Time-Series Modelling, Machine Learning and Streamlit.*