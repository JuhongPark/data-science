# data-science

Data science projects and studies (2017-2024) in ML, statistics, and financial data engineering.
The most complete piece is the [financial data pipeline](finance/quant/) — crawlers, storage, and backtesting in one workflow.

## Projects

| Project | Description | Stack |
|---------|------------|-------|
| [**Financial Data Pipeline**](finance/quant/) | Stock price & financial statement crawlers (KR/global), MySQL storage, portfolio strategy backtesting | yfinance, Selenium, MySQL |
| [**Medical AI Tasks**](study/med-ai-expert/) | 5 ML classification tasks on clinical datasets — regression, SVM, model evaluation | scikit-learn, pandas |
| [**IPA Crawler**](python/IPA_crawler.ipynb) | Web scraper for pronunciation symbols from online dictionary | Selenium, BeautifulSoup |

## Studies

- **ML & DL** — [Hands-On ML](study/handson-ml/) (housing prediction), [PyTorch](study/pytorch/), [TensorFlow](study/tensorflow/) (CNN, k-means)
- **Math** — [Probability and statistics](study/math-stat/)
- **Python** — [Titanic classification](python/titanic_first_class.ipynb)
- **R** — [11 tutorial topics](r/)
- **SQL** — [SQLite exercises](sql/)

## Takeaways

| Observation | Context |
|-------------|---------|
| **Accuracy alone hides error costs** | Breast cancer classification required 13 separate metrics (sensitivity, specificity, FPR, FNR, F1, ...) because missing cancer (false negative) is far more dangerous than an unnecessary biopsy (false positive) |
| **Interpretability–accuracy tradeoff** | Logistic regression (93.7%) → SVM → MLP (95.8%) on the same clinical dataset — accuracy improved, but the model became harder to explain to a non-technical audience |
| **Regularization exposes overfitting** | SVM with C swept from 0.0001 to 10,000 (×1,000 iterations each) — training accuracy kept rising while test accuracy plateaued, showing where the model stops learning and starts memorizing |
| **Metric choice changes the conclusion** | Same backtest data ranked strategies differently depending on the metric — total return favored equity concentration, Sharpe ratio favored diversification |

## Tech

Python, R, SQL · scikit-learn, TensorFlow, PyTorch · pandas, NumPy, matplotlib · Selenium, BeautifulSoup · yfinance, MySQL

## Setup

```bash
pip install -r requirements.txt
```
