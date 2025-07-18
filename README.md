# GloBox A/B Test Analysis

## 🧪 The Project  
Analyze the results of an A/B test for a website banner for GloBox, a fictional company, and provide a data-backed recommendation to stakeholders about whether to launch the new banner experience.

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

## 🧠 Process  
1. **Data cleaning, transformation, and exploratory analysis** were conducted in **Beekeeper Studio** using PostgreSQL.
2. Cleaned datasets were **exported to Tableau Desktop** for visual exploration.
3. The same data was also analyzed in **Google Sheets** for:
   - Hypothesis testing  
   - Confidence interval estimation  
   - Power analysis
4. A second dataset was exported for **novelty effect analysis** in Tableau.
5. Final results and visual insights were compiled in the **attached slide deck and technical report**.

---

## 🔍 Key Insights  
- 📈 The **treatment group** showed a **significant lift in conversion rate** but no notable increase in revenue.
- 🌍 Highest conversion rates were seen among:
  - Users from **Mexico**
  - **Male** users
  - Users on **Android** devices
- 🕒 **No novelty effects** were observed over time.

---

## ✅ Recommendation  
Since only one of the two business objectives was achieved, I recommended **re-running the test** with modifications, outlined in detail in the slide deck and technical report.

---

## 🗂 Files Included

- `init_schema.sql` – Contains all queries used for:
  - Exploratory analysis
  - Conversion rate calculations
  - Group comparisons
  - Tableau/Sheets-ready extracts
- `README.md` – You’re reading it!
- Optional: Slide deck (if added to the repo)

> ⚠️ Note: Due to lack of schema permissions on the Neon-hosted PostgreSQL database, some DDL operations (like `CREATE TABLE`) may not execute if tested directly. All code was written and tested in Beekeeper Studio using existing datasets.

---

## 🧰 Tools Used
- PostgreSQL (Neon via Beekeeper Studio)
- Tableau Desktop
- Google Sheets
- GitHub
