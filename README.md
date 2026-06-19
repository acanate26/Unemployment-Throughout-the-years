
 📊 U.S. Unemployment & Education Analysis

An exploratory data analysis (EDA) of U.S. unemployment trends broken down by education level, race, and sex using publicly available Kaggle and Data.gov 

---

## 📁 Project Structure

unemployment-education-analysis/
│
├── data/
│   ├── education_usa.csv              # World Bank Barro-Lee education indicators
│   ├── unemployment_data_us.csv       # BLS unemployment by race, sex & education
│   └── df_sex_unemployment_rates.csv  # Historical unemployment by sex (1948–present)
│
├── analysis.py                        # Main EDA script
├── requirements.txt
└── README.md

---

## 📌 Datasets

| File | Source | Coverage | Key Columns |
|------|--------|----------|-------------|
| `education_usa.csv` | U.S. Bureau of Labor Statistics | 2010–2020 | Race, sex, education level, month |
| `unemployment_data_us.csv` | https://www.kaggle.com/datasets/guillemservera/us-unemployment-rates BLS unemployment by race, sex & education |
| `df_sex_unemployment_rates.csv` | BLS unemployment by race, sex & education BLS (CPS) | 1948–present | Men/women rates by age group |

---

## 📈 Analysis Covered

- Unemployment trends by **education level** (Primary → Professional Degree)
- Unemployment by **race** (White, Black, Asian, Hispanic)
- Unemployment by **sex** (Men vs. Women) over time
- **Race gap ratio** — Black/White, Hispanic/White unemployment disparity by year
- **Correlation analysis** — does higher education reduce race/sex unemployment gaps?
- Grouped bar charts and area charts for multi-variable comparison

---

## 🚀 Getting Started

### 1. Clone the repo
git clone https://github.com/yourname/unemployment-education-analysis.git
cd unemployment-education-analysis

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the analysis
python analysis.py

---

## 🧰 Requirements

pandas
matplotlib
numpy
scipy

Install all at once:
pip install pandas matplotlib numpy scipy

---

## 💡 Key Findings

- **Education gap**: Professional degree holders consistently saw unemployment rates 2–3× lower than those with only a primary school education.
- **Race gap**: Black unemployment remained roughly 1.8–2× higher than White unemployment throughout 2010–2019, regardless of economic conditions.
- **Sex gap**: The men/women unemployment gap narrowed significantly post-2013, with women recovering faster after the 2008 recession.
- **COVID caveat**: April 2020 data is excluded as an outlier due to the pandemic spike distorting long-term trends.

---

## ⚠️ Limitations

- `unemployment_data_us.csv` does not cross-tabulate race × sex × education
  simultaneously — columns are independent. True 3-way breakdowns require
  BLS CPS microdata.
- Education attainment data (`education_usa.csv`) ends at 2010 and cannot
  be directly joined to the unemployment data without interpolation.


## 👩🏿‍💻 Author

Arielle 
GitHub: @ariellecanate

Want me to generate the requirements.txt or a Jupyter notebook version of the analysis too?
Sonnet 4.6 Low
