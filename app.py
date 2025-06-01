from keras.models import load_model
import numpy as np
import pickle
import tensorflow as tf
from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model =pickle.load(open("static/model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        txn_type = request.form['txn_type']
        amount = float(request.form['amount'])
        oldbalanceOrg = float(request.form['oldbalanceOrg'])
        newbalanceOrig = float(request.form['newbalanceOrig'])

        # Mapping transaction types to numerical values
        txn_mapping = {
            "CASH_OUT": 1, "PAYMENT": 2,
            "CASH_IN": 3, "TRANSFER": 4,
            "DEBIT": 5
        }

        # Convert txn_type to a numerical value
        val = txn_mapping.get(txn_type, 0)  # Default to 0 if unknown type

        # Create input array for prediction
        input_array = np.array([[val, amount, oldbalanceOrg, newbalanceOrig]])

        # Make prediction using the loaded model
        prediction = model.predict(input_array)

        # Extract the predicted output value
        output = prediction[0]

        return render_template('index.html', prediction=output)

    except Exception as e:
        return f"Error in processing: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
