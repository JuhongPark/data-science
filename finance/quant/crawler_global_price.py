import pymysql
from sqlalchemy import create_engine
import pandas as pd
import yfinance as yf
import time
from datetime import date
from dateutil.relativedelta import relativedelta
from tqdm import tqdm

engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/stock_db')
con = pymysql.connect(user='root',
                      passwd='',
                      host='127.0.0.1',
                      db='stock_db',
                      charset='utf8')
mycursor = con.cursor()

ticker_list = pd.read_sql("""
select * from global_ticker
where date = (select max(date) from global_ticker)
and country = 'United States';
""", con=engine)

query = """
    insert into global_price (Date, High, Low, Open, Close, Volume, `Adj Close`, ticker)
    values (%s, %s, %s, %s, %s, %s, %s, %s) as new
    on duplicate key update
    High = new.High, Low = new.Low, Open = new.Open, Close = new.Close,
    Volume = new.Volume, `Adj Close` = new.`Adj Close`;
"""

start_date = date.today() + relativedelta(years=-5)

error_list = []
for i in tqdm(range(0, len(ticker_list))):

    ticker = ticker_list['Symbol'][i]

    try:
        price = yf.download(ticker, start=start_date, progress=False)
        if len(price) == 0:
            price = yf.download(f'{ticker[:-1]}-{ticker[-1]}', start=start_date, progress=False)
            print('Downloaded')

        price = price.reset_index()
        price['ticker'] = ticker

        args = price.values.tolist()
        mycursor.executemany(query, args)
        con.commit()

    except:
        print(ticker)
        error_list.append(ticker)

    time.sleep(2)

engine.dispose()
con.close()

print(error_list)
