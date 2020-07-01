import datetime as dt


class Record:
    DATE_FORMAT = "%d.%m.%Y"

    def __init__(self, amount, comment, date=dt.date.today()):
        self.amount = amount
        self.comment = str(comment)

        if not isinstance(date, dt.date):
            self.date = dt.datetime.strptime(date, self.DATE_FORMAT).date()
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
        past_date = dt.date.today() - dt.timedelta(days=days_amount)
        today = dt.date.today()

        for record in self.records:
            if past_date < record.date <= today:
                result += record.amount
        return result

    def get_today_stats(self):
        return self.get_stats(1)

    def get_week_stats(self):
        return self.get_stats(7)


class CashCalculator(Calculator):
    RUB_RATE = 1.0
    USD_RATE = 68.61
    EURO_RATE = 77.75

    def get_today_cash_remained(self, currency):
        spent = self.get_today_stats()
        remained = self.limit - spent

        if remained == 0:
            return f"Денег нет, держись"

        currency_switch = {
            'rub': (self.RUB_RATE, "руб"),
            'usd': (self.USD_RATE, "USD"),
            'eur': (self.EURO_RATE, "Euro")
        }
        currency_str = f"{round(abs(remained) / currency_switch[currency][0], 2)} {currency_switch[currency][1]}"

        if remained < 0:
            return (f"Денег нет, держись: твой долг - {currency_str}")

        return (f"На сегодня осталось {currency_str}")


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        spent = self.get_today_stats()
        remained = self.limit - spent

        if remained > 0:
            return (f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {remained} кКал')

        return (f'Хватит есть!')

if __name__ == "__main__":
    cash_calculator = CashCalculator(1000.567)
    cash_calculator.add_record(Record(amount=500, comment="кофе"))
    cash_calculator.add_record(Record(amount=100, comment="Сереге за обед"))
    cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
    print(cash_calculator.get_today_cash_remained('rub'))