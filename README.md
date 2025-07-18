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
3. The same dataset was also analyzed in **Google Sheets** for:
   - Hypothesis testing  
   - Confidence intervals  
   - Power analysis
4. A separate export was created to analyze **novelty effects**.
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

- `init_schema.sql` – All SQL queries used for:
  - Exploratory analysis  
  - Conversion metrics  
  - Group comparisons  
  - Tableau/Sheets exports
- `README.md` – This document
- **Slide deck** – Final summary presentation (attached separately)

---

## 🛠️ Tools Used
- **PostgreSQL** (via [Neon](https://neon.tech) using Beekeeper Studio)
- **Tableau Desktop**
- **Google Sheets**
- **GitHub**

---

## 🔐 Database Access & Notes

> ⚠️ Some DDL operations (like `CREATE TABLE`) may fail when run directly due to lack of schema privileges on the hosted Neon DB.  
> All SQL was written, tested, and exported using Beekeeper Studio.

### 🔗 Connection Info (Read-Only)

'postgres://Test:bQNxVzJL4g6u@ep-noisy-flower-846766-pooler.us-east-2.aws.neon.tech/Globox'

