# ads_optimizer.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Step 1: Load Data
df = pd.read_csv("ads_data.csv")

# Step 2: Feature Engineering
df['CTR'] = (df['Clicks'] / df['Impressions']) * 100
df['CPC'] = df['Cost'] / df['Clicks']
df['ROI'] = df['Conversions'] / df['Cost'] * 100

# Step 3: Summary Stats
print("\n🔍 Ad Campaign Summary with CTR, CPC, ROI:\n")
print(df[['Campaign', 'Keyword', 'CTR', 'CPC', 'ROI']])

# Step 4: ML Prediction Setup
features = df[['CTR', 'CPC']]
target = df['ROI']

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test set
predictions = model.predict(X_test)

print("\n📈 ML ROI Predictions (Based on CTR + CPC):\n")
for i in range(len(predictions)):
    print(f"Predicted ROI: {predictions[i]:.2f}%, Actual ROI: {y_test.iloc[i]:.2f}%")

# Optional: Predict future scenarios
future_ctr = float(input("\n📥 Enter future CTR (%): "))
future_cpc = float(input("📥 Enter future CPC: "))
predicted_roi = model.predict([[future_ctr, future_cpc]])
print(f"\n💡 Predicted ROI for CTR={future_ctr}% and CPC={future_cpc} is ➜ {predicted_roi[0]:.2f}%")

# Step 5: Plot
df.groupby('Campaign')[['CTR', 'CPC', 'ROI']].mean().plot(kind='bar', figsize=(10,6), title="📊 Avg CTR, CPC, ROI by Campaign")
plt.grid(True)
plt.tight_layout()
plt.show()
