# 📊 Vendor Brand Performance Analytics  
### End-to-End Financial Intelligence Solution (SQL • Python • Power BI)

---

## 📑 Table of Contents

- [Project Summary](#project-summary)
- [Business Problem](#business-problem)
- [Solution Architecture](#solution-architecture)
- [Executive Dashboard](#executive-dashboard)
- [Financial KPIs](#financial-kpis)
- [Key Insights](#key-insights)
- [Business Impact](#business-impact)
- [Technology Stack](#technology-stack)
- [Repository Structure](#repository-structure)
- [How to Run](#how-to-run)
- [Skills Demonstrated](#skills-demonstrated)
- [Author](#author)

---

<a id="project-summary"></a>
## 📌 Project Summary

This project delivers a full financial analytics pipeline designed to evaluate **vendor profitability, revenue concentration, and working capital efficiency**.

Using **MySQL, Python, and Power BI**, raw transactional data is transformed into executive-level insights that support:

- Margin optimization  
- Strategic vendor negotiation  
- Procurement cost control  
- Inventory risk management  
- Revenue diversification strategy  

---

<a id="business-problem"></a>
## 🎯 Business Problem

Organizations often face challenges such as:

- High revenue but declining margins  
- Capital locked in slow-moving inventory  
- Vendor concentration risk  
- Poor visibility into vendor profitability  
- Limited insight into revenue-to-margin efficiency  

---

<a id="solution-architecture"></a>
## 🏗️ Solution Architecture

```
MySQL (Raw Financial Data)
        ↓
Python (Data Cleaning + KPI Engineering)
        ↓
Exploratory Financial Analysis (Jupyter)
        ↓
Processed Financial Dataset (CSV)
        ↓
Power BI Executive Dashboard
```

---

<a id="executive-dashboard"></a>
## 📊 Executive Dashboard

The Power BI dashboard provides:

![Vendor Brand Performance Dashboard](images/vendor-brand-performance-dashboard.png)

---

<a id="financial-kpis"></a>
## 📈 Financial KPIs

### Gross Profit
```
Gross Profit = Total Sales – Total Purchase
```

### Profit Margin %
```
Profit Margin = Gross Profit / Total Sales
```

### Vendor Contribution %
```
Vendor Sales / Total Sales
```

---

<a id="key-insights"></a>
## 🔎 Key Insights

- Vendors contributing <2% revenue but consuming working capital  
- High-revenue vendors with weak margin efficiency  
- Vendor concentration risk in top contributors  
- Unsold capital exposure in low-performing brands  
- Data-driven vendor rationalization model  

---

<a id="business-impact"></a>
## 💼 Business Impact

- Cost reduction opportunities  
- Margin improvement strategy  
- Working capital optimization  
- Vendor contract renegotiation support  
- Strategic sourcing decisions  

---

<a id="technology-stack"></a>
## 🛠️ Technology Stack

- MySQL  
- Python (Pandas, NumPy)  
- Power BI  
- DAX  
- Jupyter Notebook  
- Git & GitHub  

---

<a id="repository-structure"></a>
## 📂 Repository Structure

```
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

<a id="how-to-run"></a>
## ⚙️ How to Run

1. Clone repository  
2. Create MySQL database `vendor_brand_performance`  
3. Import data  
4. Run:

```
python src/ingestion_mysql_db.py
python src/get_vendor_summary.py
```

5. Open Power BI file and refresh dataset  

---

<a id="skills-demonstrated"></a>
## 🎯 Skills Demonstrated

- Financial Performance Analysis  
- Vendor Profitability Modeling  
- Revenue & Margin Analytics  
- Working Capital Analysis  
- ETL Development  
- Power BI Executive Reporting  

---

<a id="author"></a>
## 👤 Author

**Muhammad Afzal**  
Financial Analytics | Vendor Performance | Business Intelligence  

Open to Financial Analyst / BI Analyst opportunities.