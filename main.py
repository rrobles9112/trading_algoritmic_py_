import datetime as dt
import pandas_datareader as pdr

ticker = "APPL"
start_date = dt.date.today() - dt.timedelta(365)
end_date = dt.date.today()




def main():
    data = pdr.get_data_yahoo(ticker, start_date, end_date, interval='mo')
    print(data)


if __name__ == '__main__':
    main()