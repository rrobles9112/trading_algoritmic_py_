import pandas_datareader as pdr
import numpy as np
import datetime

ticker = '^GSPC'

SnP = pdr.get_data_yahoo(ticker, datetime.date.today()-datetime.timedelta(1925), datetime.date.today())

SnP['Adj Close'].plot()