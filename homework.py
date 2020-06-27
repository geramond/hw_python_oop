import datetime as dt

class Record:            
    def __init__(self, amount, comment, date=dt.date.today()):
        self.amount = amount
        self.comment = str(comment)

        if not isinstance(date, dt.date):
            date_format = "%d.%m.%Y"
            self.date = dt.datetime.strptime(date, date_format).date()
        else:    
            self.date = date

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_stats(self, days_amount):
        result = 0
        delta = dt.timedelta(days=days_amount)

        for record in self.records:
            if dt.date.today() - delta < record.date <= dt.date.today():
                result += record.amount
        return result

    def get_today_stats(self):              
        return self.get_stats(1)

    def get_week_stats(self):                
        return self.get_stats(7)

class CashCalculator(Calculator):
    USD_RATE = 68.61
    EURO_RATE = 77.75

    def get_today_cash_remained(self, currency):        
        spent = self.get_today_stats()
        remained = self.limit - spent
        
        currency_switch = {
            'rub': f"{round(abs(remained), 2)} руб",
            'usd': f"{round(abs(remained) / self.USD_RATE, 2)} USD",
            'eur': f"{round(abs(remained) / self.EURO_RATE, 2)} Euro"
        }
        
        if remained == 0:
            return f"Денег нет, держись"        
        elif remained < 0:            
            return (f"Денег нет, держись: твой долг - {currency_switch[currency]}")
        else:
            return (f"На сегодня осталось {currency_switch[currency]}")

class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        spent = self.get_today_stats()
        remained = self.limit - spent

        if remained > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {remained} кКал')
        else:
            return (f'Хватит есть!')


cash_calculator = CashCalculator(1000.567)
cash_calculator.add_record(Record(amount=500, comment="кофе"))
cash_calculator.add_record(Record(amount=100, comment="Сереге за обед"))
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
print(cash_calculator.get_today_cash_remained('rub'))