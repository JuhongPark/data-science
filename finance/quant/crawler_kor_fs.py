# crawler_kor_fs 로 계산
import pymysql
from sqlalchemy import create_engine
import pandas as pd
import requests as rq
from bs4 import BeautifulSoup
import re
from tqdm import tqdm
import time

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
    insert into kor_fs (계정, 기준일, 값, 종목코드, 공시구분)
    values (%s, %s, %s, %s, %s) as new
    on duplicate key update
    값=new.값
"""

def clean_fs(df, ticker, frequency):
    df = df[~df.loc[:, ~df.columns.isin(['계정'])].isna().all(axis=1)]
    df = df.drop_duplicates(['계정'], keep='first')
    df = pd.melt(df, id_vars='계정', var_name='기준일', value_name='값')
    df = df[~pd.isnull(df['값'])]
    df['계정'] = df['계정'].replace({r'계산에 참여한 계정 펼치기': '', r'\(': '', r'\)': '', r'\*': ''}, regex=True)
    df['기준일'] = pd.to_datetime(df['기준일'],
                               format='%Y/%m') + pd.tseries.offsets.MonthEnd()
    df['종목코드'] = ticker
    df['공시구분'] = frequency
    return df

error_list = []
for i in tqdm(range(0, len(ticker_list))):
    ticker = ticker_list['종목코드'][i]

    try:
        url = f'http://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode=A{ticker}'
        data = pd.read_html(url, displayed_only=False)
    
        data_fs_y = pd.concat([
            data[0].iloc[:, ~data[0].columns.str.contains('전년동기')], data[2],
            data[4]
        ])
        data_fs_y = data_fs_y.rename(columns={data_fs_y.columns[0]: "계정"})
    
        page_data = rq.get(url)
        page_data_html = BeautifulSoup(page_data.content, 'html.parser')
    
        fiscal_data = page_data_html.select('div.corp_group1 > h2')
        fiscal_data_text = fiscal_data[1].text
        fiscal_data_text = re.findall('[0-9]+', fiscal_data_text)
    
        data_fs_y = data_fs_y.loc[:, (data_fs_y.columns == '계정') | (
            data_fs_y.columns.str[-2:].isin(fiscal_data_text))]
        data_fs_y_clean = clean_fs(data_fs_y, ticker, 'y')
    
        data_fs_q = pd.concat([
            data[1].iloc[:, ~data[1].columns.str.contains('전년동기')], data[3],
            data[5]
        ])
        data_fs_q = data_fs_q.rename(columns={data_fs_q.columns[0]: "계정"})
        data_fs_q_clean = clean_fs(data_fs_q, ticker, 'q')
    
        data_fs_bind = pd.concat([data_fs_y_clean, data_fs_q_clean])
    
        args = data_fs_bind.values.tolist()
        mycursor.executemany(query, args)
        con.commit()

    except:
        print(ticker)
        error_list.append(ticker)

    time.sleep(2)

engine.dispose()
con.close()

print(f'{error_list}: error_list')
