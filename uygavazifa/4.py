class Employee:
    def  __init__(self, ish_kuni:int, kunlik_ish_haqi:int):
        self.ish_kuni = ish_kuni
        self.maosh=kunlik_ish_haqi
    
    def calculate_salary(self):
        return self.ish_kuni * self.maosh


class Boshliq (Employee):
    def  __init__(self, ish_kuni, kunlik_ish_haqi):
        super().__init__(ish_kuni, kunlik_ish_haqi)
        self.oylik=0
    def update(self):
        self.oylik=super().calculate_salary()
    def __str__(self):
        return f"""boshliq: {self.oylik}"""

class Developer(Employee):
    def __init__(self, ishkuni:int, ishhaqi:int):
        super().__init__(ishkuni,ishhaqi)
        self.daromad=0
    def update(self):
        self.daromad=super().calculate_salary()
    def __str__(self):
        return f"""Developer: {self.daromad}"""

class Sotuvchi(Employee):
    def __init__(self, ishkuni:int, ishhaqi:int):
        super().__init__(ishkuni, ishhaqi)
        self.ish_haqi=0
    def update(self):
        self.ish_haqi=super().calculate_salary()
    def __str__(self):
        return f"""sotuvchi: {self.ish_haqi}"""
a=Boshliq(20, 50)
a.update()

b=Developer(10, 30)
b.update()

c=Sotuvchi(20, 15)
c.update()

lst=[a,b,c]

print(max(lst, key=lambda x: x.maosh))
