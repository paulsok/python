class Money:
    def __init__(self, dollars, cents):
        self.total_cents = 100 * dollars + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, dollars):
        if isinstance(dollars, int) and dollars >= 0:
            self.total_cents = self.total_cents - self.total_cents // 100 * 100 + dollars * 100
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, cents):
        if isinstance(cents, int) and cents < 100:
            self.total_cents = self.total_cents - self.total_cents % 100 + int(cents)
        else:
            print("Error cents")

    def __str__(self):
        return "Ваше состояние составляет %s долларов %s центов" % \
                (self.total_cents // 100, self.total_cents % 100)


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов

        
        
