# data-science

Personal data science study and experiment archive (2017-2024).

## Tech stack

**Languages** : Python, R, SQL
**Frameworks** : TensorFlow, PyTorch, scikit-learn
**Tools** : Jupyter, Selenium, yfinance, yahooquery, Tiingo API

## Repository map

```
r/                  R language tutorials (apply, control, date, subsetting, etc.)
sql/                SQL practice with SQLite
python/
  titanic_first_class   Kaggle Titanic classification
  IPA_crawler           pronunciation web scraper (Selenium)
  gate                  logic gates (AND, OR, NAND, XOR)
study/
  handson-ml/           Hands-On ML with Scikit-Learn & TensorFlow (book)
  pytorch/              PyTorch official tutorials
  tensorflow/           TensorFlow intro (linear regression, CNN, k-means)
  math-stat/            probability and mathematical statistics
  med-ai-expert/        medical AI expert course assignments
finance/
  quant/                stock price/financial statement crawlers (KR/global)
                        simple backtesting, Tiingo API example
data/                   shared datasets (iris.csv, sql.db)
```

## Setup

```bash
pip install -r requirements.txt
```

> **Note**: `finance/quant/` crawlers require a local MySQL database (`stock_db`).
> API notebooks require keys configured via `keyring` (see each notebook for details).
