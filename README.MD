# ⚽ Does Money Buy Success?

## FIFA World Cup Analytics (2010–2022)

A data analytics project investigating whether higher squad market values lead to greater FIFA World Cup success using Python, Pandas, NumPy, and Matplotlib.

---

## 📑 Table of Contents

<ol>
  <li><a href="#overview">Overview</a></li>
  <li><a href="#business-question">Business Question</a></li>
  <li><a href="#dataset">Dataset</a></li>
  <li><a href="#tools--technologies">Tools & Technologies</a></li>
  <li><a href="#methodology">Methodology</a></li>
  <li><a href="#key-findings">Key Findings</a></li>
  <li><a href="#project-structure">Project Structure</a></li>
  <li><a href="#how-to-run">How to Run</a></li>
  <li><a href="#visualizations">Visualizations</a></li>
  <li><a href="#conclusion">Conclusion</a></li>
  <li><a href="#future-work">Future Work</a></li>
  <li><a href="#author">Author</a></li>
</ol>

---

## Overview

This project analyzes FIFA World Cup team data from **2010–2022** to determine whether expensive squads perform better in the tournament.

A custom **Return on Investment (ROI)** metric was developed to compare tournament performance relative to squad market value, helping identify both overperforming and underperforming teams.

---

## Business Question

**Does money buy success in the FIFA World Cup?**

---

## Dataset

**Source**

https://www.kaggle.com/datasets/harrachimustapha/fifa-world-cup-team-dataset

**Coverage**

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
| Matplotlib | Data Visualization |
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

**Tournament Performance Score**

| Stage | Score |
|------|------:|
| Group Stage | 0 |
| Quarter Final | 2 |
| Semi Final | 3 |
| Runner-up | 4 |
| Winner | 5 |

**ROI Formula**

```text
ROI = Tournament Performance Score / Squad Market Value
```

### Analysis

- Correlation Analysis
- ROI Analysis
- Spending Trend Analysis
- Biggest Tournament Disappointments
- Year-wise Spending vs Success

---

## Key Findings

- Squad market value and tournament success show a **moderate positive correlation (≈0.47)**.
- Higher spending increases the probability of success but does **not guarantee** it.
- Costa Rica (2014) delivered one of the highest value-for-money performances.
- Spain (2018) and Germany (2018) were among the tournament favourites but exited in the group stage.
- Average squad values increased significantly between 2010 and 2022.

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
├── analysis.py
├── README.md
└── requirements.txt
```

---

## How to Run

Clone the repository

```bash
git clone https://github.com/Dhruv5959/fifa-world-cup-analytics.git
```

Move into the project

```bash
cd fifa-world-cup-analytics
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

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

> Add screenshots here after pushing the project.

---

## Conclusion

The analysis indicates that **money improves a team's chances of success, but it does not guarantee tournament performance**.

While higher-valued squads generally progress further, several lower-valued teams consistently outperformed expectations, demonstrating that tactical quality, team cohesion, and execution remain crucial factors in World Cup success.

---

## Future Work

- Build an interactive Power BI dashboard
- Deploy a web dashboard
- Develop a 2026 World Cup prediction model
- Add interactive filters and player-level analysis

---

## Author

**Dhruv Patel**

- GitHub: https://github.com/Dhruv5959
- LinkedIn: https://www.linkedin.com/in/dhruv-patel-7b194a318