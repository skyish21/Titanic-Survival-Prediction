print("Script started")

from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

print("Imports completed")

app = Flask(__name__)

# Load the trained model using pickle
with open('Titanic_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title Mapping (Ensure these match the training data encoding)
TITLE_MAPPING = {
    'Mr': 0, 'Miss': 1, 'Mrs': 2, 'Master': 3, 'Dr': 4,
    'Rev': 5, 'Col': 6, 'Major': 7, 'Mlle': 8, 'Ms': 9,
    'Mme': 10, 'Capt': 11, 'Sir': 12, 'Lady': 13, 'Don': 14,
    'Jonkheer': 15, 'Countess': 16
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extracting form data and encoding categorical variables
        features = [
            float(request.form['Pclass']),
            1 if request.form['Sex'] == 'male' else 0,  # Encoding Male/Female
            float(request.form['Age']),
            float(request.form['SibSp']),
            float(request.form['Parch']),
            float(request.form['Fare']),
            {'C': 0, 'Q': 1, 'S': 2}[request.form['Embarked']],  # Encoding Embarked
            TITLE_MAPPING.get(request.form['Title'], -1),  # Encoding Title
            float(request.form["Ticket"]),
            float(request.form["Cabin"]),
        ]

        # Ensure Title was found in the mapping
        if features[7] == -1:
            return jsonify({'error': f"Invalid title: {request.form['Title']}. Please use a valid title."}), 400

        # Convert to NumPy array and reshape for model
        input_array = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_array)

        return jsonify({'Survival Prediction': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Return error response

if __name__ == '__main__':
    app.run(debug=True)

