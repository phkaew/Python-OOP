import datetime as dt
d1 = dt.datetime(year=2020, month=1, day=1,hour=12,minute=0,second=0)
d2= dt.datetime(year=2020, month=1, day=2,hour=1,minute=15,second=0)
days= dt.timedelta(days=20)
dd=d2-d1
print(d2.strftime('%d %H:%M:%S'))