import datetime as dt
import math

class Record:
    date_now = dt.date.today()        
    def __init__(self, amount, comment, date=date_now):
        self.amount = amount
        self.comment = str(comment)

        if isinstance(date, dt.date) == False:
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

    def get_today_stats(self):
        result = 0
        date_now = dt.date.today()

        for record in self.records:
            if record.date == date_now:
                result += record.amount
        #return float(result)       
        return result

    def get_week_stats(self):
        result = 0
        delta = dt.timedelta(days=7)
        date_now = dt.date.today()

        for record in self.records:
            #if record.date in range(date_now - delta, date_now):
            if record.date > date_now - delta and record.date <= date_now:            
                result += record.amount
        #return float(result)
        return result

class CashCalculator(Calculator):
    USD_RATE = 68.61
    EURO_RATE = 77.75

    #def __init__(self, limit):
    #    super().__init__(limit)        

    def get_today_cash_remained(self, currency):
        spent = super().get_today_stats()
        remained = self.limit - spent

        """
        if currency == 'rub':
            rub = round(remained, 2)
            currency_str = f"{rub} руб"
        elif currency == 'usd':
            usd = round(remained / self.USD_RATE, 2)
            currency_str = f"{usd} USD"
        elif currency == 'eur':
            eur = round(remained / self.EUR_RATE, 2)
            currency_str = f"{eur} Euro"
        else:
            raise ValueError("Unknown currency")

        if remained == 0:
            return (f"Денег нет, держись")            
        elif remained < 0:
            return (f"Денег нет, держись: твой долг - {math.fabs(remained)}")
        elif remained > 0:
            return (f"На сегодня осталось {currency_str}")
        else:
            raise ValueError("Unknown error, check code")
        """

        if remained == 0:
            return (f"Денег нет, держись")            
        elif remained < 0:
            remained = math.fabs(remained)
            if currency == 'rub':
                rub = round(remained, 2)
                currency_str = f"{rub} руб"
            elif currency == 'usd':
                usd = round(remained / self.USD_RATE, 2)
                currency_str = f"{usd} USD"
            elif currency == 'eur':
                eur = round(remained / self.EURO_RATE, 2)
                currency_str = f"{eur} Euro"
            else:
                raise ValueError("Unknown currency")
            return (f"Денег нет, держись: твой долг - {currency_str}")            
        elif remained > 0:
            if currency == 'rub':
                rub = round(remained, 2)
                currency_str = f"{rub} руб"
            elif currency == 'usd':
                usd = round(remained / self.USD_RATE, 2)
                currency_str = f"{usd} USD"
            elif currency == 'eur':
                eur = round(remained / self.EURO_RATE, 2)
                currency_str = f"{eur} Euro"
            else:
                raise ValueError("Unknown currency")
            return (f"На сегодня осталось {currency_str}")
        else:
            raise ValueError("Unknown error, check code")

class CaloriesCalculator(Calculator):
    #def __init__(self, limit):
    #    super().__init__(limit)

    def get_calories_remained(self):
        spent = super().get_today_stats()
        remained = self.limit - spent

        if remained > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {remained} кКал')
        elif remained <= 0:
            return (f'Хватит есть!')
        else:
            raise ValueError('Unknown error, check code')



if __name__ == "__main__":
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=500, comment="кофе"))
    cash_calculator.add_record(Record(amount=5000, comment="Сереге за обед"))
    cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
    print(cash_calculator.get_today_cash_remained('rub'))