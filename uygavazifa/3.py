class Vehicle:
    def __init__(self, day:int):
        self.day=day
    
    def rental_car(self):
        return self.day*50
    
    def rental_bike(self):
        return self.day*10
    
    def rental_truck(self):
        return self.day*100
    
class Car(Vehicle):
    def __init__(self, day:int):
        super().__init__(day)
    def chiqar(self):
        return f"mashina shuncha narh turadi:  {super().rental_car()}$"

class Truck (Vehicle):
    def __init__(self, day:int):
        super().__init__(day)
    def chiz(self):
        print(f"Yuk mashinasi shuncha narhda turadi: {super().rental_truck()}$")    

class Bike (Vehicle):
    def __init__(self, day:int):
        super().__init__(day)
    def yoz(self):
        print(f"velosiped shuncha narhda turadi: {super().rental_bike()}$")

n=int(input("nechchi kunga mashina olmoqchisiz: "))
m=int(input("necha kunga yuk mashinasini sotib olmoqchisiz: "))
b=int(input("necha kunga velosiped sotib olmoqchisiz: "))
print("narhlar: ->")
c=Car(n)
print(c.chiqar())

t=Truck(m)
t.chiz()

g=Bike(b)
g.yoz()