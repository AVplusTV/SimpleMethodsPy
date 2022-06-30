from datetime import datetime, timedelta


now = datetime.now()
seven  = datetime.now() + timedelta(days=-6)

now_day = now.strftime("%d.%m.%Y")
seven_days = seven.strftime("%d.%m.%Y")

record_list_cash = []
record_list_ccal = []


class Record:
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment
        self.date = date
        
    def add_record_cash(self):        
        record_list_cash.append({'amount' : self.amount,
                                 'comment' : self.comment,
                                 'date' : self.date})
           
    def add_record_ccal(self):        
        record_list_ccal.append({'amount' : self.amount,
                                 'comment' : self.comment,
                                 'date' : self.date})
        
    def get_today_stats(self):
        sum_cash_day = 0
        for i in range(len(record_list_cash)):
            if record_list_cash[i]['date'] == now_day:
                sum_cash_day += record_list_cash[i]['amount']
        print(sum_cash_day)
        
        sum_ccal_day = 0
        for i in range(len(record_list_ccal)):
            if record_list_ccal[i]['date'] == now_day:
                sum_ccal_day += record_list_ccal[i]['amount']
        print(sum_ccal_day)
        
    def get_week_stats(self):
        sum_cash_week = 0
        for i in range(len(record_list_cash)):
            if seven_days <= record_list_cash[i]['date'] <= now_day:
                sum_cash_week += record_list_cash[i]['amount']
        print(sum_cash_week)
        
        sum_ccal_week = 0
        for i in range(len(record_list_ccal)):
            if seven_days <= record_list_ccal[i]['date']  <= now_day:
                sum_ccal_week  += record_list_ccal[i]['amount']
        print(sum_ccal_week )
     
        
class Calculator:
    def _init_(self, limits):
        self.limits = limits        
    
usd_rate = 74
euro_rate = 88      
        
class CashCalculator(Calculator):
    def _init_(self, limits):
        super().__init__(limits)
        
        
        
        
class CaloriesCalculator(Calculator):
    def _init_(self, limits,):
        super().__init__(limits)
        
        
        
            
        
        
r01 = Record(1000, 'Бензин', '01.05.2021')
r0 = Record(2000, 'Вейп', '05.05.2021')
r1 = Record(3000, 'Транспортные расходы', '06.05.2021')
r2 = Record(4000, 'Напился', '07.05.2021')
r3 = Record(5000, 'Забил холодильник', '08.05.2021')

r04 = Record(10000, 'Литр масла', '01.05.2021') 
r4 = Record(100, 'Орешек', '05.05.2021') 
r5 = Record(1000, 'Кусок тортика. И ещё один.', '06.05.2021')
r6 = Record(100, 'Йогурт.', '07.05.2021')
r7 = Record(2000, 'Баночка чипсов.', '08.05.2021') 

r01.add_record_cash()
r0.add_record_cash()
r1.add_record_cash()
r2.add_record_cash()
r3.add_record_cash()

r04.add_record_ccal()
r4.add_record_ccal()
r5.add_record_ccal()
r6.add_record_ccal()
r7.add_record_ccal()

print(record_list_cash)
print()
print(record_list_ccal)
print()
r0.get_today_stats()
print()
r0.get_week_stats()





