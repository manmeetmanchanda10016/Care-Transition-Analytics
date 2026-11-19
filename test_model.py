import joblib

model = joblib.load("arima_331_model.pkl")

print("Model loaded successfully!")
print(model.summary())