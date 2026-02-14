# 📊 Vendor Brand Performance SQL-Python-PowerBI Analytics  
### Financial Performance & Vendor Profitability Analysis

---

## 📑 Table of Contents

- [Project Summary](#project-summary)
- [Business Objectives](#business-objectives)
- [Project Architecture](#project-architecture)
- [Technology Stack](#technology-stack)
- [Repository Structure](#repository-structure)
- [Executive Dashboard Overview](#executive-dashboard-overview)
- [Financial KPIs Engineered](#financial-kpis-engineered)
- [Key Business Insights](#key-business-insights-generated)
- [Financial Impact](#financial-impact)
- [How to Run the Project](#how-to-run-the-project)
- [Skills Demonstrated](#skills-demonstrated)
- [Author](#author)

---

## 📌 Project Summary

This project delivers an end-to-end financial analytics solution to evaluate vendor and brand performance using **MySQL, Python, and Power BI**.

The objective is to transform raw transactional data into strategic financial insights that support:

- Profitability optimization  
- Cost control  
- Vendor evaluation  
- Working capital management  
- Revenue concentration analysis  

---

## 🎯 Business Objectives

The analysis was designed to answer key financial questions:

- Which vendors generate the highest revenue?
- Which vendors provide the strongest margins?
- Where is capital locked in low-performing inventory?
- Are we overly dependent on specific vendors?
- Which brands contribute revenue but reduce overall profitability?

---

## 🏗️ Project Architecture

```text
MySQL Database (Raw Financial Data)
        ↓
Python (Data Cleaning & KPI Engineering)
        ↓
Exploratory Financial Analysis (Jupyter Notebooks)
        ↓
Processed Financial Dataset (CSV)
        ↓
Power BI Executive Dashboard
```

---

## 🛠️ Technology Stack

- **Database:** MySQL  
- **Programming:** Python  
- **Libraries:** Pandas, NumPy, MySQL Connector  
- **Analysis:** Jupyter Notebook  
- **Visualization:** Power BI  
- **Business Logic:** DAX  
- **Version Control:** Git & GitHub  

---

## 📂 Repository Structure

```text
vendor_brand_performance/
│
├── dashboard/
│   └── vendor_brand_performance_dashboard.pbix
│
├── data/
│   ├── database_dump.sql
│   ├── raw_data.csv
│   └── processed_data.csv
│
├── images/
│   └── vendor-brand-performance-dashboard.png
│
├── notebooks/
│   ├── exploratory_data_analysis.ipynb
│   └── vendor_performance_analysis.ipynb
│
├── src/
│   ├── ingestion_mysql_db.py
│   └── get_vendor_summary.py
│
└── README.md
```

---

## 📊 Executive Dashboard Overview

The Power BI dashboard provides a financial performance snapshot including:

- Total Sales  
- Total Purchase  
- Gross Profit  
- Profit Margin %  
- Unsold Capital  
- Vendor Contribution %  
- Top Performing Vendors  
- Low Performing Vendors  
- Sales vs Margin Scatter Analysis  

![Vendor Brand Performance Dashboard](images/vendor-brand-performance-dashboard.png)

---

## 📈 Financial KPIs Engineered

### 1️⃣ Gross Profit

```
Gross Profit = Total Sales – Total Purchase
```

### 2️⃣ Profit Margin %

```
Profit Margin = Gross Profit / Total Sales
```

### 3️⃣ Vendor Contribution %

```
Vendor Sales / Total Sales
```

### 4️⃣ Vendor Segmentation Strategy

- High Revenue – High Margin → Strategic Vendors  
- High Revenue – Low Margin → Renegotiation Candidates  
- Low Revenue – Low Margin → Phase-Out Candidates  

---

## 🔎 Key Business Insights Generated

- Identified vendors contributing less than 2% of revenue but consuming working capital  
- Detected high-sales vendors with declining margin efficiency  
- Highlighted vendor concentration risk in top revenue contributors  
- Measured unsold capital exposure tied to low-performing brands  
- Provided data-driven recommendations for vendor contract review  

---

## 💼 Financial Impact

This analysis supports:

- Procurement cost optimization  
- Margin improvement strategy  
- Vendor rationalization  
- Working capital control  
- Strategic sourcing decisions  

The dashboard enables management to move from reactive reporting to proactive financial decision-making.

---

## ⚙️ How to Run the Project

1. Clone this repository.  
2. Create a MySQL database (e.g., `vendor_brand_performance`).  
3. Load the CSV files into the database using the provided SQL script or MySQL import:
4. Run the Python scripts:
   ```
   python src/ingestion_mysql_db.py
   python src/get_vendor_summary.py
   ```
5. Open the Power BI file:
   ```
   dashboard/vendor_brand_performance_dashboard.pbix
   ```
6. Refresh the dataset  

---

## 🎯 Skills Demonstrated

- Financial Performance Analysis  
- Revenue & Margin Modeling  
- Vendor Profitability Assessment  
- Cost Structure Evaluation  
- Working Capital Analysis  
- SQL Data Extraction  
- ETL Pipeline Development  
- KPI Engineering  
- Power BI Executive Reporting  

---

## 👤 Author

**Muhammad Afzal**  
Financial Analytics | Vendor Performance | Business Intelligence  

Open to Financial Analyst / BI Analyst opportunities.
