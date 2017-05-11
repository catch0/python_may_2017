class Car(object):
    def __init__(self,price,speed,fuel,mileage,tax=0):
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        if price>10000:
            self.tax=1.15
        else:
            self.tax=1.12
    def display_all(self):
        print "Price: {}".format(self.price)
        print "Speed: {}".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Mileage: {}".format(self.mileage)
        print "Tax: {}".format(self.tax)
        print " "
accord=Car(2000,"35mph","Full","15mpg")
datsun=Car(2000,"5mph","Not Full","105mpg")
camry=Car(2000,"15mph","Kind of Full","95mpg")
truck=Car(2000,"25mph","Full", "25mpg")
dunebuggy=Car(2000,"45mph","Empty","25mpg")
jeep=Car(20000,"35mph","Empty","15mpg")
accord.display_all()
datsun.display_all()
camry.display_all()
truck.display_all()
dunebuggy.display_all()
jeep.display_all()