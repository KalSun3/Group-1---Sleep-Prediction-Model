from flask import Flask, request, render_template, jsonify
import model  # Import your model logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Serves the input form page

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Extract inputs from the request
    workout_time = float(data['workout_time'])
    reading_time = float(data['reading_time'])
    phone_time = float(data['phone_time'])
    work_hours = float(data['work_hours'])
    caffeine_intake = float(data['caffeine_intake'])
    relaxation_time = float(data['relaxation_time'])

    # Call the model's prediction function
    prediction = model.predict_sleep(
        workout_time, reading_time, phone_time, work_hours, caffeine_intake, relaxation_time
    )

    return jsonify({'predicted_sleep_hours': prediction})

if __name__ == '__main__':
    app.run(debug=True)
