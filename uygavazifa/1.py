class Shape:
    def __init__(self, tortburchak:list, doira:list, uchburchak:list) -> None:
        self.tortburchak=tortburchak
        self.doira=doira
        self.uchburchak=uchburchak
        # self.kv_tortbut=0
        
    def calculate_area_tort(self):
        return sum(self.tortburchak)*2
    def calculate_area_doira(self):
        return  sum(self.doira)**2*3.14
    def hisobla_yuzasi(self):
        a=self.uchburchak[0]
        b=self.uchburchak[1]
        c=self.uchburchak[2]
        S = (a + b + c) / 2
        return S

class Restangle(Shape):
    def __init__(self,a:int,b:int):
        super().__init__([a,b],None,None)
    def __str__(self):
        return f"tortburchakning yuzi {super().calculate_area_tort()}"


class Doira(Shape):
    def __init__(self, radius:int):
        super().__init__(None, [radius], None)
    def __str__(self):
        return f"Circlening yuzi {super().calculate_area_doira()}"


class  Uchburchak(Shape):
    def __init__(self, a:int, b:int, c:int):
        super().__init__(None, None, [a,b,c])
    def __str__(self):
        return f"uchburchakning yuzi {super().hisobla_yuzasi()}"


a=Restangle(10,29)
print(a)
b=Doira(34)
print(b)
c=Uchburchak(10,20,30)
print(c)
