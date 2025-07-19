# GloBox A/B Test Analysis

## 🧪 The Project  
Analyze the results of an A/B test for a website banner for GloBox, a fictional company, and provide a data-backed recommendation to stakeholders on whether to launch the new banner experience.

---

## 🏢 Business Context  
GloBox is primarily known for boutique fashion items and high-end decor. However, their food and drink offerings have grown significantly in recent months. To increase visibility and drive revenue in this category, they launched an A/B test on their **mobile website**, featuring a promotional banner at the top.

---

## 🎯 Objectives  
- **Boost visibility** of the *Food & Drink* section  
- **Increase revenue**

---

## 📊 Key Metrics  
- **Conversion Rate / Conversion Lift**  
- **Average Amount Spent per User**

---

## 🧠 Process Overview  
1. **Data cleaning, transformation, and exploratory analysis** were conducted in **Beekeeper Studio** using PostgreSQL.
2. Cleaned datasets were **exported to Tableau Desktop** for visual exploration.
3. The same dataset was also analysed with **Python** for:
   - Hypothesis testing
   - Effect size estimation
   - Confidence intervals  
4. A separate export was created to analyse **novelty effects**.
5. Final recommendations and visual insights were compiled in the attached **slide deck**.

---

## 🔍 Key Insights  
- 📈 The **treatment group** showed a **significant increase in conversion rate**, but no meaningful change in revenue.
- 🌍 Highest conversion rates were seen among:
  - Users from **Mexico**
  - **Male** users
  - **Android** users
- 🕒 **No novelty effects** were observed over time.

---

## ✅ Recommendation  
Since only one of the two business goals was met, I recommended **re-running the test** with adjusted targeting and design, as detailed in the slide deck and technical report.

---

## 🗂 Files Included

- `EDA.sql` – All SQL queries used for:
  - Exploratory analysis  
  - Conversion metrics  
  - Group comparisons  
  - Tableau/Python exports
- `README.md` – This document
- `Globox_statistical_analysis.py` – Python script containing:
  - Hypothesis testing on conversion rates and average spend
  - Confidence interval calculations
  - Effect size estimation using Cohen's h and d
  - Visualisations with error bars
- **Slide deck** – Final summary presentation (attached separately)

---

## 🛠️ Tools Used
- **PostgreSQL** (via Beekeeper Studio)
- **Tableau Desktop**
- **Python**
- **GitHub**

---

## 🔐 Database Access & Notes

> ⚠️ Some DDL operations (like `CREATE TABLE`) may fail when run directly due to a lack of schema privileges on the hosted Neon DB.  
> All SQL was written, tested, and exported using Beekeeper Studio.

### 🔗 Connection Info (Read-Only)

'postgres://Test:bQNxVzJL4g6u@ep-noisy-flower-846766-pooler.us-east-2.aws.neon.tech/Globox'

