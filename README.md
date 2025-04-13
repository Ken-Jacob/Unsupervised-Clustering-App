
# 🛍️ Mall Customer Clustering App

This is an interactive Streamlit web app that uses **KMeans clustering** to segment mall customers based on their **annual income** and **spending score**. It helps businesses gain insights into customer behavior to support targeted marketing and personalization strategies.

---

## 📌 Features

- Loads and displays customer demographic data
- Allows user to select number of clusters (2 to 10)
- Uses KMeans to group similar customers
- Visualizes customer segments in a 2D scatter plot
- Simple and intuitive UI built with Streamlit
- Logging system to track events and errors

---

## 🧠 What is Clustering?

Clustering is an **unsupervised machine learning** technique that groups data points based on similarity. In this app, clustering is used to:

- Identify customer groups like "High income, high spending", "Low income, low spending", etc.
- Help businesses make data-driven marketing decisions

---

## ▶️ How to Run the App Locally

### 🔧 Step 1: Clone the Repository

```bash
git clone https://github.com/Ken-Jacob/Unsupervised-Clustering-App.git
cd Unsupervised-Clustering-App
```

### 📦 Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### 🚀 Step 3: Launch the App

```bash
streamlit run app.py
```

---

## ☁️ Deployment

This app is deployed using **Streamlit Cloud**.

**Live Demo**: [https://your-streamlit-app-link](https://your-streamlit-app-link)

To deploy your own version:

1. Push this project to GitHub
2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Connect your GitHub repo
4. Choose `app.py` as the entry point
5. Click "Deploy"

---

## 📊 Sample Output

![Cluster Plot](https://via.placeholder.com/600x300?text=Customer+Segments+Plot)

---

## 📋 Dataset Description

The dataset used in this app contains the following columns:

- `Customer_ID` — Unique customer ID
- `Gender` — Male/Female
- `Age` — Customer’s age
- `Annual_Income` — In thousands (k$)
- `Spending_Score` — Score assigned by the mall based on customer behavior

---

## 📄 License

This project is licensed under 

---

## 🙋‍♂️ Author

Ken Biju Jacob
Business Intelligence System Infrastructure program
Algonquin College.
