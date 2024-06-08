from sqlalchemy import create_engine
import pymysql
import pandas as pd
from yahooquery import Ticker
import time
from tqdm import tqdm
import numpy as np

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

query_fs = """
    insert into global_fs (ticker, date, account, value, freq)
    values (%s, %s, %s, %s, %s) as new
    on duplicate key update
    value = new.value;
"""

error_list = []
for i in tqdm(range(0, len(ticker_list))):
    ticker = ticker_list['Symbol'][i]

    try:
        data = Ticker(ticker)
        
        data_y = data.all_financial_data(frequency = 'a')
        if type(data_y) == str:
            data = Ticker(f'{ticker[:-1]}-{ticker[-1]}')
            data_y = data.all_financial_data(frequency = 'a')
        data_y.reset_index(inplace = True)
        data_y = data_y.loc[:, ~data_y.columns.isin(['periodType', 'currencyCode'])]
        data_y = data_y.melt(id_vars = ['symbol', 'asOfDate'])
        data_y = data_y.replace([np.nan], None)
        data_y['freq'] = 'y'
        data_y.columns = ['ticker', 'date', 'account', 'value', 'freq']
        
        data_q = data.all_financial_data(frequency = 'q')
        data_q.reset_index(inplace = True)
        data_q = data_q.loc[:, ~data_q.columns.isin(['periodType', 'currencyCode'])]
        data_q = data_q.melt(id_vars = ['symbol', 'asOfDate'])
        data_q = data_q.replace([np.nan], None)
        data_q['freq'] = 'q'
        data_q.columns = ['ticker', 'date', 'account', 'value', 'freq']
        
        data_fs = pd.concat([data_y, data_q], axis=0)

        args = data_fs.values.tolist()
        mycursor.executemany(query_fs, args)
        con.commit()

    except:
        print(ticker)
        error_list.append(ticker)

    time.sleep(2)

engine.dispose()
con.close()

print(error_list)
