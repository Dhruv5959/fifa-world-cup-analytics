# ⚽ Does Money Buy Success?

# FIFA World Cup Analytics (2010–2022)

A data analytics project investigating whether higher squad market values lead to greater FIFA World Cup success using **Python** for data analysis and **Power BI** for interactive dashboard visualization.

---

## 📑 Table of Contents

<ol>
  <li><a href="#overview">Overview</a></li>
  <li><a href="#business-question">Business Question</a></li>
  <li><a href="#dataset">Dataset</a></li>
  <li><a href="#tools--technologies">Tools & Technologies</a></li>
  <li><a href="#methodology">Methodology</a></li>
  <li><a href="#key-findings">Key Findings</a></li>
  <li><a href="#results">Results</a></li>
  <li><a href="#project-structure">Project Structure</a></li>
  <li><a href="#how-to-run">How to Run</a></li>
  <li><a href="#visualizations">Visualizations</a></li>
  <li><a href="#interactive-dashboard">Interactive Dashboard</a></li>
  <li><a href="#dashboard-preview">Dashboard Preview</a></li>
  <li><a href="#conclusion">Conclusion</a></li>
  <li><a href="#author">Author</a></li>
</ol>

---

## Overview

This project analyzes FIFA World Cup team data from **2010–2022** to determine whether expensive squads perform better in the tournament.

Using **Python** for data cleaning, feature engineering, and statistical analysis, along with **Power BI** for interactive dashboard development, the project investigates whether higher squad market values translate into greater tournament success.

A custom **Return on Investment (ROI)** metric was developed to compare tournament performance relative to squad market value, helping identify both overperforming and underperforming teams.

---

## Business Question

**Does money buy success in the FIFA World Cup?**

---

## Dataset

### Source

https://www.kaggle.com/datasets/harrachimustapha/fifa-world-cup-team-dataset

### Coverage

- FIFA World Cup
- 2010
- 2014
- 2018
- 2022
- 128 Team-Tournament Records

---

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python | Data Analysis |
| Pandas | Data Cleaning & Feature Engineering |
| NumPy | Numerical Calculations |
| Matplotlib | Exploratory Data Visualization |
| **Power BI** | Interactive Dashboard & Business Intelligence |
| Excel | Dataset Preparation |

---

## Methodology

### Data Cleaning

- Loaded and validated the dataset
- Converted squad values into millions (€M)
- Created a unique Team-Year identifier

### Feature Engineering

Created:

- **Tournament Performance Score**
- **ROI (Return on Investment)**

### Tournament Performance Score

| Stage | Score |
|------|------:|
| Group Stage | 0 |
| Quarter Final | 2 |
| Semi Final | 3 |
| Runner-up | 4 |
| Winner | 5 |

### ROI Formula

```text
ROI = Tournament Performance Score / Squad Market Value
```

### Analysis

- Correlation Analysis
- ROI Analysis
- Spending Trend Analysis
- Biggest Tournament Disappointments
- Year-wise Spending vs Success

## Key Findings

- Squad market value and tournament success show a **moderate positive correlation (≈0.47)**.
- Higher spending increases the probability of success but does **not guarantee** it.
- Costa Rica (2014) delivered one of the highest value-for-money performances.
- Spain (2018) and Germany (2018) were among the tournament favourites but exited in the group stage.
- Average squad values increased significantly between 2010 and 2022.

---

## Results

The analysis produced several notable insights:

- **Correlation between Squad Market Value and Tournament Success:** **0.47**
- **Highest ROI Performance:** Costa Rica (2014)
- Average squad market values increased consistently from **2010 to 2022**
- Several high-value squads underperformed despite their financial strength.
- Lower-valued teams repeatedly demonstrated that tactical quality, team cohesion, and execution can outperform financial investment.

---

## Project Structure

```text
fifa-world-cup-analytics/
│
├── data/
│   └── Fifa_master_v2.xlsx
│
├── charts/
│   ├── top_10_roi.png
│   ├── scatter_2010.png
│   ├── scatter_2014.png
│   ├── scatter_2018.png
│   ├── scatter_2022.png
│   ├── biggest_disappointments.png
│   ├── yearly_roi_trend.png
│   └── yearly_spending_trend.png
│
├── dashboard/
│   └── dashboard.png
│
├── analysis.py
├── README.md
└── requirements.txt
```

---

## How to Run

### Clone the repository

```bash
git clone https://github.com/Dhruv5959/fifa-world-cup-analytics.git
```

### Move into the project

```bash
cd fifa-world-cup-analytics
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the analysis

```bash
python analysis.py
```

---

## Visualizations

The project includes:

- Top 10 Value-for-Money Teams
- Spending vs Success (2010)
- Spending vs Success (2014)
- Spending vs Success (2018)
- Spending vs Success (2022)
- Biggest World Cup Disappointments
- Average Squad Spending Trend
- Average ROI Trend

---

## Interactive Dashboard

Alongside the Python analysis, an interactive **Power BI dashboard** was developed to enable users to explore World Cup spending patterns dynamically.

### Dashboard Features

- Filter analysis by FIFA World Cup year (2010–2022)
- View the World Cup Champion for the selected tournament
- Identify the highest Value-for-Money (ROI) teams
- Analyze average ROI trends across World Cups
- Explore the relationship between squad market value and tournament performance
- Identify expensive teams that underperformed expectations
- View key performance indicators including:
  - Teams Analyzed
  - Highest ROI
  - Average Squad Market Value
- Executive insight summarizing the overall findings

---

## Dashboard Preview

### Power BI Dashboard


---

## Conclusion

The analysis indicates that **money improves a team's chances of success, but it does not guarantee tournament performance**.

While higher-valued squads generally progress further, several lower-valued teams consistently outperformed expectations, demonstrating that tactical quality, team cohesion, and execution remain crucial factors in World Cup success.

Overall, the findings reveal a **moderate positive relationship (r = 0.47)** between squad market value and tournament success, suggesting that financial investment increases the probability of success but cannot consistently predict World Cup outcomes.

---

## Author

**Dhruv Patel**

Computer Engineering Student | Aspiring Data Analyst

- GitHub: https://github.com/Dhruv5959
- LinkedIn: https://www.linkedin.com/in/dhruv-patel-7b194a318

---

### ⭐ If you found this project interesting, consider giving it a star!
