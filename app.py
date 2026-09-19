import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle

# 1. Load data
df = pd.read_csv('Churn.csv')

# 2. Clean
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna()
df = df.drop('customerID', axis=1)

# 3. Encode
for col in df.select_dtypes(include='object').columns:
    df[col] = LabelEncoder().fit_transform(df[col])

# 4. Train
X = df.drop('Churn', axis=1)
y = df['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

model = RandomForestClassifier(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

print(f"Accuracy: {model.score(X_test, y_test)*100:.2f}%")
print("Model Ready Bro!")

# Save model
pickle.dump(model, open('churn_model.pkl','wb'))