import joblib
import numpy as np

# Load the saved Random Forest model
model = joblib.load('random_forest_model.pkl')
#scaler = joblib.load('scaler.pkl')

def predict_sleep(workout_time, reading_time, phone_time, work_hours, caffeine_intake, relaxation_time):
    # Prepare the input as a 2D array
    input_data = np.array([[workout_time, reading_time, phone_time, work_hours, caffeine_intake, relaxation_time]])
    
    # Scale Data
    #scaled = scaler.transform(input_data)

    # Make a prediction
    prediction = model.predict(input_data)
    return round(prediction[0], 2)  # Return the predicted sleep hours, rounded to 2 decimal places
