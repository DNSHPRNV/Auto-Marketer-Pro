# email_insights.py

import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv("email_data.csv")

# Print the data (like a baby preview)
print("\n📄 Email Data:\n")
print(data)

# Average Open and Click Rates
avg_open = data['OpenRate'].mean()
avg_click = data['ClickRate'].mean()

print("\n📊 Average Open Rate:", round(avg_open, 2), "%")
print("📊 Average Click Rate:", round(avg_click, 2), "%")

# Best performing subject line
best_subject = data.loc[data['ClickRate'].idxmax()]
print("\n🔥 Best Subject Line:")
print("Subject:", best_subject['Subject'])
print("Click Rate:", best_subject['ClickRate'], "%")

# Visualize Time vs Open Rate
plt.figure(figsize=(8, 5))
plt.plot(data['SendTime'], data['OpenRate'], marker='o', color='skyblue', label='Open Rate')
plt.plot(data['SendTime'], data['ClickRate'], marker='o', color='lightgreen', label='Click Rate')
plt.title("📈 Open & Click Rate by Send Time")
plt.xlabel("Send Time")
plt.ylabel("Percentage")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
