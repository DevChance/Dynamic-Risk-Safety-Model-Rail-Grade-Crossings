---

# **🚦 Forecasting Safety: The Meteorological Impact on Highway-Rail Grade Crossing Safety**  

## **📌 Project Overview**  
Traditional risk models for highway-rail grade crossings rely heavily on **historical accident data** and **static infrastructure characteristics**, often failing to consider **real-time weather conditions, visibility, and traffic volume fluctuations**.  

This project introduces a **dynamic risk assessment model** that integrates **meteorological data and real-time traffic variables** to **enhance safety predictions and emergency response strategies**. By modeling **how weather impacts crossing safety in real-time**, this approach helps **reduce incidents, optimize safety investments, and inform smarter transportation planning**.  

---

## **🌍 Why This Project Matters**  
Rail crossings are **critical intersections** where railroads meet vehicle and pedestrian traffic. Despite safety advancements, **accidents at these crossings remain a leading cause of railway-related fatalities**. The risks are significantly **exacerbated by poor visibility, adverse weather conditions, and fluctuating traffic levels**.  

### 🔹 **Key Challenges of Traditional Risk Models**  
- **Static Data Usage** → Doesn’t account for **real-time weather or traffic conditions**.  
- **Lack of Meteorological Impact Integration** → Weather and visibility factors **directly affect accident risks but are often ignored**.  
- **Limited Predictive Capabilities** → Focuses on **historical trends rather than dynamic risk forecasting**.  

### 🔹 **How This Project Solves These Issues**  
✔ **Dynamically adjusts risk scores** based on **live & forecasted weather conditions**.  
✔ **Introduces the Meteorological Impact Score (MIS)** to **quantify visibility, precipitation, and illumination effects**.  
✔ **Integrates real-time traffic exposure** to enhance **predictive accuracy**.  
✔ **Uses data visualization** to **identify high-risk crossings and trends** for better **urban planning and safety interventions**.  

---

## **🛠 Key Features & Innovations**  
| **Feature** | **Traditional Models** | **This Project** |
|------------|----------------------|-----------------|
| **Data Source** | Static historical accident data | **Real-time weather & traffic variables** |
| **Risk Calculation** | Based on **past incidents** | **Predicts risk dynamically using environmental & operational data** |
| **Weather Integration** | **Limited or absent** | **Quantifies meteorological impact using the MIS sub-model** |
| **Traffic Volume Consideration** | Uses **fixed averages** | Uses **real-time AADT (Annual Average Daily Traffic) & TDT (Total Daily Trains)** |
| **Data Visualization** | Often **tabular or basic statistics** | Uses **Matplotlib-generated charts & graphs** to analyze risk patterns |

---

## **📊 How It Works: The Two-Tier Model Approach**  
This project consists of two key models:

### **🔹 1. Meteorological Impact Score (MIS) Sub-Model**  
> **Purpose:** Quantifies how weather and visibility conditions affect safety at rail crossings.

📌 **Key Components**:  
- **Visibility Analysis** → Categorizes natural lighting into **Dawn, Day, Dusk, and Dark**.  
- **Weather Impact Calculation** → Classifies conditions as **Clear, Cloudy, or Rainy**, assigning each a **risk weight**.  
- **Artificial Illumination Adjustment** → Determines whether **artificial lighting mitigates low-visibility risks**.  

📊 **Formula:**  
```math
MIS = V_{illuminated} + W
```
Where:  
- **$V_{illuminated}$** → Adjusted visibility score based on **time of day and artificial lighting**.  
- **$W$** → Weather impact factor, scaled based on **severity**.  

---

### **🔹 2. Meteorological-Adjusted Risk Calculator (M.A.R.C.) Model**  
> **Purpose:** Uses **MIS** to calculate a **dynamic, real-time risk score** for rail crossings by integrating meteorological impact with **traffic exposure and safety infrastructure**.

📊 **MARC Formula:**  
```math
MARC = e^{\left[ a(1 + MIS \cdot x_1) (M - B) + b \cdot CE_M - c(W \cdot (1 - MIS \cdot x_3)) \right]}
```  

---

## **📌 Variable Breakdown: Key Components of the M.A.R.C. Model**  

| **Variable** | **Definition** |
|-------------|---------------|
| **$MARC$** | The final **risk score** for a highway-rail grade crossing under specific conditions. |
| **$a, b, c$** | **Calibrated coefficients** derived from historical data to fine-tune the model’s accuracy. |
| **$MIS$** | **Meteorological Impact Score**, a measure of how weather, visibility, and artificial lighting affect risk. |
| **$x_1, x_2, x_3$** | **Adjustment parameters** that scale meteorological effects on risk calculations. |
| **$M$** | **Maximum train speed** (in mph) at the crossing, influencing risk severity. |
| **$B$** | **Baseline train speed**, representing the lowest speed threshold used for comparison. |

📊 **Equation for $CE_M$:**  
```math
CE_M = (AADT \times TDT) \times \left(1 - \frac{MIS}{x_2} \right)
```
where:  
- **AADT** = Annual Average Daily Traffic (vehicles per day).  
- **TDT** = Total Daily Trains (trains per day).  
- **MIS/x_2** adjusts for **meteorological conditions** affecting crossing exposure.  

---

## **📂 Project Files & Description**
| **File** | **Description** | **Link** |
|----------|---------------|----------|
| **📄 Math111a Final Project Meteorological Impact on Rail Grade Crossings.pdf** | The **full project report**, explaining the methodology, analysis, and conclusions. | [🔗 View Report](#) |
| **📊 Forecasting Safety: The Meteorological Impact on Highway-Rail Grade Crossing Safety.pdf** | The **project presentation slides**, summarizing key findings and visualizations. | [🔗 View Presentation](#) |
| **📜 Percentage Change.py** | Computes **percentage changes in risk scores** based on different meteorological conditions using exponential functions. | [🔗 View Code](#) |
| **🖥️ M.A.R.C. (New Iteration Simulation).py** | Runs **real-world crossing risk simulations** using train speed, traffic volume, and weather data, applying the **MARC formula**. | [🔗 View Code](#) |

---

## **🚀 Future Enhancements**  
✔ **Live Weather Data Feeds** – Integrate **real-time weather APIs** to dynamically update risk assessments.  
✔ **Automated Reporting System** – Develop a **system that alerts local authorities and transportation agencies** when risk levels reach a critical threshold.  
✔ **Real-Time Traffic Integration** – Use **live vehicle and train traffic feeds** to enhance the accuracy of crossing exposure calculations.  
✔ **Machine Learning Optimization** – Train **predictive models** using historical incident data alongside real-time weather updates for **adaptive risk forecasting**.  

---

## **💡 Final Thoughts**  
This project presents a **groundbreaking approach** to rail crossing safety by **dynamically integrating meteorological factors into risk assessment models**. Unlike traditional methods that **rely solely on historical data**, this model **proactively adjusts risk scores based on real-time conditions**, making it a powerful tool for **transportation safety planning and emergency response teams**.  

**Interested in discussing or collaborating?** Feel free to reach out! 🚆  

---
