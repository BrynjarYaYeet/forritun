import math
import random
"""
class Bill():
    def __init__(self, nafn, nr):
        self.nafn=nafn
        self.nr=nr
    def upl(self):
        print(self.nafn, self.nr)
class Bla():
    def heilsa():
        print("hallo")

biLL1=Bill("Toyota", "ab-123")
bill2=Bill("Ford", "qw-652")

print(bill2.upl())
Bla.heilsa()


#dæmi1
class TrapisaTest():
    teljari=0
    def __init__(self, a=0, b=0, c=0, d=0, h=0):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.h=h
        TrapisaTest.teljari+=1

    def ummal_trapisu(self):
        um = self.a + self.b + self.c + self.d
        print("Ummál trapisunar er:", um)
        return " "

    def flatarmal_trapisu1(self):
        s=(self.a + self.b + self.c + self.d)/2
        sum=self.a + self.c
        sum1= self.a - self.c
        sum2=sum/sum1
        sum3= (s-self.c)*(s-self.a)*(s-self.c-self.b)*(s-self.c-self.d)
        sum4=math.sqrt(sum3)
        sum5=sum2*sum4
        print("Flatarmál ef a og c eru samsíða línur:", format(sum5, ".1f"))
        return " "



    def flatarmal_trapisu2(self):
        sum=self.a + self.c
        sum2= sum/2
        um=sum2*self.h
        print("Flatarmál ef a og b eru samsíða línur:", um)
        return" "

    def trapisa_jafnarma(self):
        if self.b==self.d or self.a==self.c:
            return True
        else:
            return False
        

    def lestu_mig(self):
        return "Trapisa eða hálfsamsíðungur er ferhyrningur þar sem tvær mótlægar hliðar eru samsíða. "

m1=TrapisaTest(9, 5, 4, 2, 6)
print(m1.ummal_trapisu())
print(m1.flatarmal_trapisu1())
print(m1.flatarmal_trapisu2())
print(m1.trapisa_jafnarma())
print(m1.lestu_mig())

"""


class Bill():
    def __init__(self, tegund, argerd, hradi, bensin, eydsla):
        self.tegund=tegund
        self.argerd=argerd
        self.hradi=hradi
        self.bensin=bensin
        self.eydsla=eydsla

    def numer1(self):
        return self.hradi


bill1=Bill("Toyota", "2016", random.randint(20, 40), random.randint(70, 130), random.randint(7, 13))
bill2=Bill("Honda", "2003", random.randint(20, 40), random.randint(70, 130), random.randint(7, 13))
bill3=Bill("Ferrari", "2018", random.randint(20, 40), random.randint(70, 130), random.randint(7, 13))

#print(bill1.numer1())


hradi=bill1.hradi
print(hradi, "m/s")

lengdbrautar=1000

timi=format(lengdbrautar/hradi, ".3f")
print(timi, "sec")

bensin=bill1.bensin
print(bensin, "lítrar")

eydsla=bill1.eydsla
print(eydsla, "lítrar/100m")

eytt= eydsla*10
print(eytt, "lítrum var eytt")








