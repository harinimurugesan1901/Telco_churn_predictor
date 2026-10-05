from flask import Flask, request, render_template_string
import joblib
import os

app = Flask(__name__)

# Model try pannuvom, illana simple logic
MODEL_PATH = "churn_model.pkl"
model = None
if os.path.exists(MODEL_PATH):
    try:
        model = joblib.load(MODEL_PATH)
    except:
        model = None

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Telco Churn Predictor</title>
<style>
body {
  font-family: 'Segoe UI', sans-serif;
  background: linear-gradient(135deg, #667eea, #764ba2);
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0;
}
.card {
  background: white;
  padding: 30px;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.3);
  width: 90%;
  max-width: 380px;
  text-align: center;
}
h2 { color: #333; margin-bottom: 20px; }
input {
  width: 90%;
  padding: 12px;
  margin: 8px 0;
  border-radius: 10px;
  border: 1px solid #ccc;
  font-size: 15px;
}
button {
  background: #667eea;
  color: white;
  border: none;
  padding: 12px 25px;
  border-radius: 10px;
  font-size: 16px;
  cursor: pointer;
  margin-top: 15px;
  width: 95%;
}
button:hover { background: #5a67d8; }
.result {
  margin-top: 20px;
  padding: 15px;
  border-radius: 10px;
  font-weight: bold;
  font-size: 18px;
}
.churn { background: #fed7d7; color: #c53030; }
.no-churn { background: #c6f6d5; color: #22543d; }
</style>
</head>
<body>
<div class="card">
  <h2>📱 Telco Churn Predictor</h2>
  <form method="POST">
    <input type="number" name="tenure" placeholder="Tenure (months)" value="{{tenure}}" required>
    <input type="number" step="0.1" name="monthly" placeholder="Monthly Charges" value="{{monthly}}" required>
    <input type="number" step="0.1" name="total" placeholder="Total Charges" value="{{total}}" required>
    <button type="submit">Predict Churn</button>
  </form>
  {% if result %}
    <div class="result {{cls}}">{{result}}</div>
  {% else %}
    <p style="color:#667eea; margin-top:15px; font-size:14px;">Values kuduthu Predict pannunga 👇</p>
  {% endif %}
</div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    cls = ""
    tenure = monthly = total = ""
    if request.method == 'POST':
        try:
            tenure = request.form.get('tenure','')
            monthly = request.form.get('monthly','')
            total = request.form.get('total','')
            t = float(tenure)
            m = float(monthly)
            # Simple logic - tenure kammi, charge jaasthi na churn
            if t < 12 and m > 70:
                result = "⚠️ Customer CHURN aagalam!"
                cls = "churn"
            else:
                result = "✅ Customer CHURN aaga maatar!"
                cls = "no-churn"
        except Exception as e:
            result = f"Error: {e}"
            cls = "churn"
    return render_template_string(HTML, result=result, cls=cls, tenure=tenure, monthly=monthly, total=total)

if __name__ == '__main__':
    app.run()
