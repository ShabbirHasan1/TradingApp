from django.shortcuts import render
import pandas as pd


#views are here.

def home(request):
    data = pd.read_csv('NIFTY_F1.csv',index_col=0,parse_dates=True)
    #data['dateTime'] = pd.to_datetime(data['dateTime'])
    print(data)
    ohlc = {
        'BANKNIFTY':'first',
        'DATE':'first',
        'TIME':'first',
        'OPEN':'first',
        'HIGH':'max',
        'LOW':'min',
        'CLOSE':'last',
        'VOLUME':'last',
    }
    df = data.resample('5T', on = 'dateTime').agg(ohlc)
    # df = data.resample('5min').apply(ohlc)
    mydict = {
        "df": df.to_html()
    }
    return render(request, 'index.html', context=mydict)




