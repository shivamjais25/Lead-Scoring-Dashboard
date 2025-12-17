# 📊 Tech Professional Lead Ranking & Scoring Dashboard

A **Streamlit web app** that ranks and scores tech professionals (leads) using clear and configurable business rules based on **role seniority, company tier, location, and work mode**.

This project uses **dummy/sample data** and is intended for **learning, demonstration, and portfolio purposes**.

---

## 🚀 Features

- 🏆 Automatic **ranking** of professionals based on scores
- 🧮 Rule-based **Probability Score (0–100)**
- 🔍 Search by **Name, Title, Company, or Location**
- 📋 Interactive and responsive data table
- ⬇️ **Download filtered results** as CSV
- ⚙️ Transparent and editable scoring logic

---

## 🛠️ Tech Stack

- **Python**
- **Pandas** – data handling and transformation
- **Streamlit** – interactive web dashboard

---

## 📊 Scoring Logic

Each professional is scored based on:

1. **Role Seniority**
   - Senior roles → higher score
   - Engineer / Scientist / Developer → mid-level score

2. **Company Tier**
   - Big Tech companies: Google, Microsoft, Meta, Amazon, Tesla

3. **Location**
   - US tech hubs (Bay Area, Seattle, Austin)
   - India-based professionals

4. **Work Mode**
   - Remote
   - Hybrid

> Scores are capped at **100**.

---

## ⚖️ Configurable Weights

```python
WEIGHTS = {
    "senior_role": 30,
    "mid_role": 20,
    "big_tech_company": 30,
    "india_location": 10,
    "us_hub_location": 20,
    "remote": 20,
    "hybrid": 10
}

