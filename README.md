# HCL-PROJECT
# 🏨 Hotel Booking Revenue Analysis

A clean, beginner-friendly data analytics project built **strictly with Python, pandas, and NumPy** to analyze hotel booking behavior and revenue drivers across 5 major Indian cities (Mumbai, Bengaluru, New Delhi, Jaipur, and Goa).

---

## 📌 Project Overview
This project takes a raw hotel booking dataset (255 bookings), cleans real-world data flaws (duplicates, missing values, human typos, and invalid stay lengths), and extracts actionable business insights using basic data analysis techniques.

Everything runs from a single, self-contained Python script: [`main.py`](main.py).

---

## ❓ Business Questions Answered
1. **Overall Performance:** What is the average revenue per booking?
2. **Revenue Drivers:** How strongly do room rates and stay lengths correlate with total revenue?
3. **Room Types:** Which room categories generate the highest income?
4. **Channels:** Do Direct Website bookings outperform third-party OTA Apps?
5. **Cities:** Which destinations bring in the highest booking value?
6. **Low-Yield Bookings:** Why do 36% of bookings make less than ₹15,000?

---

## 🚀 Quick Start

### 1. Clone & Install
```bash
git clone https://github.com/<your-username>/hotel-revenue-analysis.git
cd hotel-revenue-analysis
pip install -r requirements.txt
```

### 2. Run the Analysis
```bash
python main.py
```
*(The script runs end-to-end in ~2 seconds and automatically saves `hotel_bookings_clean.csv`).*

---

## 🧹 What the Code Does (Step-by-Step)
1. **Loads Data:** Inspects columns, missing values, and duplicates.
2. **Cleans Flaws:**
   - Drops 5 duplicate rows.
   - Cleans messy city names using `.str.strip().str.title()` (fixes `'JAIPUR '` & `'bengaluru'`).
   - Fixes invalid negative stay nights (`-3`) by replacing them with `NaN`.
   - Imputes missing numbers with the **median** (so luxury suite prices don't skew results).
3. **Engineers Features:** Creates `Revenue_Per_Night`, `Revenue_Tier`, and `Stay_Type`.
4. **Computes Business Metrics:** Runs `.groupby()`, `.describe()`, and `.corr()`.
5. **Exports Clean Data:** Saves 250 verified records to a clean CSV.

---

## 📊 Key Findings
* **Average Booking Revenue:** **₹18,538** (median: **₹17,830**).
* **Top Revenue Drivers:** **Room Rate ($r = 0.55$)** and **Nights Stayed ($r = 0.47$)** have strong positive relationships with total revenue.
* **Direct vs. OTA:** **Direct Website** bookings have the highest average ticket size (**₹19,336**), while **OTA Apps** bring the most volume (51.2% / 128 bookings) at a slightly lower average (**₹18,702**).
* **Room Rankings:** **Suites** lead at **₹30,202** avg, followed by Executive (₹21,575), Deluxe (₹18,582), and Standard (₹15,184).
* **Low-Yield Diagnosis:** 36% of bookings earned under ₹15,000. These were primarily **short 1–2 night stays** in Standard rooms.

---

## 💡 Managerial Recommendations
1. **Encourage 3+ Night Stays:** Introduce "Stay 3, Pay for 2.5" promotions to convert 1–2 night stays into longer, higher-paying visits.
2. **Incentivize Direct Bookings:** Offer complimentary breakfast on website bookings to capture higher ticket sizes and avoid third-party OTA commissions.

---

## 🛠️ Tech Stack
* **Language:** Python 3.8+
* **Libraries:** `pandas`, `numpy` (No complex dependencies)

---

## 👤 Author
* Your Name – [GitHub Profile](https://github.com/<your-username>)
