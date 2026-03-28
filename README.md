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

### ML perspective

| Observation | Context |
|-------------|---------|
| **Accuracy alone hides error costs** | Breast cancer classification required 13 metrics (sensitivity, specificity, FPR, FNR, F1, ...) — missing cancer (FNR 3.3%) is far more dangerous than an unnecessary biopsy, and a single accuracy number masks that asymmetry |
| **More complex ≠ more accurate** | Same dataset: LR 93.7% → SVM 97.2% → RF 97.2% → MLP 95.8% — the deepest model (MLP) scored *lower* than SVM and RF |
| **Regularization exposes overfitting** | SVM C swept 0.0001–10,000 (×1,000 iterations) — training hit 100% at C ≥ 100 while test plateaued at ~96.5%, revealing memorization |
| **Feature importance validates domain knowledge** | RF top-3 features — worst perimeter, mean concave points, worst concave points — match known cytological markers of malignancy |
| **Metric choice changes the conclusion** | Same backtest data, different rankings: total return favored equity concentration (ALL SPY), Sharpe (~0.80) and Calmar favored the diversified All Weather portfolio |

### AI safety perspective

| Observation | Context |
|-------------|---------|
| **Same accuracy, different risk profiles** | RF and MLP share 96.7% sensitivity, but RF's false-positive rate (1.9%) is one-third of MLP's (5.7%) — same cancer detection, three times fewer unnecessary biopsies |
| **Overfitting is a silent deployment risk** | SVM scores 100% on training data yet ~96.5% on unseen data — without held-out validation, such a model produces confident but wrong predictions |
| **Interpretability enables clinical accountability** | LR and RF expose feature weights and importances; MLP does not — when a model must be explained to clinicians or audited by regulators, accuracy alone is insufficient |

## Tech

Python, R, SQL · scikit-learn, TensorFlow, PyTorch · pandas, NumPy, matplotlib · Selenium, BeautifulSoup · yfinance, MySQL

## Setup

```bash
pip install -r requirements.txt
```
