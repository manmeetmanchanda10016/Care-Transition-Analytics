
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go

# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Care Transition Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# 2. DARK THEME CSS
# =====================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background: #080d19;
    color: #e2e8f0;
    font-family: 'Inter', sans-serif;
}

[data-testid="stHeader"] {
    background: #080d19;
}

[data-testid="stSidebar"] {
    background: #101c30;
    border-right: 1px solid #263b58;
}

[data-testid="stSidebar"] * {
    color: #e2e8f0;
}

[data-testid="stSidebar"] hr {
    border-color: #30435e;
}

h1, h2, h3 {
    color: #f1f5f9 !important;
    font-weight: 750 !important;
}

p, label {
    color: #a9b9cf;
}

[data-testid="stMetric"] {
    background: linear-gradient(145deg, #172840, #101b2e);
    border: 1px solid #29415e;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 5px 20px rgba(0,0,0,.2);
}

[data-testid="stMetricLabel"] {
    color: #a9bdd6 !important;
}

[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-weight: 800;
}

[data-testid="stMetricDelta"] {
    color: #2dd4bf !important;
}

[data-testid="stDataFrame"] {
    border: 1px solid #2b405b;
    border-radius: 12px;
}

.stButton > button {
    background: linear-gradient(100deg, #2563eb, #0891b2);
    color: white;
    border: 1px solid #38bdf8;
    border-radius: 10px;
    font-weight: 700;
    padding: 10px 20px;
}

.stButton > button:hover {
    background: #1d4ed8;
    color: white;
    border-color: #67e8f9;
}

.stDownloadButton > button {
    background: #12314a;
    color: #67e8f9;
    border: 1px solid #28728c;
    border-radius: 10px;
}

[data-testid="stAlert"] {
    background: #14243a;
    border: 1px solid #304d6b;
    border-radius: 10px;
}

[data-testid="stSlider"] label,
[data-testid="stSelectSlider"] label {
    color: #dbeafe !important;
}

hr {
    border-color: #263b55;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# 3. LOAD DATASET
# =====================================================

@st.cache_data
def load_data():

    data = pd.read_csv(
        "HHS_Unaccompanied_Alien_Children_Program.csv"
    )

    data["Date"] = pd.to_datetime(data["Date"])

    population_col = "Children in HHS Care"

    data[population_col] = pd.to_numeric(
        data[population_col]
        .astype(str)
        .str.replace(",", "", regex=False),
        errors="coerce"
    )

    data = data.dropna(
        subset=["Date", population_col]
    )

    return data.sort_values("Date").reset_index(drop=True)


# =====================================================
# 4. LOAD TRAINED MODEL
# =====================================================

@st.cache_resource
def load_model():

    return joblib.load("arima_331_model.pkl")


try:
    df = load_data()
    model = load_model()

except Exception as error:

    st.error(f"Unable to load project files: {error}")

    st.warning(
        "Keep app.py, the CSV dataset and "
        "arima_331_model.pkl in the same folder."
    )

    st.stop()


POPULATION = "Children in HHS Care"


# =====================================================
# 5. MODEL RESULTS
# =====================================================

cv_results = pd.DataFrame({
    "Model": [
        "ARIMA (3,1,3)",
        "ARIMA (2,1,1)",
        "Damped Trend",
        "ARIMAX (Forecasted Exog)",
        "Naive Forecast",
        "Holt Linear Trend"
    ],
    "MAE": [
        31.5467,
        34.1377,
        35.7138,
        34.9834,
        60.0678,
        84.3163
    ],
    "RMSE": [
        37.9764,
        41.8428,
        45.2545,
        42.4606,
        71.1148,
        98.0872
    ]
})

rolling_results = pd.DataFrame({
    "Model": [
        "ARIMAX (Actual Exog)",
        "ARIMA (2,1,1)",
        "Linear Regression",
        "SARIMA"
    ],
    "MAE": [
        3.9626,
        4.5423,
        6.4195,
        6.8779
    ],
    "RMSE": [
        5.1200,
        6.1149,
        7.9316,
        8.6226
    ]
})


# =====================================================
# 6. PLOTLY DARK THEME
# =====================================================

def dark_layout(fig, height=420):

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#111c2e",
        plot_bgcolor="#111c2e",
        font=dict(
            family="Inter",
            color="#dbeafe"
        ),
        height=height,
        margin=dict(
            l=25,
            r=25,
            t=35,
            b=25
        ),
        xaxis=dict(
            gridcolor="#293c54",
            zerolinecolor="#293c54"
        ),
        yaxis=dict(
            gridcolor="#293c54",
            zerolinecolor="#293c54"
        ),
        legend=dict(
            bgcolor="rgba(0,0,0,0)"
        )
    )

    return fig


# =====================================================
# 7. SIDEBAR NAVIGATION
# =====================================================

with st.sidebar:

    st.title("🌌 CARE TRANSITION")

    st.caption("AI & ANALYTICS PLATFORM")

    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "Dashboard",
            "Data Analysis",
            "Model Comparison",
            "Forecasting",
            "About Project"
        ]
    )

    st.divider()

    st.subheader("SYSTEM STATUS")

    st.success("Dataset connected")

    st.success("ARIMA model loaded")

    st.divider()

    st.caption("TIME SERIES FORECASTING")

    st.caption("Python | Streamlit | Plotly")


