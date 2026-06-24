import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="HR Attrition Dashboard", layout="wide")
st.title("📊 HR Employee Attrition Dashboard")
st.markdown("Explore employee turnover trends and identify key risk factors.")

# 2. Load the Data
# The @st.cache_data decorator keeps the app fast by not reloading data on every click
@st.cache_data
def load_data():
    df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
    return df

df = load_data()

# 3. Sidebar for Filters
st.sidebar.header("Filter Options")
department_filter = st.sidebar.selectbox(
    "Select Department", 
    options=["All"] + list(df['Department'].unique())
)

# Apply the filter
if department_filter != "All":
    filtered_df = df[df['Department'] == department_filter]
else:
    filtered_df = df

# 4. Calculate Top-Level KPIs
total_employees = len(filtered_df)
attrition_rate = (filtered_df['Attrition'] == 'Yes').mean() * 100
avg_monthly_income = filtered_df['MonthlyIncome'].mean()

# Display KPIs using Streamlit metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Employees", f"{total_employees:,}")
col2.metric("Attrition Rate", f"{attrition_rate:.1f}%")
col3.metric("Average Monthly Income", f"${avg_monthly_income:,.0f}")

st.divider()

# 5. Interactive Visualizations
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("Attrition by Job Role")
    # Calculate attrition count per job role
    role_attrition = filtered_df[filtered_df['Attrition'] == 'Yes'].groupby('JobRole').size().reset_index(name='Count')
    fig1 = px.bar(role_attrition, x='JobRole', y='Count', color='JobRole', title="Number of Employees Leaving by Role")
    st.plotly_chart(fig1, use_container_width=True)

with col_chart2:
    st.subheader("Income Distribution: Stayed vs. Left")
    fig2 = px.box(filtered_df, x='Attrition', y='MonthlyIncome', color='Attrition', 
                  title="Monthly Income Impact on Attrition")
    st.plotly_chart(fig2, use_container_width=True)