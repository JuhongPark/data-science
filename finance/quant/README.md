# finance/quant

Financial data pipeline that collects market data from multiple sources, stores it in MySQL, and runs portfolio backtests.

## Data flow

```
Sources                    Crawlers                     Storage          Analysis
─────────                  ────────                     ───────          ────────
Naver Finance  ──→  crawler_kor_price.py   ──→  kor_price     ──┐
FnGuide        ──→  crawler_kor_fs.py      ──→  kor_fs        ──┤
Yahoo Finance  ──→  crawler_global_price.py ──→  global_price  ──├──→  simple_backtest.ipynb
yahooquery     ──→  crawler_global_fs.py   ──→  global_fs     ──┤
Tiingo API     ──→  tiingo_example.ipynb   ──→  (DataFrame)   ──┘
DART API       ──→  data_crawler_ref.ipynb ──→  dart_code
```

## Crawlers

| Script | Source | Data | Method |
|--------|--------|------|--------|
| `crawler_kor_price.py` | Naver Finance | Korean stock daily prices | REST API → CSV parsing |
| `crawler_kor_fs.py` | FnGuide | Korean financial statements | HTML scraping (BeautifulSoup) |
| `crawler_global_price.py` | Yahoo Finance | Global stock daily prices | yfinance library |
| `crawler_global_fs.py` | yahooquery | Global financial statements | yahooquery library |

All crawlers follow the same pattern: read ticker list from DB → fetch data per ticker → upsert into MySQL.

## Backtesting (`simple_backtest.ipynb`)

Compares three portfolio strategies using the `bt` library:

- **ALL SPY** — 100% S&P 500, yearly rebalance (benchmark)
- **Asset EW** — equal-weight across 10 asset classes, monthly rebalance
- **All Weather** — Ray Dalio-inspired allocation (30% stocks, 55% bonds, 15% commodities), quarterly rebalance

## Notebooks

| Notebook | Purpose |
|----------|---------|
| `crawler.ipynb` | Web scraping techniques and examples |
| `data_crawler.ipynb` | Korean market data collection walkthrough |
| `data_crawler_global.ipynb` | Global market data collection walkthrough |
| `data_crawler_ref.ipynb` | DART (Korean corporate disclosure) API integration |
| `tiingo_example.ipynb` | Tiingo API — tickers, metadata, prices, fundamentals |
| `simple_backtest.ipynb` | Portfolio strategy comparison and analysis |
