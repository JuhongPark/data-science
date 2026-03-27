# data-science

A collection of data science projects and studies I've built over the years (2017-2024), spanning ML, mathematical statistics, financial data engineering, and foundational programming across Python, R, and SQL.

## Why this repo

I started this repository to consolidate everything I learn into runnable code rather than notes. Each directory represents a different stage of my learning — from basic R tutorials and logic gates all the way to building production-style financial data pipelines and training ML models on medical datasets. It has grown into a personal reference I still revisit.

## Highlights

### Financial Data Pipeline (`finance/quant/`)
Built a set of crawlers that collect stock prices and financial statements from both Korean (Naver Finance, FnGuide, DART) and global (Yahoo Finance, Tiingo) sources, store them in MySQL, and run simple backtests. This was the most end-to-end project: API integration, web scraping, data cleaning, storage, and analysis in one workflow.

### Medical AI Expert Course (`study/med-ai-expert/`)
Five ML task notebooks from a medical AI program — linear regression, logistic regression, SVM, and more — applied to clinical datasets. Focused on understanding model selection and evaluation in a domain where interpretability matters.

### ML & Deep Learning Studies (`study/`)
Worked through *Hands-On Machine Learning with Scikit-Learn and TensorFlow* (end-to-end housing price prediction), PyTorch official tutorials, and TensorFlow exercises (CNN, perceptron, k-means clustering, linear regression).

### Mathematical Statistics (`study/math-stat/`)
Probability theory notes and exercises grounding the math behind the ML models above.

### Python Projects (`python/`)
- **Titanic classification** — decision tree on Kaggle Titanic dataset with visualization (graphviz, folium, seaborn)
- **IPA crawler** — Selenium-based web scraper that collects pronunciation symbols from an online dictionary

### R & SQL Foundations (`r/`, `sql/`)
Comprehensive R tutorials covering core topics (data I/O, apply family, subsetting, control flow, date handling, profiling, simulation, p-value distributions) and SQL practice with SQLite.

## Tech stack

**Languages** : Python, R, SQL
**ML/DL** : scikit-learn, TensorFlow, PyTorch
**Data** : pandas, NumPy, SciPy, matplotlib, seaborn
**Scraping** : Selenium, BeautifulSoup, requests
**Finance** : yfinance, yahooquery, Tiingo API, bt (backtesting)
**Storage** : MySQL, SQLite

## Repository structure

```
finance/quant/      stock crawlers (KR/global), backtesting, Tiingo API
study/
  handson-ml/       Hands-On ML book — housing price prediction
  pytorch/          PyTorch official tutorials
  tensorflow/       TensorFlow — CNN, perceptron, k-means, linear regression
  math-stat/        probability and mathematical statistics
  med-ai-expert/    medical AI course — 5 ML task notebooks
python/
  titanic_first_class   Kaggle Titanic classification
  IPA_crawler           pronunciation web scraper (Selenium)
  gate                  logic gates (AND, OR, NAND, XOR)
r/                  R tutorials (11 topics)
sql/                SQL practice with SQLite
data/               shared datasets (iris.csv, sql.db)
```

## Setup

```bash
pip install -r requirements.txt
```
