class Product:
    def __init__ (self, nomi:str):
        self.nomi=nomi
    def tekshir_el (self):
        if self.nomi.lower() in ["kabel", "zaryadnik", "telefon"]:
            return True
    def tekshir_kiy(self):
        if self.nomi.lower() in ["kiyim", "sumka", "kurtka"]:
            return True
    def tekshir_kitob(self):
        if self.nomi.lower() in ["kitob", "daftar", "ruchka"]:
            return True

class Clothing(Product):
    def __init__(self,name:str):
        super().__init__(name)
    def yoz(self):
        if super().tekshir_kiy():
            print("siz kiyim tanladingiz yerkazib berish 20K")

class Book(Product):
    def __init__ (self, name:str):
        super().__init__(name)
    def chop_et(self):
        if super().tekshir_kitob():
            print("siz oquv qurollarini tanladingiz yetkazib berish 10K")


class Elektronics(Product):
    def __init__(self, name:str):
        super().__init__(name)

    def chiqar(self):
        if super().tekshir_el():
            print("siz elektronik mahsulot tanladingiz yetkazib berish 50 k")

tanlov=input("sotib olmoqcho bolgan narsangizni kiriting: ")
a=Elektronics(tanlov)
b=Clothing(tanlov)
c=Book(tanlov)
a.chiqar()
b.yoz()
c.chop_et()