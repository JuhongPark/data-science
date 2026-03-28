# data-science

Data science projects and studies (2017-2024) in ML, statistics, and financial data engineering.
The most complete piece is the [financial data pipeline](finance/quant/) — crawlers, storage, and backtesting in one workflow.

## Projects

| Project | Description | Stack |
|---------|------------|-------|
| [**Financial Data Pipeline**](finance/quant/) | Stock price & financial statement crawlers (KR/global), MySQL storage, portfolio strategy backtesting | yfinance, Selenium, MySQL |
| [**Medical AI Tasks**](study/med-ai-expert/) | 4 classification + 1 regression task on a clinical dataset (breast cancer) — LR, SVM, Random Forest, MLP with 13-metric evaluation | scikit-learn, pandas |
| [**IPA Crawler**](python/IPA_crawler.ipynb) | Web scraper for pronunciation symbols from online dictionary | Selenium, BeautifulSoup |

## Studies

- **ML & DL** — [Hands-On ML](study/handson-ml/) (housing prediction), [PyTorch](study/pytorch/), [TensorFlow](study/tensorflow/) (CNN, k-means)
- **Math** — [Probability and statistics](study/math-stat/)
- **Python** — [Titanic classification](python/titanic_first_class.ipynb)
- **R** — [11 tutorial topics](r/)
- **SQL** — [SQLite exercises](sql/)

## Takeaways

Different data, different models, different metrics — different conclusions. These projects are a reminder to evaluate from multiple angles before trusting any single result.

| Observation | Evidence |
|-------------|----------|
| **Model choice changes the answer** | Breast cancer: LR 93.7% → SVM 97.2% → RF 97.2% → MLP 95.8% — four models, no consensus |
| **Metric choice changes the answer** | RF and MLP share 96.7% sensitivity, yet RF's FPR (1.9%) is one-third of MLP's (5.7%); backtest total return favored ALL SPY, Sharpe (~0.80) favored All Weather |
| **A single number is never enough** | 13 metrics (sensitivity, specificity, FPR, FNR, F1, ...) were needed to reveal that missing cancer (FNR 3.3%) costs far more than an unnecessary biopsy |
| **Overfitting hides in plain sight** | SVM C swept 0.0001–10,000 (×1,000 iter) — training hit 100% at C ≥ 100, test plateaued at ~96.5% |

## Tech

Python, R, SQL · scikit-learn, TensorFlow, PyTorch · pandas, NumPy, matplotlib · Selenium, BeautifulSoup · yfinance, MySQL

## Setup

```bash
pip install -r requirements.txt
```
