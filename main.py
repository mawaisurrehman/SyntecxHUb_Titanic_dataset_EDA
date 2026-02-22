# ==========================================
# TITANIC DATASET - EXPLORATORY DATA ANALYSIS
# ==========================================

# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# 2. Load Dataset
df = pd.read_csv("SyntecxHUb_Titanic_dataset_EDA/train.csv")

print("\nFirst 5 Rows")
print(df.head())

# 3. Dataset Info
print("\nDataset Info")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

# 4. Missing Values
print("\nMissing Values")
missing = df.isnull().sum().sort_values(ascending=False)
print(missing)

plt.figure(figsize=(10,4))
sns.heatmap(df.isnull(), cbar=False)
plt.title("Missing Values Heatmap")
plt.show()

# 5. Overall Survival Rate
survival_rate = df['Survived'].mean()
print("\nOverall Survival Rate:", survival_rate)

plt.figure()
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()

# 6. Survival by Gender
plt.figure()
sns.barplot(x="Sex", y="Survived", data=df)
plt.title("Survival Rate by Gender")
plt.show()

# 7. Survival by Passenger Class
plt.figure()
sns.barplot(x="Pclass", y="Survived", data=df)
plt.title("Survival Rate by Passenger Class")
plt.show()

# 8. Create Age Buckets
bins = [0, 12, 18, 35, 60, 100]
labels = ['Child', 'Teen', 'Young Adult', 'Adult', 'Senior']

df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)

# 9. Survival by Age Group
plt.figure(figsize=(8,5))
sns.barplot(x="AgeGroup", y="Survived", data=df)
plt.title("Survival by Age Group")
plt.show()

# 10. Age Distribution vs Survival
plt.figure(figsize=(8,5))
sns.violinplot(x="Survived", y="Age", data=df)
plt.title("Age Distribution by Survival")
plt.show()

# 11. Boxplot Age vs Class
plt.figure(figsize=(8,5))
sns.boxplot(x="Pclass", y="Age", data=df)
plt.title("Age Distribution by Passenger Class")
plt.show()

# 12. Combined Analysis (Class + Gender)
sns.catplot(x="Pclass", y="Survived", hue="Sex", kind="bar", data=df)
plt.title("Survival by Class and Gender")
plt.show()

# 13. Insight Report
print("\n========== INSIGHTS ==========")

print("1. Females have a much higher survival rate than males.")
print("2. First-class passengers survived more than second and third class.")
print("3. Children show relatively higher survival chances.")
print("4. Cabin column has many missing values and may not be useful directly.")
print("5. Passenger class strongly influences survival probability.")

print("================================")