# =====================================================
# 8. HERO SECTION — NATIVE STREAMLIT
# =====================================================

with st.container(border=True):

    st.caption("✦ DATA SCIENCE  /  MACHINE LEARNING  /  FORECASTING")

    st.title("Care Transition Analytics")

    st.write(
        "An intelligent analytics platform for exploring "
        "historical HHS care population trends, evaluating "
        "forecasting models and generating future estimates."
    )

    st.caption(
        f"DATA PERIOD: {df['Date'].min():%d %b %Y} "
        f"— {df['Date'].max():%d %b %Y}"
    )


# =====================================================
# 9. DASHBOARD
# =====================================================

if page == "Dashboard":

    st.subheader("⚡ Intelligence Overview")

    st.caption("Key statistics from the historical dataset")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Records",
        f"{len(df):,}"
    )

    c2.metric(
        "Latest HHS Population",
        f"{df[POPULATION].iloc[-1]:,.0f}"
    )

    c3.metric(
        "Average Population",
        f"{df[POPULATION].mean():,.0f}"
    )

    c4.metric(
        "Maximum Population",
        f"{df[POPULATION].max():,.0f}"
    )

    st.divider()

    left, right = st.columns([1.8, 1])

    with left:

        st.subheader("📈 Population Evolution")

        fig = px.area(
            df,
            x="Date",
            y=POPULATION,
            color_discrete_sequence=["#38bdf8"]
        )

        fig.update_traces(
            line=dict(width=2.5),
            fillcolor="rgba(56,189,248,0.13)"
        )

        fig = dark_layout(fig, 420)

        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Children in HHS Care",
            hovermode="x unified"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("💡 Key Insights")

        st.info(
            "**Historical Trends**\n\n"
            "The HHS care population experienced "
            "substantial changes throughout the study period."
        )

        st.info(
            "**Important Variables**\n\n"
            "HHS discharges and CBP transfers were examined "
            "in relation to population levels."
        )

        st.success(
            "**Best 30-Day CV Model**\n\n"
            "ARIMA (3,1,3)\n\n"
            "MAE: 31.55 | RMSE: 37.98"
        )

        st.info(
            "**Forecasting Objective**\n\n"
            "Estimate aggregate HHS care population "
            "over a 30-day horizon."
        )

    st.divider()

    st.subheader("📋 Recent Observations")

    st.dataframe(
        df.tail(10),
        use_container_width=True,
        hide_index=True
    )


# =====================================================
# 10. DATA ANALYSIS
# =====================================================

