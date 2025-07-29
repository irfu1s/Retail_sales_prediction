# 🛍️ Retail Sales Prediction using Machine Learning

## 📌 Overview  
This project aims to predict **weekly retail store sales** using historical data like promotions, store type, fuel prices, holidays, and more.  
It includes model building, data preprocessing, and deployment via **Streamlit**, with a **Power BI dashboard** as a bonus.

---

## 🚀 Live App  
👉 [Click here to try the Streamlit App](https://irfu1s-retail-sales-prediction.streamlit.app/)

---

## 📂 Datasets Used  
- `train.csv`: Weekly sales data  
- `features.csv`: Temperature, fuel price, markdowns, holidays  
- `stores.csv`: Store metadata (type, size)  
- `cleaned_retail_data.csv`: Cleaned and merged dataset  

---

## 🔍 Models Trained

| Model              | R² Score | RMSE     | MAE     |
|-------------------|----------|----------|---------|
| Linear Regression | 0.0900   | 21824.98 | 14564.77 |
| Decision Tree      | 0.9640   | 7152.62  | 4954.30 |
| Random Forest      | 0.0866   | 21824.98 | 14564.77 |
| **XGBoost ✅**       | **0.9035** | **7094.16** | **4019.50** |

✅ **XGBoost** was selected as the final model due to its high performance.

---

## 📊 Key Features  
- Cleaned & preprocessed 50,000+ records  
- Feature selection & model evaluation  
- Deployed model using **Streamlit**  
- Developed a **Power BI dashboard** to complement predictions

---

## 📈 Visualizations Included  
- Weekly Sales Trends  
- Store Type & Size Distribution  
- Sales During Holidays vs Non-Holidays  
- Markdown Impact on Sales  
- Monthly and Department-wise Sales

---

## 🛠️ Tools & Technologies  
**Python**, **Pandas**, **NumPy**, **Scikit-learn**, **XGBoost**  
**Matplotlib**, **Seaborn**, **Streamlit**, **Google Colab**, **Power BI**

---

## 📁 Repository Structure

Retail_sales_prediction/ ├── train.csv ├── features.csv ├── stores.csv ├── cleaned_retail_data.csv ├── modeling.ipynb                        # Model training & evaluation ├── app.py                                # Streamlit web app ├── xgboost_model.pkl                     # Trained XGBoost model ├── requirements.txt ├── Retail_sales_prediction_dashboard.pbix # Power BI dashboard └── README.md

---

## 📊 Power BI Dashboard (Bonus)

A Power BI dashboard was built using the same dataset to visualize:

- ✅ Total Retail Sales by Year  
- ✅ Store-wise Sales by Type  
- ✅ Holiday vs Non-Holiday Sales Comparison  
- ✅ Top Performing Stores  
- ✅ Sales Contribution by Store Type  
- ✅ Dynamic filters: year, store type, holiday flag

📄 Included: `Retail_sales_prediction_dashboard.pbix`

---

## 👨‍💻 About Me

**Irfan Hussain**  
🎓 B.Sc. Computer Science (Data Science & AIML)  
📍 Yenepoya University, Mangalore  
🔍 Passionate about building predictive ML pipelines, dashboards, and solving real-world business problems through data.

🔗 [Irfan Hussain](https://www.linkedin.com/in/irfanhussain-irfu)

---

## ✅ Future Improvements  
- Add holiday effect time series features  
- Test on unseen years  
- Automate weekly retraining pipeline  
- Extend dashboard to mobile-friendly Power BI service
