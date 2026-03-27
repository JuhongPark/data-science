# data-science

Data science projects and studies (2017-2024) — ML, statistics, financial data engineering, and programming across Python, R, and SQL.

> I built this repo to turn everything I learn into runnable code.
> Each directory is a different stage of learning, from logic gates to production-style data pipelines.

---

## Highlights

| Project | What I did | Stack |
|---------|-----------|-------|
| **[Financial Data Pipeline](finance/quant/)** | Crawled stock prices & financial statements (KR/global), stored in MySQL, ran backtests | Python, Selenium, yfinance, Tiingo API, MySQL |
| **[Medical AI Course](study/med-ai-expert/)** | 5 ML tasks on clinical datasets — regression, SVM, model evaluation | scikit-learn, pandas |
| **[Hands-On ML](study/handson-ml/)** | End-to-end housing price prediction from the O'Reilly book | scikit-learn, NumPy |
| **[Deep Learning](study/pytorch/, study/tensorflow/)** | PyTorch tutorials, TensorFlow CNN / perceptron / k-means | PyTorch, TensorFlow |
| **[Math & Statistics](study/math-stat/)** | Probability theory — the math behind the ML models above | Jupyter |
| **[Titanic Classification](python/titanic_first_class.ipynb)** | Decision tree on Kaggle dataset with graphviz visualization | scikit-learn, seaborn |
| **[IPA Crawler](python/IPA_crawler.ipynb)** | Web scraper for pronunciation symbols from online dictionary | Selenium, BeautifulSoup |
| **[R Tutorials](r/)** | 11 topics: apply, subsetting, control flow, profiling, simulation, etc. | R |
| **[SQL Practice](sql/)** | Query exercises with SQLite | SQL, pandas |

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
finance/quant/          stock crawlers (KR/global), backtesting, Tiingo API
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
