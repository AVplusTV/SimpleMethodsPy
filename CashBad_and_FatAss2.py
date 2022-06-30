"""Calculator of the remeined cash and calories.

Calculating the cash and calories depending of your
own limits eating and spending by day,
giving advice for your better life.
"""
from datetime import date as day
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple


class Record:
    """Record cash and calories data."""

    FORMAT_DAY: str = "%d.%m.%Y"

    def __init__(self, amount: int, comment: str,
                 date: Optional[str] = None) -> None:
        """Define the parameters of the class Record."""
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date: day = day.today()
        else:
            self.date: datetime = (datetime.strptime(date,
                                   Record.FORMAT_DAY).date())


class Calculator:
    """Create, record and sum cash and calories data.

    Contain the methods for recording the data to list.
    Contain the methods for calculating the day and week
    sum of cash and calories.
    Contain the child classes CashCalculator and CaloriesCalculator.
    """

    def __init__(self, limit: int):
        """Define the parameters of the class Calculator."""
        self.limit = limit
        self.records: List[Record] = []

    def add_record(self, record: Record) -> None:
        """Record cash and calories data to list."""
        self.records.append(record)

    def get_today_stats(self) -> int:
        """Calculate the day sum of cash and calories."""
        now: day = day.today()
        return sum(rec.amount for rec in self.records
                   if rec.date == now)

    def get_week_stats(self) -> int:
        """Calculate the week sum of cash and calories."""
        now: day = day.today()
        seven_days: day = now - timedelta(days=7)
        return sum(rec.amount for rec in self.records
                   if seven_days < rec.date <= now)

    def remaned_value(self) -> int:
        """Calculate the remaned_value of cash and calories."""
        return self.limit - self.get_today_stats()


class CashCalculator(Calculator):
    """Calculate the cash data.

    Contain the methods for calculating the remained cash
    and translate it depends of currency rates.
    """

    USD_RATE: float = 77.44
    EURO_RATE: float = 89.55
    RUB_RATE: float = 1.0

    def get_today_cash_remained(self, currency: str = 'rub') -> str:
        """Calculate the remained cash.

        Check the currency name.
        Translate remained cash depends of currency rates.
        """
        remaned_cash: int = self.remaned_value()

        if remaned_cash == 0:
            return 'Денег нет, держись'

        curr_data: Dict[str, Tuple[float, str]] = {
            'usd': (self.USD_RATE, 'USD'),
            'eur': (self.EURO_RATE, 'Euro'),
            'rub': (self.RUB_RATE, 'руб')
        }

        if currency not in curr_data:
            return 'Проверьте наименование валюты'

        curr_rate: float
        curr_text: str
        curr_rate, curr_text = curr_data[currency]

        cash_remain_rate: float = round(remaned_cash / curr_rate, 2)

        if remaned_cash > 0:
            return f'На сегодня осталось {cash_remain_rate} {curr_text}'
        cash_debt = abs(cash_remain_rate)
        return ('Денег нет, держись: твой долг - '
                f'{cash_debt} {curr_text}')


class CaloriesCalculator(Calculator):
    """Calculate the calories data.

    Contain the methods for calculating the remained calories
    and advice of your fatbody life.
    """

    def get_calories_remained(self) -> str:
        """Calculate the remained calories.

        Giving advice of your fatbody life.
        """
        remaned_ccal: int = self.remaned_value()
        if remaned_ccal > 0:
            return ('Сегодня можно съесть что-нибудь ещё, '
                    'но с общей калорийностью не более'
                    f' {remaned_ccal} кКал')
        return 'Хватит есть!'
        

print(date)

cash_calculator = CashCalculator(2000)

print()
cash_calculator.add_record(Record(1000, 'Бензин', '01.05.2021'))
cash_calculator.add_record(Record(1000, 'Вейп', '02.05.2021'))
cash_calculator.add_record(Record(1000, 'Вейп', '03.05.2021'))
cash_calculator.add_record(Record(1000, 'Вейп', '04.05.2021'))
cash_calculator.add_record(Record(1000, 'Вейп', '05.05.2021'))
cash_calculator.add_record(Record(1000, 'Транспортные расходы', '06.05.2021'))
cash_calculator.add_record(Record(1000, 'Напился', '07.05.2021'))
cash_calculator.add_record(Record(1000, 'Забил холодильник', '08.05.2021'))
cash_calculator.add_record(Record(1000, 'Забил холодильник', '09.05.2021'))
cash_calculator.add_record(Record(1000, 'Куртеха', '10.05.2021'))
cash_calculator.add_record(Record(1000, 'трусы', '11.05.2021'))
cash_calculator.add_record(Record(1000, 'трусы', '12.05.2021'))
cash_calculator.add_record(Record(3000, 'трусы', '15.05.2021'))
cash_calculator.add_record(Record(1000, 'трусы'))

print(cash_calculator.records)
print()
print(cash_calculator.get_today_stats())
print(cash_calculator.get_week_stats())
print()
print(cash_calculator.get_today_cash_remained('eur'))
print()
print('++++++++++++++++++++++++++++++++++++++++++')
print()
ccal_calc = CaloriesCalculator(2000)

ccal_calc.add_record(Record(100, 'банан', '01.05.2021'))
ccal_calc.add_record(Record(100, 'банан', '02.05.2021'))
ccal_calc.add_record(Record(100, 'банан', '03.05.2021'))
ccal_calc.add_record(Record(100, 'банан', '04.05.2021'))
ccal_calc.add_record(Record(100, 'банан', '05.05.2021'))
ccal_calc.add_record(Record(100, 'яблоко', '06.05.2021'))
ccal_calc.add_record(Record(100, 'Литр масла', '07.05.2021'))
ccal_calc.add_record(Record(100, 'Водка и пиво', '08.05.2021'))
ccal_calc.add_record(Record(100, 'Тортище', '09.05.2021'))
ccal_calc.add_record(Record(100, 'орешки', '10.05.2021'))
ccal_calc.add_record(Record(100, 'пирожки','11.05.2021'))
ccal_calc.add_record(Record(100, 'пирожки','12.05.2021'))
ccal_calc.add_record(Record(1800, 'пирожки'))
ccal_calc.add_record(Record(100, 'пирожки'))

print(ccal_calc.records)
print()
print(ccal_calc.get_today_stats())
print(ccal_calc.get_week_stats())
print()
print(ccal_calc.get_calories_remained())
