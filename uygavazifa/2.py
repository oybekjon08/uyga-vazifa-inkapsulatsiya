class Animal:
    def dog_crate_voise(self):
        return "Wow"
    def cat_crate_voise(self):
        return "Meow"
    def dusk_crate_voise(self):
        return "G'aq-g'aq"

class Dog(Animal):
    def chiqar(self):
        return super().dog_crate_voise()
class Cat(Animal):
    def yoz(self):
        return super().cat_crate_voise()
class Dusk(Animal):
    def chop_et(self):
        return super().dusk_crate_voise()


lst=[]
a=Dog()
a1=Dog()
a2=Dog()

lst.append(a.chiqar())
lst.append(a1.chiqar())
lst.append(a2.chiqar())
b=Cat()
b1=Cat()
b2=Cat()

lst.append(b.yoz())
lst.append(b1.yoz())
lst.append(b2.yoz())

c=Dusk()
c1=Dusk()
c2=Dusk()

lst.append(c.chop_et())
lst.append(c1.chop_et())
lst.append(c2.chop_et())
m=0
if lst.count("Wow")>0:
    m+=1
if lst.count("Meow")>0:
    m+=1
if lst.count("G'aq-g'aq")>0:
    m+=1
print(lst)
print(f"shuncha hil ovoz soni bor: {m}")