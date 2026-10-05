from flask import Flask, request
import os
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
 result="";t="";m="";tot="";bg=""
 if request.method=='POST':
  t=request.form.get('tenure','');m=request.form.get('monthly','');tot=request.form.get('total','')
  try:
   if float(t)<15 and float(m)>70:
    result="Customer May CHURN";bg="#fecaca"
   else:
    result="Customer Will NOT Churn";bg="#bbf7d0"
  except:
   result="Enter valid numbers";bg="#fecaca"
 return "<html><head><meta name=viewport content='width=device-width,initial-scale=1'><style>body{margin:0;font-family:Arial;background:linear-gradient(135deg,#667eea,#764ba2);min-height:100vh;display:flex;justify-content:center;align-items:center}.card{background:white;padding:28px;border-radius:18px;width:90%;max-width:350px;text-align:center}input{width:100%;padding:11px;margin:7px 0;border-radius:8px;border:1px solid #ccc;box-sizing:border-box}button{width:100%;padding:12px;background:#6366f1;color:white;border:none;border-radius:8px;font-weight:bold}.box{margin-top:12px;padding:10px;border-radius:8px;font-weight:bold;background:"+bg+"}</style></head><body><div class=card><h2>Telco Churn Predictor</h2><form method=POST><input name=tenure type=number placeholder='Tenure (months)' value='"+t+"' required><input name=monthly type=number step=0.01 placeholder='Monthly Charges' value='"+m+"' required><input name=total type=number step=0.01 placeholder='Total Charges' value='"+tot+"' required><button>Predict Churn</button></form><div class=box>"+result+"</div></div></body></html>"

if __name__=='__main__':
 app.run(host='0.0.0.0',port=int(os.environ.get('PORT',10000)))
