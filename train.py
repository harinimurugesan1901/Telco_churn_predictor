import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

# File peru Churn.csv
df = pd.read_csv('Churn.csv')

# TotalCharges-a number aakkurom - error iruntha remove panrom
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna()

print(f"Total rows: {len(df)}")

# Thevaiyana 3 column mattum
X = df[['tenure', 'MonthlyCharges', 'TotalCharges']]
y = df['Churn'].map({'Yes':1, 'No':0})

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

pickle.dump(model, open('churn_model.pkl','wb'))
print("Real Telco Model Ready Bro! 7043 customers vechu train pannitom!")