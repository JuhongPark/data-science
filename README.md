# data-science

Data science projects and studies (2017-2024) — from foundational programming and statistics to production-style financial data pipelines.

> Started with R tutorials and logic gates, gradually moved into ML modeling, and eventually built end-to-end systems that crawl, store, and analyze real market data.

**Best starting point:** [`finance/quant/`](finance/quant/) — the most complete project in this repo.

---

## Highlights

| Project | What I did | Stack |
|---------|-----------|-------|
| **[Financial Data Pipeline](finance/quant/)** | Designed crawlers for stock prices & financial statements (KR/global), stored in MySQL, compared portfolio strategies via backtesting | Python, Selenium, yfinance, Tiingo, MySQL |
| **[Medical AI Course](study/med-ai-expert/)** | 5 ML tasks on clinical datasets — linear/logistic regression, SVM, model evaluation | scikit-learn, pandas |
| **[Math & Statistics](study/math-stat/)** | Probability theory and mathematical statistics foundations | Jupyter |
| **[ML & DL Studies](study/)** | Hands-On ML (housing prediction), PyTorch tutorials, TensorFlow (CNN, perceptron, k-means) | scikit-learn, PyTorch, TensorFlow |
| **[Python Projects](python/)** | Titanic classification, IPA pronunciation scraper, logic gates | scikit-learn, Selenium |
| **[R & SQL](r/, sql/)** | 11 R tutorial topics, SQL exercises with SQLite | R, SQL |

---

## Tech stack

| Category | Tools |
|----------|-------|
| Languages | Python, R, SQL |
| ML / DL | scikit-learn, TensorFlow, PyTorch |
| Data | pandas, NumPy, SciPy, matplotlib, seaborn |
| Scraping | Selenium, BeautifulSoup, requests |
| Finance | yfinance, yahooquery, Tiingo API, bt |
| Storage | MySQL, SQLite |

---

## Repository structure

```
finance/quant/          data pipeline, backtesting, API integrations
study/
  handson-ml/           Hands-On ML book — housing price prediction
  pytorch/              PyTorch official tutorials
  tensorflow/           CNN, perceptron, k-means, linear regression
  math-stat/            probability and mathematical statistics
  med-ai-expert/        medical AI course — 5 ML task notebooks
python/                 Titanic, IPA crawler, logic gates
r/                      R tutorials (11 topics)
sql/                    SQL practice with SQLite
data/                   shared datasets (iris.csv, sql.db)
```

## Setup

```bash
pip install -r requirements.txt
```
