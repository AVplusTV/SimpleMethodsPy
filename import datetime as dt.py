import datetime as dt
period = dt.timedelta(hours=3) # сохраняем промежуток времени в три часа
print(period) 
now = dt.datetime.utcnow()
period = dt.timedelta(hours=3)
    
moscow_moment = now + period
    
print(moscow_moment)