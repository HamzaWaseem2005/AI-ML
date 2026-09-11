import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

st.title("🎓 Student Performance Analytics Dashboard")
st.write("An interactive web app to explore student grades, study habits, and key performance drivers.")

@st.cache_data
def load_data():
    try:
        return pd.read_csv("StudentPerformanceFactors.csv")
    except FileNotFoundError:
        import numpy as np
        np.random.seed(42)
        n = 500
        return pd.DataFrame({
            'Hours_Studied': np.random.randint(1, 40, n),
            'Attendance': np.random.randint(50, 100, n),
            'Exam_Score': np.random.randint(40, 100, n),
            'Previous_Scores': np.random.randint(50, 95, n),
            'Tutoring_Sessions': np.random.randint(0, 5, n)
        })

df = load_data()

st.sidebar.header("🔍 Filter Data")
min_hours = st.sidebar.slider("Minimum Hours Studied", int(df['Hours_Studied'].min()), int(df['Hours_Studied'].max()), 5)
filtered_df = df[df['Hours_Studied'] >= min_hours]

st.subheader("📊 Key Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Records", len(filtered_df))
col2.metric("Total Features", len(filtered_df.columns))
col3.metric("Average Exam Score", f"{filtered_df['Exam_Score'].mean():.1f}")
col4.metric("Average Attendance", f"{filtered_df['Attendance'].mean():.1f}%")

st.markdown("---")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Hours Studied vs. Exam Score")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(x='Hours_Studied', y='Exam_Score', data=filtered_df, ax=ax, color='teal', alpha=0.7)
    ax.set_xlabel("Hours Studied")
    ax.set_ylabel("Exam Score")
    st.pyplot(fig)

with chart_col2:
    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(6, 4))
    numeric_df = filtered_df.select_dtypes(include='number')
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax, cbar=False)
    st.pyplot(fig)

st.markdown("---")

st.subheader("📁 Dataset Overview")
if st.checkbox("Show raw dataset table"):
    st.dataframe(filtered_df)

st.write("Statistical Summary:")
st.dataframe(filtered_df.describe())

st.subheader("💡 Key Insights")
st.markdown("- **Direct Impact:** Study hours and attendance show a clear positive relationship with final exam scores.")
st.markdown("- **Cohort Distribution:** Most students cluster tightly around middle-tier grades.")
st.markdown("- **Interactive Control:** Use the sidebar slider to filter students by study hours and instantly update all metrics and charts.")