from flask import Flask, request, render_template_string

app = Flask("churn")

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Churn Predictor</title>
<style>
body{font-family:Arial;background:#f0f2f5;display:flex;justify-content:center;align-items:center;height:100vh}
.box{background:white;padding:30px;border-radius:15px;box-shadow:0 4px 20px rgba(0,0,0,0.1);width:350px}
input{width:100%;padding:10px;margin:8px 0;border-radius:8px;border:1px solid #ccc}
button{width:100%;padding:12px;background:#6C63FF;color:white;border:none;border-radius:8px;cursor:pointer;font-size:16px}
.result{margin-top:20px;padding:15px;border-radius:8px;text-align:center;font-weight:bold}
.churn{background:#ffebee;color:#c62828}
.no-churn{background:#e8f5e9;color:#2e7d32}
</style>
</head>
<body>
<div class="box">
<h2 style="text-align:center">Customer Churn Predictor</h2>
<form method="post">
Tenure (months): <input name="tenure" type="number" required>
Monthly Charges: <input name="mc" type="number" required>
Total Charges: <input name="tc" type="number" required>
<button type="submit">Predict Churn</button>
</form>
{% if result %}
<div class="result {{cls}}">{{result}}</div>
{% endif %}
</div>
</body>
</html>
"""

@app.route('/', methods=['GET','POST'])
def home():
    result = None
    cls = ""
    if request.method == 'POST':
        try:
            t = int(request.form['tenure'])
            mc = float(request.form['mc'])
            # Simple logic - you can connect your real model later
            if t < 12 and mc > 70:
                result = "⚠️ HIGH RISK - Customer will CHURN!"
                cls = "churn"
            else:
                result = "✅ LOW RISK - Customer will NOT Churn"
                cls = "no-churn"
        except:
            result = "Please enter valid numbers"
            cls = "churn"
    return render_template_string(HTML, result=result, cls=cls)

app.run(debug=True)