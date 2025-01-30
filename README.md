# **Dynamic Risk Modeling for Rail Crossings**

## **Overview**
The **Dynamic Risk Modeling for Rail Crossings** project introduces an advanced approach to rail safety assessment by integrating **statistical modeling**, **real-world data analysis**, and **simulation techniques**. Unlike traditional static evaluations, this project dynamically quantifies risk factors, enabling more proactive and precise interventions. 

A key innovation in this project is the **Meteorological-Adjusted Risk Calculator (M.A.R.C.)**, which assesses how environmental and operational factors—such as weather, traffic patterns, and safety infrastructure—impact crossing safety. By leveraging **data-driven insights**, this project provides actionable recommendations for improving highway-rail grade crossings.

---

## **💡 Why This Project Matters**
Rail crossings are critical intersections where road and rail traffic meet, posing significant safety risks. Accidents at these locations often result in severe casualties and financial losses. Factors like adverse weather conditions, poor visibility, and insufficient safety measures exacerbate these dangers. 

This project aims to **enhance risk prediction and mitigation strategies** by:
- Quantifying the impact of weather and lighting conditions with the **Meteorological Impact Score (MIS)**.
- Dynamically adjusting risk evaluations using the **M.A.R.C. model**.
- Providing **data-driven insights** to optimize rail crossing safety measures.

By implementing this model, municipalities, transportation agencies, and railway operators can:
- **Reduce accident rates** by proactively identifying high-risk crossings.
- **Optimize infrastructure investments** based on real-world data.
- **Improve decision-making** using predictive analytics.

---

## **✨ Key Features & Innovations**
### **1. Meteorological Impact Score (MIS)**
The **MIS** quantifies how weather and lighting conditions affect crossing safety by calculating:
- **Visibility Index (VI)**: Measures clear sight distance for drivers.
- **Lighting Factor (LF)**: Adjusts for daylight and artificial lighting conditions.
- **Weather Severity Index (WSI)**: Evaluates adverse weather impact.

### **2. Dynamic Risk Calculator (M.A.R.C.)**
This tool integrates:
- **Traffic Exposure (TE)**: Measures vehicle and train flow at crossings.
- **Weather Adjustments (WA)**: Accounts for weather-based risk variations.
- **Safety Measures (SM)**: Quantifies the presence of gates, warning lights, and signage.

The model outputs a **Dynamic Risk Score (DRS)**, prioritizing crossings for safety improvements.

### **3. Monte Carlo Simulation Framework**
Simulations validate the **M.A.R.C. model’s** predictive accuracy by:
- Running **10,000+ iterations** to assess risk variations.
- Evaluating safety measures under diverse environmental conditions.
- Identifying **critical high-risk crossings** for immediate intervention.

### **4. Data Visualization**
- **Heatmaps** highlight high-risk crossings.
- **Line Graphs** track weather-related accident trends.
- **Bar Charts** compare the effectiveness of safety interventions.

---

## **🔧 How to Get Started**
### **Clone the Repository**
```bash
git clone https://github.com/DevChance/Dynamic-Risk-Modeling-Rail-Crossings.git
cd Dynamic-Risk-Modeling-Rail-Crossings
```
### **Install Dependencies**
```bash
pip install -r requirements.txt
```
### **Run the Simulation**
```bash
python MARC_Simulation.py
```

---

## **📊 Technologies Used**
- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Matplotlib
- **Tools**: Jupyter Notebook, PyCharm
- **Methods**: Statistical modeling, Monte Carlo simulation, Data visualization

---

## **📄 Research & Documentation**
- **[Project Report](./Math111aProject_Report.pdf)**: In-depth methodology and findings.
- **[Presentation Slides](./Forecasting_Safety_Slide_Presentation.pdf)**: Summary of key results.

---

## **🚀 Future Enhancements**
- **Live Weather Data Integration**: Implement real-time weather APIs.
- **Machine Learning Expansion**: Improve predictions with regression models.
- **Web Dashboard**: Develop an interactive interface for stakeholders.



