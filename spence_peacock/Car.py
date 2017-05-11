class Car(object):
    def __init__(self,price,speed,fuel,mileage,tax=0):
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        self.tax=tax
    def setCar(self,price,speed,fuel,mileage):
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
    def setTax(price):
        if price>10000:
            self.tax=.15*self.price
        else:
            self.tax=.12*self.price
        return self
        #print self.tax
    def display_all(self):
        print "Price: {}".format(self.price)
        print "Speed: {}".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Mileage: {}".format(self.mileage)
        print "Tax: {}".format(self.tax)
        print " "
accord=Car(300,60,30,100000)
ferrari=Car(400,30,30,0)
camry=Car(500,60,40,5)
truck=Car(600,60,50,200)
dunebuggy=Car(100000,5,0,100)
jeep=Car(800,60,30,10)
print accord.display_all()
print ferrari.display_all()
print camry.display_all()
print truck.display_all()
print dunebuggy.display_all()
print jeep.display_all()