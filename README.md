#  Retail Sales Prediction using Machine Learning

## 📌 Overview
This project aims to predict retail store sales using historical data that includes promotions, store type, holiday flags, fuel price, and more.

Built with multiple regression models and evaluated to find the most accurate one — perfect for real-world forecasting use cases.

---
# 🛍️ Retail Sales Prediction

A machine learning project that predicts weekly sales for retail stores using XGBoost.

🚀 **Live Demo**: [Click here to try the app](https://irfu1s-retail-sales-prediction.streamlit.app/)

📊 Built with: XGBoost, Pandas, Streamlit  
🔍 Dataset: Walmart Retail Sales Data (cleaned)

---


## 📂 Datasets Used
- `train.csv`: Weekly sales data
- `features.csv`: Additional features like temperature, markdowns, and holidays
- `stores.csv`: Store-level metadata (type and size)

---

##  Models Trained
| Model             | R² Score | RMSE     | MAE     |
|------------------|----------|----------|---------|
| Linear Regression| 0.0900   | 21824.98 | 14564.77 |
| Decision Tree    | 0.9640   | 7152.62  | 4954.30 |
| Random Forest    | 0.0866   | 21824.98 | 14564.77 |
| **XGBoost ✅**     | **0.9035** | **7094.16** | **4019.50** |

---

## ✅ Best Model: XGBoost
XGBoost gave the best performance with high R² and lowest RMSE & MAE, making it the final selected model.

---

## 📊 Visualizations
- Weekly Sales Trend
- Store-wise Sales Comparison
- Holiday vs Non-Holiday Sales
- Promotions vs Sales Insights

---

## 🛠 Tools Used
- Python, Pandas, NumPy
- Scikit-learn, XGBoost
- Seaborn, Matplotlib
- Google Colab

---

## 👨‍💻 Built By
**Irfan Hussain**  



## 📊 Power BI Dashboard

A Power BI dashboard was built using the cleaned dataset to provide dynamic visual insights.

**Key Visuals:**
- Total Retail Sales by Year
- Store-wise Sales by Type
- Holiday vs Non-Holiday Sales Comparison
- Top Performing Stores
- Sales Contribution by Store Type
- Interactive Filters by Year, Store Type, Holiday Flag

> 🔗 Power BI File: [Retail_sales_prediction_dashboard.pbix](Retail_sales_prediction_dashboard.pbix)
Data Science Enthusiast | [irfan Hussain](https://www.linkedin.com/in/irfanhussain-irfu)

---
