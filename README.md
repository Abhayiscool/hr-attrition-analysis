# 📊 Employee Attrition Analysis & Prediction

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://[YOUR-STREAMLIT-APP-LINK-HERE])

## 📝 Project Overview
Employee turnover is a massive expense for organizations, costing up to 200% of an employee's annual salary to replace them. This project aims to analyze the root causes of employee attrition and build a predictive machine learning model to flag high-risk employees before they leave. 

The project concludes with an interactive web dashboard built in Streamlit, allowing HR stakeholders to explore the data and insights intuitively.

## 🎯 Business Value
* **Proactive Retention:** Identifies flight-risk employees allowing for targeted interventions.
* **Cost Reduction:** Decreases recruitment and onboarding costs by improving retention rates.
* **Data-Driven HR:** Shifts HR strategy from reactive problem-solving to proactive, predictive management.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Logistic Regression, Random Forest)
* **Data Visualization:** Matplotlib, Seaborn, Plotly
* **Deployment:** Streamlit

## 📂 Dataset
The data used is the **IBM HR Analytics Employee Attrition & Performance** dataset.
* **Size:** 1,470 rows, 35 columns
* **Target Variable:** `Attrition` (Yes/No)
* **Key Features:** Age, Department, Monthly Income, Overtime, Job Role, Years at Company.

## 🔍 Key Insights & Exploratory Data Analysis
1. **The Baseline:** The overall attrition rate for the company is **16.1%**.
2. **The Income Factor:** Employees who leave generally have a significantly lower median monthly income compared to those who stay.
3. **The Overtime Burnout:** Employees working overtime have a disproportionately higher flight risk.
4. **Departmental Trends:** The Sales department exhibits higher turnover relative to Research & Development.

## 🤖 Machine Learning Modeling
To predict attrition, I trained and evaluated two classification models, handling the class imbalance using balanced class weights.

* **Logistic Regression:** Used for baseline interpretability.
* **Random Forest Classifier:** Used to capture complex, non-linear relationships and extract feature importance. 

**Top 3 Drivers of Attrition (Feature Importance):**
1. Monthly Income
2. Age
3. Overtime

## 🚀 How to Run Locally

1. Clone the repository:

   git clone [https://github.com/](https://github.com/)[YOUR-USERNAME]/hr-attrition-analysis.git
   
2. Install dependencies:
    pip install -r requirements.txt

3. Run the Streamlit dashboard:
    streamlit run app.py