elif page == "Data Analysis":

    st.subheader("🔬 Exploratory Data Analysis")

    st.caption(
        "Explore population trends, data distributions "
        "and relationships between variables."
    )

    c1, c2 = st.columns(2)

    c1.metric(
        "Start Date",
        df["Date"].min().strftime("%d %b %Y")
    )

    c2.metric(
        "End Date",
        df["Date"].max().strftime("%d %b %Y")
    )

    st.divider()

    st.subheader("Historical HHS Population")

    fig = px.line(
        df,
        x="Date",
        y=POPULATION,
        color_discrete_sequence=["#2dd4bf"]
    )

    fig.update_traces(
        line=dict(width=2.5)
    )

    fig = dark_layout(fig, 430)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("Correlation Matrix")

    numeric_df = df.select_dtypes(include="number")

    correlation = numeric_df.corr()

    fig = px.imshow(
        correlation,
        text_auto=".2f",
        color_continuous_scale="Tealrose",
        zmin=-1,
        zmax=1,
        aspect="auto"
    )

    fig = dark_layout(fig, 550)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("Dataset Explorer")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# =====================================================
# 11. MODEL COMPARISON
# =====================================================

elif page == "Model Comparison":

    st.subheader("🧠 Model Performance Lab")

    st.caption(
        "Compare the performance of statistical "
        "forecasting models."
    )

    a, b, c = st.columns(3)

    a.metric(
        "Best 30-Day CV Model",
        "ARIMA (3,1,3)"
    )

    b.metric(
        "Lowest CV MAE",
        "31.55"
    )

    c.metric(
        "Lowest CV RMSE",
        "37.98"
    )

    st.divider()

    st.subheader("30-Day Cross-Validation Results")

    st.caption(
        "Lower MAE and RMSE indicate better performance."
    )

    st.dataframe(
        cv_results.style.highlight_min(
            subset=["MAE", "RMSE"],
            color="#14532d"
        ).format({
            "MAE": "{:.2f}",
            "RMSE": "{:.2f}"
        }),
        use_container_width=True,
        hide_index=True
    )

    left, right = st.columns(2)

    with left:

        st.subheader("MAE Comparison")

        fig = px.bar(
            cv_results.sort_values("MAE"),
            x="MAE",
            y="Model",
            orientation="h",
            text="MAE",
            color="MAE",
            color_continuous_scale="Blues"
        )

        fig.update_layout(
            coloraxis_showscale=False,
            xaxis_title="Mean Absolute Error",
            yaxis_title=""
        )

        fig = dark_layout(fig, 430)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("RMSE Comparison")

        fig = px.bar(
            cv_results.sort_values("RMSE"),
            x="RMSE",
            y="Model",
            orientation="h",
            text="RMSE",
            color="RMSE",
            color_continuous_scale="Teal"
        )

        fig.update_layout(
            coloraxis_showscale=False,
            xaxis_title="Root Mean Squared Error",
            yaxis_title=""
        )

        fig = dark_layout(fig, 430)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    st.subheader("Rolling One-Step Evaluation")

    st.warning(
        "These results use a different evaluation protocol "
        "from 30-day cross-validation. Do not compare "
        "their numerical values directly."
    )

    st.dataframe(
        rolling_results.style.highlight_min(
            subset=["MAE", "RMSE"],
            color="#14532d"
        ).format({
            "MAE": "{:.2f}",
            "RMSE": "{:.2f}"
        }),
        use_container_width=True,
        hide_index=True
    )


# =====================================================
# 12. FORECASTING
# =====================================================

