import streamlit as st
from data_preprocessing import load_data
from model_training import train_model
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Mall Customer Segmentation", layout="centered")

st.title("🛍️ Mall Customer Clustering App")
st.markdown("Visualize clusters based on income and spending score.")

df = load_data("data/mall_customers.csv")

st.write("### Dataset Preview")
st.dataframe(df.head())

n_clusters = st.slider("Select number of clusters", 2, 10, 5)

clustered_df, model = train_model(df.copy(), n_clusters)

st.write("### Clustered Data Sample")
st.dataframe(clustered_df.head())

st.write("### 📊 Customer Segmentation Plot")
fig, ax = plt.subplots()
sns.scatterplot(data=clustered_df, x='Annual_Income', y='Spending_Score', hue='Cluster', palette='Set1', ax=ax)
st.pyplot(fig)
