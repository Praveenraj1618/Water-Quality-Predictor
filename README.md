# 💧 Water Quality Prediction Dashboard

A full-stack machine learning dashboard that predicts pollutant concentrations in water bodies and evaluates their overall quality. Built with Flask and powered by a `MultiOutputRegressor` wrapped around an `XGBoostRegressor`, the system enables users to interactively explore results through a sleek web interface.

The application features dark mode, CSV/PDF export, dynamic pollutant visualization, and a pollutant-wise safety classification — all integrated in a 100% local Python-Flask environment.

---

## 📌 Predicted Water Quality Parameters

The model predicts multiple water quality parameters such as:

- **NH4** – Ammonium
- **BSK5** – Biological Oxygen Demand (BOD5)
- **Suspended** – Suspended Solids (Colloids)
- **O2** – Dissolved Oxygen
- **NO3** – Nitrate
- **NO2** – Nitrite
- **SO4** – Sulfate
- **PO4** – Phosphate
- **CL** – Chloride

---

## 📊 Model Performance

The model was evaluated using:

- ✅ **R² Score**
- 📉 **Mean Squared Error (MSE)**

Performance was acceptable across all parameters, and **XGBoost** showed the best generalization compared to alternatives like Linear Regression and Random Forest.

---

## 🔗 Model Download

You can download the trained model and column structure here:

📦 [`pollution_model.pkl`](https://drive.google.com/file/d/1fzg02RD50EbjwT_-xIBFxZQqszbU59w6/view?usp=sharing)

---

## 🚀 Features

- 📈 Multi-pollutant prediction from Station ID & Year
- 🟥 Pollutant safety classification (Safe / Polluted)
- 📊 Dynamic bar chart with color-coded status
- 🌙 Dark mode toggle with persistent preference
- 📄 Export results to **CSV** and **PDF**
- 🧭 Drop-down for all 22 water monitoring stations
- 🖼️ Clean UI with sidebar-panel layout (20:80)

---

## 🧪 Tech Stack

- **Backend:** Flask, Pandas, Joblib
- **ML Model:** MultiOutputRegressor + XGBoost
- **Visualization:** Chart.js
- **Exporting:** xhtml2pdf, CSV
- **UI:** HTML, CSS, JS (dark mode, responsive)

---

## 🏫 Internship Information

- **Internship Type**: AICTE Virtual Internship  
- **Organization**: Edunet Foundation  
- **Sponsor**: Shell  
- **Duration**: June 2025 (4 weeks)  
- **Focus**: AI & ML for Green Tech and Environmental Monitoring  

---