elif page == "Forecasting":

    st.subheader("🔮 Forecasting Studio")

    st.caption(
        "Generate population estimates using "
        "your trained ARIMA (3,1,3) model."
    )

    st.info(
        "The model was trained on data ending "
        "December 21, 2025. Forecasts start after "
        "that historical endpoint."
    )

    steps = st.select_slider(
        "Select Forecast Horizon",
        options=[7, 14, 21, 30],
        value=30
    )

    st.write(f"Selected forecast period: **{steps} days**")

    if st.button("🚀 Generate Forecast"):

        with st.spinner("Running ARIMA forecasting model..."):

            result = model.get_forecast(
                steps=steps
            )

            forecast = result.predicted_mean

            interval = result.conf_int()

            forecast_dates = pd.date_range(
                start=df["Date"].max() + pd.Timedelta(days=1),
                periods=steps,
                freq="D"
            )

            forecast_df = pd.DataFrame({

                "Date": forecast_dates,

                "Predicted HHS Population":
                    np.asarray(forecast),

                "Lower Bound":
                    interval.iloc[:, 0].to_numpy(),

                "Upper Bound":
                    interval.iloc[:, 1].to_numpy()

            })

            st.success("Forecast generated successfully!")

            a, b, c = st.columns(3)

            a.metric(
                "Forecast Horizon",
                f"{steps} Days"
            )

            b.metric(
                "First Prediction",
                f"{forecast_df['Predicted HHS Population'].iloc[0]:,.0f}"
            )

            c.metric(
                "Final Prediction",
                f"{forecast_df['Predicted HHS Population'].iloc[-1]:,.0f}"
            )

            st.divider()

            st.subheader("📈 Historical vs Forecasted Population")

            historical = df.tail(180)

            fig = go.Figure()

            fig.add_trace(
                go.Scatter(
                    x=historical["Date"],
                    y=historical[POPULATION],
                    mode="lines",
                    name="Historical",
                    line=dict(
                        color="#38bdf8",
                        width=3
                    )
                )
            )

            fig.add_trace(
                go.Scatter(
                    x=forecast_df["Date"],
                    y=forecast_df["Upper Bound"],
                    mode="lines",
                    line=dict(width=0),
                    showlegend=False,
                    hoverinfo="skip"
                )
            )

            fig.add_trace(
                go.Scatter(
                    x=forecast_df["Date"],
                    y=forecast_df["Lower Bound"],
                    mode="lines",
                    fill="tonexty",
                    fillcolor="rgba(45,212,191,0.15)",
                    line=dict(width=0),
                    name="95% Confidence Interval",
                    hoverinfo="skip"
                )
            )

            fig.add_trace(
                go.Scatter(
                    x=forecast_df["Date"],
                    y=forecast_df["Predicted HHS Population"],
                    mode="lines+markers",
                    name="Forecast",
                    line=dict(
                        color="#2dd4bf",
                        width=3
                    ),
                    marker=dict(size=6)
                )
            )

            fig = dark_layout(fig, 470)

            fig.update_layout(
                hovermode="x unified",
                xaxis_title="Date",
                yaxis_title="Children in HHS Care"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.divider()

            st.subheader("📋 Forecast Results")

            st.dataframe(
                forecast_df.round(2),
                use_container_width=True,
                hide_index=True
            )

            st.download_button(
                "⬇️ Download Forecast CSV",
                forecast_df.to_csv(index=False),
                file_name="HHS_Forecast.csv",
                mime="text/csv"
            )


# =====================================================
# 13. ABOUT PROJECT
# =====================================================

elif page == "About Project":

    st.subheader("🌐 About the Project")

    with st.container(border=True):

        st.title("Care Transition Efficiency & Placement Outcome Analytics")

        st.write(
            "A data science project focused on understanding "
            "historical HHS care population trends and evaluating "
            "time-series forecasting models."
        )

    st.divider()

    st.subheader("🎯 Project Objectives")

    objectives = [
        "Analyse historical HHS care population trends.",
        "Study relationships between CBP transfers, HHS discharges and population levels.",
        "Develop aggregate population forecasting models.",
        "Compare statistical and machine-learning approaches.",
        "Generate 30-day population forecasts."
    ]

    for objective in objectives:
        st.markdown(f"- {objective}")

    st.divider()

    st.subheader("🧠 Models Evaluated")

    st.write(
        "Linear Regression | ARIMA | SARIMA | ARIMAX | "
        "Holt Linear Trend | Damped Trend"
    )

    st.divider()

    st.subheader("🏆 Best 30-Day CV Model")

    c1, c2 = st.columns(2)

    c1.metric("Model", "ARIMA (3,1,3)")

    c2.metric("MAE / RMSE", "31.55 / 37.98")

    st.warning(
        "The dataset contains aggregate population counts, "
        "not individual-level placement records. This application "
        "does not predict individual placement outcomes "
        "or sponsor reunification."
    )


# =====================================================
# 14. FOOTER
# =====================================================

st.divider()

st.caption(
    "CARE TRANSITION ANALYTICS  |  "
    "DATA SCIENCE  •  MACHINE LEARNING  •  FORECASTING"
)

