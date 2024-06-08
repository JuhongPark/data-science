import pymysql
from sqlalchemy import create_engine
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
import requests as rq
import time
from tqdm import tqdm
from io import BytesIO

engine = create_engine('mysql+pymysql://root:@127.0.0.1:3306/stock_db')
con = pymysql.connect(user='root',
                      passwd='',
                      host='127.0.0.1',
                      db='stock_db',
                      charset='utf8')
mycursor = con.cursor()

ticker_list = pd.read_sql("""
select * from kor_ticker
where 기준일 = (select max(기준일) from kor_ticker) 
	and 종목구분 = '보통주';
""", con=engine)

query = """
    insert into kor_price (날짜, 시가, 고가, 저가, 종가, 거래량, 종목코드)
    values (%s, %s, %s, %s, %s, %s, %s) as new
    on duplicate key update
    시가 = new.시가, 고가 = new.고가, 저가 = new.저가,
    종가 = new.종가, 거래량 = new.거래량;
"""

error_list = []
for i in tqdm(range(0, len(ticker_list))):
    ticker = ticker_list['종목코드'][i]

    fr = (date.today() + relativedelta(years=-5)).strftime("%Y%m%d")
    to = (date.today()).strftime("%Y%m%d")

    try:
        url = f'''https://fchart.stock.naver.com/siseJson.nhn?symbol={ticker}&requestType=1
        &startTime={fr}&endTime={to}&timeframe=day'''

        data = rq.get(url).content
        data_price = pd.read_csv(BytesIO(data))

        price = data_price.iloc[:, 0:6]
        price.columns = ['날짜', '시가', '고가', '저가', '종가', '거래량']
        price = price.dropna()
        price['날짜'] = price['날짜'].str.extract(r'(\d+)')
        price['날짜'] = pd.to_datetime(price['날짜'])
        price['종목코드'] = ticker

        args = price.values.tolist()
        mycursor.executemany(query, args)
        con.commit()

    except:
        print(ticker)
        error_list.append(ticker)

    time.sleep(2)

engine.dispose()
con.close()

print(f'{error_list}: error_list')
