# -*- coding: utf-8 -*-
"""
Created on Sun Feb  8 19:39:22 2026

@author: donyf
"""

import pandas as pd
import matplotlib.pyplot as plt

# =========================
# STEP 1: Load the dataset
# =========================
# IMPORTANT:
# Put "aml_sample_dataset.csv" in the SAME folder as this .py file
# Or set your working directory to the folder that contains the CSV

df = pd.read_csv(r"C:\Users\donyf\Downloads\aml_sample_dataset (1).csv")

print("Dataset loaded successfully!")
print("\nTop 5 rows:")
print(df.head())

print("\nDataset columns:")
print(df.columns)

# ==================================
# STEP 2: AML Risk Scoring Function
# ==================================
def calculate_risk_score(row):
    score = 0

    # Frequency risk
    if row["transactions_per_month"] > 40:
        score += 25
    elif row["transactions_per_month"] > 20:
        score += 15

    # Amount risk
    if row["transaction_amount"] > 15000:
        score += 25
    elif row["transaction_amount"] > 8000:
        score += 15

    # Country risk
    if row["country_risk"] == "High":
        score += 30
    elif row["country_risk"] == "Medium":
        score += 15

    # Cash transaction risk
    if row["cash_transaction"] == 1:
        score += 10

    return score

# =============================
# STEP 3: Apply Risk Scoring
# =============================
df["risk_score"] = df.apply(calculate_risk_score, axis=1)

# =============================
# STEP 4: Risk Category Labels
# =============================
def risk_category(score):
    if score >= 60:
        return "High Risk"
    elif score >= 30:
        return "Medium Risk"
    else:
        return "Low Risk"

df["risk_category"] = df["risk_score"].apply(risk_category)

# =============================
# STEP 5: Print Results
# =============================
print("\nRisk Category Count:")
print(df["risk_category"].value_counts())

print("\nTop 10 Highest Risk Customers (sample rows):")
print(df.sort_values("risk_score", ascending=False).head(10))

# ==========================================
# STEP 6: Save Output for Power BI / Excel
# ==========================================
output_file = "AML_Risk_Scoring_Output.csv"
df.to_csv(output_file, index=False)
print(f"\nSaved output file: {output_file}")

# =============================
# STEP 7: Create Charts
# =============================

# Chart 1: Risk category count
df["risk_category"].value_counts().plot(kind="bar")
plt.title("Customer Risk Category Count")
plt.xlabel("Risk Category")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# Chart 2: Risk score distribution
df["risk_score"].plot(kind="hist", bins=10)
plt.title("Risk Score Distribution")
plt.xlabel("Risk Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
