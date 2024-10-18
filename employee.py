"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name, salary=None, hourly_wage=None, hours=None, bonus_commission=None, contract_commission=None, contracts_landed=None):
        self.name = name
        self.salary = salary
        self.hourly_wage = hourly_wage
        self.hours = hours
        self.bonus_commission = bonus_commission
        self.contract_commission = contract_commission
        self.contracts_landed = contracts_landed

    def get_pay(self):
        if self.salary:
            total_pay = self.salary
        elif self.hourly_wage and self.hours:
            total_pay = self.hourly_wage * self.hours
        else:
            total_pay = 0

        if self.bonus_commission:
            total_pay += self.bonus_commission

        if self.contract_commission and self.contracts_landed:
            total_pay += self.contract_commission * self.contracts_landed

        return total_pay

    def __str__(self):
        if self.salary and self.bonus_commission:
            return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."

        if self.salary and self.contract_commission and self.contracts_landed:
            return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contracts_landed} contract(s) at {self.contract_commission}/contract. Their total pay is {self.get_pay()}."

        if self.salary:
            return f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}."

        if self.hourly_wage and self.hours and self.bonus_commission:
            return f"{self.name} works on a contract of {self.hours} hours at {self.hourly_wage}/hour and receives a bonus commission of {self.bonus_commission}. Their total pay is {self.get_pay()}."

        if self.hourly_wage and self.hours and self.contract_commission and self.contracts_landed:
            return f"{self.name} works on a contract of {self.hours} hours at {self.hourly_wage}/hour and receives a commission for {self.contracts_landed} contract(s) at {self.contract_commission}/contract. Their total pay is {self.get_pay()}."

        if self.hourly_wage and self.hours:
            return f"{self.name} works on a contract of {self.hours} hours at {self.hourly_wage}/hour. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000. Their total pay is 4000.
billie = Employee('Billie', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.
charlie = Employee('Charlie', hourly_wage=25, hours=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800.
renee = Employee('Renee', salary=3000, contract_commission=200, contracts_landed=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.
jan = Employee('Jan', hourly_wage=25, hours=150, contract_commission=220, contracts_landed=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.
robbie = Employee('Robbie', salary=2000, bonus_commission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.
ariel = Employee('Ariel', hourly_wage=30, hours=120, bonus_commission=600)
