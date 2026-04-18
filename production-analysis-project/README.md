# Production Data Analysis Project (End-to-End)

## Overview

This project simulates a real-world production data analysis workflow aligned with manufacturing environments such as Panasonic.

The objective is to transform raw production data into actionable insights to support:

* Production efficiency improvement
* Product quality monitoring
* Data-driven decision making

This project covers the full data pipeline:
Python → SQL → Power BI

---

## Business Problem

Production teams often face challenges in:

* Maintaining consistent product quality
* Identifying inefficiencies in production processes
* Understanding which factors impact performance

This project aims to answer:

* What factors influence product quality?
* Does higher efficiency always improve quality?
* Which suppliers or production settings perform best?

---

## 🧰 Tools & Technologies

* **Python (Pandas)** → Data Cleaning & Preprocessing
* **SQL (SQLite)** → Data Storage & Analytical Queries
* **Power BI** → Dashboard & Visualization
* **GitHub** → Documentation & Version Control

---

## 🗂️ Project Structure

```id="proj-structure"
production-analysis-project/
│
├── Data/
│   ├── production_data.csv
│   └── Clean_Production_Data.csv
│
├── Python/
│   └── cleaning_sqlite.py
│
├── Database/
│   └── production.db
│
├── SQL/
│   ├── Efficiency Analysis.sql
│   ├── Quality per Supplier.sql
│   ├── Quality per Pigment.sql
│   ├── Efficiency_Analysis.png
│   ├── Quality_Per_Supplier.png
│   └── Quality_per_pigment.png
│
├── Dashboard_PowerBI/
│   ├── Production Data.pbix
│   ├── Dashboard.png
│   └── Decomposition Tree.png
│
└── README.md
```

---

## 🔄 Data Pipeline

### 1. Data Cleaning & Preprocessing (Python)

End-to-end pipeline: **Load → Clean → Transform → Validate → Export → SQL**

* Cleaned raw production data by handling missing values and inconsistent records
* Standardized categorical variables (e.g., supplier, production category) for consistent analysis
* Normalized key numerical features (quality score, efficiency) to enable meaningful comparison
* Validated data integrity to ensure reliability for downstream analysis
* Exported cleaned dataset for SQL-based analysis and dashboard integration

This step ensures that production data is reliable, consistent, and ready for decision-making. Improved data quality to support accurate production performance analysis and reporting.


---

### 2. Database & SQL Analysis

Data stored in SQLite database and analyzed using SQL queries.

#### Key SQL Analyses:

**1. Efficiency Analysis**

* Measures production efficiency trends
* Identifies performance variation
* Helps evaluate process optimization

**2. Quality per Supplier**

* Compares product quality across suppliers
* Identifies best-performing supplier
* Supports supplier decision-making

**3. Quality per Pigment**

* Analyzes impact of material/pigment on quality
* Identifies optimal material usage

SQL queries are designed to replicate real production reporting needs.

---

### 3. Data Visualization (Power BI)

Interactive dashboard includes:

* KPI Monitoring:

  * Average Quality Score
  * Average Efficiency Score

* Analysis:

  * Supplier performance comparison
  * Category-based quality analysis
  * Monthly trend analysis
  * Scatter plot (Efficiency vs Quality)

* Advanced Analysis:

  * Decomposition Tree (Root Cause Analysis)

---

## Key Insights

* Product quality is influenced by:

  * Mixing speed
  * Supplier
  * Pigment type

* No strong linear relationship between efficiency and quality
  → Improving efficiency does not always increase quality

* Certain suppliers consistently produce higher quality output

---

## 📈 Dashboard Preview

### Main Dashboard

![Dashboard](Dashboard_PowerBI/Dashboard.png)

### Root Cause Analysis

![Decomposition Tree](Dashboard_PowerBI/Decomposition%20Tree.png)

---

## 💡 Business Impact

This project demonstrates how data can be used to:

* Improve production decision-making
* Identify optimal production configurations
* Enhance product quality control
* Support continuous improvement in manufacturing

---
## 📂 Data Source

Dataset used in this project:

* **Production Data Dataset**
  
  Source: Kaggle

  Author: Minamagdy24

  Link: https://www.kaggle.com/datasets/minamagdy24/production-data

This dataset was used as a simulation of real-world production data for analytical and learning purposes. The dataset has been modified and cleaned to fit analytical requirements.

## Skills Demonstrated

* Data Cleaning & Preprocessing
* SQL Query & Database Handling
* Data Visualization & Dashboarding
* Analytical Thinking & Problem Solving
* Translating Data into Business Insights

---

## 👤 About Me
**FITRIA ROZI**

I am a Physics graduate transitioning into Data Analytics, with strong analytical and problem-solving skills.
This project reflects my ability to:

* Work with real-world data
* Build end-to-end data solutions
* Deliver actionable insights for business use cases

---

## 📬 Contact
* LinkedIn: www.linkedin.com/in/fitria-rozi-6a344a1b1
* Email: fitria100319@gmail.com

---

⭐ If you find this project useful, feel free to give it a star!

