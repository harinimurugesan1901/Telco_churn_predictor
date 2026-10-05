from flask import Flask, request, render_template_string
import pickle
import pandas as pd

app = Flask(__name__)

# Load your model
try:
    model = pickle.load(open('churn_model.pkl','rb'))
except:
    model = None

HTML_PAGE = """
<h2 style="text-align:center">Telco Churn Predictor</h2>
<form method="post" style="text-align:center">
    <p>Tenure: <input name="tenure" value="12" required></p>
    <p>Monthly Charges: <input name="MonthlyCharges" value="70" required></p>
    <p>Total Charges: <input name="TotalCharges" value="800" required></p>
    <button type="submit">Predict Churn</button>
</form>
<h3 style="text-align:center; color:blue">{{ result }}</h3>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    result = "Values kuduthu Predict pannunga"
    if request.method == 'POST' and model is not None:
        # Simple logic - we need to handle your model columns
        # For now, using direct prediction
        try:
            tenure = float(request.form['tenure'])
            # Basic rule for demo (replace with real model input later)
            if tenure < 10:
                result = "Prediction: Customer CHURN pannuvanga 😟"
            else:
                result = "Prediction: Customer STAY pannuvanga 😊"
        except Exception as e:
            result = f"Error: {e}"
    elif model is None:
        result = "Model file churn_model.pkl GitHub la illa! Notebooks la irunthu upload pannunga"
    
    return render_template_string(HTML_PAGE, result=result)

if __name__ == '__main__':
    app.run()
