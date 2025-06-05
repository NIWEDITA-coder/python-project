**Online-Payments-Fraud-Detection-with-Machine-Learning**

Online payment frauds can happen with anyone using any payment system, especially while making payments using a credit card. That is why detecting online payment fraud is very important for credit card companies to ensure that the customers are not getting charged for the products and services they never paid.The online payment method leads to fraud that can happen using any payment app. That is why Online Payment Fraud Detection is very important.

To identify online payment fraud with machine learning, we need to train a machine learning model for classifying fraudulent and non-fraudulent payments. For this, we need a dataset containing information about online payment fraud, so that we can understand what type of transactions lead to fraud. For this task, I collected a dataset from Kaggle, which contains historical information about fraudulent transactions which can be used to detect fraud in online payments. Below are all the columns from the dataset I’m using here:

step : represents a unit of time where 1 step equals 1 hour
type : type of online transaction
amount : the amount of the transaction
nameOrig : customer starting the transaction
oldbalanceOrg : balance before the transaction
newbalanceOrig : balance after the transaction
nameDest : recipient of the transaction
oldbalanceDest : initial balance of recipient before the transaction
newbalanceDest : the new balance of recipient after the transaction
isFraud : fraud transaction

**Online Payments Fraud Detection using Python**

import pandas as pd   
import numpy as np   

import matplotlib.pyplot as plt   
import seaborn as sns   
data = pd.read_csv('fraud.csv')
data.head()
![image](https://github.com/user-attachments/assets/63ab863d-b851-4340-a834-be59c84cc947)
# Load the trained model
model =pickle.load(open("static/model.pkl", "rb"))
 # Get input values from the form
        txn_type = request.form['txn_type']
        amount = float(request.form['amount'])
        oldbalanceOrg = float(request.form['oldbalanceOrg'])
        newbalanceOrig = float(request.form['newbalanceOrig'])
**Files:-**
`app.py` – Flask application
`model.pkl` – Trained ML model
`index.html` – Frontend UI
`main.ipynb` – Notebook used for training and testing
`README.md` – Project documentation

**Run the application:**
python app.py

Open browser and go to:
http://127.0.0.1:5000
Press CTRL+C to quit











