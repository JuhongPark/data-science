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

### ML perspective — models disagree, metrics reveal why

| Observation | Context |
|-------------|---------|
| **Same data, different answers** | Breast cancer dataset: LR 93.7% → SVM 97.2% → RF 97.2% → MLP 95.8% — four models, no consensus on ranking, and the deepest model (MLP) was *not* the best |
| **Same accuracy, different errors** | RF and MLP share 96.7% sensitivity, yet RF's false-positive rate (1.9%) is one-third of MLP's (5.7%) — which model is "better" depends entirely on which error you care about |
| **Single metrics hide asymmetric risk** | Breast cancer classification required 13 metrics (sensitivity, specificity, FPR, FNR, F1, ...) — accuracy alone cannot express that missing cancer (FNR 3.3%) is far costlier than an unnecessary biopsy |
| **Metric choice flips the ranking** | Same backtest data: total return favored equity concentration (ALL SPY), Sharpe (~0.80) and Calmar favored the diversified All Weather portfolio — the "best" strategy changed with the metric |
| **Regularization separates learning from memorizing** | SVM C swept 0.0001–10,000 (×1,000 iterations) — training hit 100% at C ≥ 100 while test plateaued at ~96.5%; only the train-test gap metric exposed the problem |
| **Feature importance as a sanity check** | RF top-3 features — worst perimeter, mean concave points, worst concave points — match known cytological markers; a metric that accuracy alone cannot provide |

### AI safety perspective

| Observation | Context |
|-------------|---------|
| **Model choice is a patient-safety decision** | RF and MLP both "pass" at >95% accuracy, but choosing MLP triples unnecessary biopsies (FPR 5.7% vs 1.9%) — model selection requires multi-metric evaluation, not a single leaderboard score |
| **Overfitting is invisible without the right metric** | SVM scores 100% on training data yet ~96.5% on unseen data — accuracy on training set looks perfect, only the held-out gap reveals the risk |
| **Interpretability enables accountability** | LR and RF expose feature weights and importances; MLP does not — regulators and clinicians need metrics beyond accuracy to trust and audit a model |

## Tech

Python, R, SQL · scikit-learn, TensorFlow, PyTorch · pandas, NumPy, matplotlib · Selenium, BeautifulSoup · yfinance, MySQL

## Setup

```bash
pip install -r requirements.txt
```
