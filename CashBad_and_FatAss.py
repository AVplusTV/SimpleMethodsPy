"""Import the method datetime."""
from datetime import datetime, timedelta
from currency_converter import CurrencyConverter

now = datetime.now().date()
seven = now + timedelta(days=-6)
now_day = now.strftime("%d.%m.%Y")
seven_days = seven.strftime("%d.%m.%Y")

c = CurrencyConverter()
usd_rate = c.convert(1, 'USD', 'RUB')
euro_rate = c.convert(1, 'EUR', 'RUB')


class Record:
    """Create, record and sum cash and calories data.

    Contain the methods for recording the data to lists.
    Contain the methods for calculating the day and week
    sum of cash and calories.
    """

    record_list_cash = []
    record_list_ccal = []

    def __init__(self, amount, comment, date=now_day):
        """Define the parameters of the class Record."""
        self.amount = amount
        self.comment = comment
        self.date = datetime.strptime(date, "%d.%m.%Y").date()

    def add_record_cash(self):
        """Record the data to lists of cash."""
        Record.record_list_cash.append({'amount': self.amount,
                                        'comment': self.comment,
                                        'date': self.date})

    def add_record_ccal(self):
        """Record the data to lists of calories."""
        Record.record_list_ccal.append({'amount': self.amount,
                                        'comment': self.comment,
                                        'date': self.date})

    def get_today_stats_cash(self):
        """Calculate the day sum of cash."""
        sum_cash_day = 0

        for i in range(len(Record.record_list_cash)):
            if Record.record_list_cash[i]['date'] == now:
                sum_cash_day += Record.record_list_cash[i]['amount']
        return sum_cash_day

    def get_today_stats_ccal(self):
        """Calculate the day sum of calories."""
        sum_ccal_day = 0

        for i in range(len(Record.record_list_ccal)):
            if Record.record_list_ccal[i]['date'] == now:
                sum_ccal_day += Record.record_list_ccal[i]['amount']
        return sum_ccal_day

    def get_week_stats_cash(self):
        """Calculate the week sum of cash."""
        sum_cash_week = 0

        for i in range(len(Record.record_list_cash)):
            if seven <= Record.record_list_cash[i]['date'] <= now:
                sum_cash_week += Record.record_list_cash[i]['amount']
        return sum_cash_week

    def get_week_stats_ccal(self):
        """Calculate the week sum of calories."""
        sum_ccal_week = 0

        for i in range(len(Record.record_list_ccal)):
            if seven <= Record.record_list_ccal[i]['date'] <= now:
                sum_ccal_week += Record.record_list_ccal[i]['amount']
        return sum_ccal_week


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        
    records = []

class CashCalculator(Calculator):
    USD_RATE = float(74)
    EURO_RATE = float(88)

    def __init__(self, limit):
        super().__init__(limit)
        

    def add_record(self, record):
        self.record = record
        Calculator.records.append({'amount': record.amount,
                                   'comment': record.comment,
                                   'date': record.date})



    def get_today_cash_remained(self, currency='rub'):
        self.currency = currency
        ammount = Record.get_today_stats_cash(self)
        if self.currency == 'usd':
            day_ammount = ammount / CashCalculator.USD_RATE
            carrency_text = 'usd'
        elif self.currency == 'euro':
            day_ammount = ammount / CashCalculator.EURO_RATE
            carrency_text = 'euro'
        elif self.currency == 'rub':
            day_ammount = ammount
            carrency_text = 'руб.'
        else:
            print('Что за бредовая валюта?')
            return

        if self.limit > day_ammount:
            cash_remain = round(self.limit - day_ammount, 2)
            print(f'У Вас осталось {cash_remain} {carrency_text}')
        elif self.limit == day_ammount:
            print('Деньги кончились, ух транжира!')
        else:
            cash_remain = round(day_ammount - self.limit, 2)
            print(f'Денег нет, держись: твой долг - '
                  f'{cash_remain} {carrency_text}')


class CaloriesCalculator(Calculator):
    def _init_(self, limit):
        super().__init__(limit)
        
        
    def add_record(self, record):
        self.record = record
        Calculator.records.append({'amount': record.amount,
                                   'comment': record.comment,
                                   'date': record.date})

    def get_calories_remained(self):
        if self.limit > Record.get_today_stats_ccal(self):
            print(f'Сегодня можно съесть что-нибудь ещё, '
                  f'но с общей калорийностью не более'
                  f', {self.limit - Record.get_today_stats_ccal(self)},'
                  f'ккал')
        elif self.limit == Record.get_today_stats_ccal(self):
            print('Харе закидываться, Твой предел достигнут!')
        else:
            print(f'Хватит есть! Ты уже разжирел на'
                  f' {Record.get_today_stats_ccal(self) - self.limit}'
                  f'ккал. Жиробас!')



CaloriesCalculator(1500).get_calories_remained()
