class Bike(object):
    def __init__(self,price,max_speed,miles=0):
        self.price=price
        self.max_speed=max_speed
        self.miles=miles
    def ride(self,num):
        self.miles+=10*num
        return self
    def reverse(self,num):
        self.miles -=10*num
        return self
    def displayinfo(self):
        print "The Price is {} The Maximum speed is {}. It has {} miles on it ".format(self.price,self.max_speed,self.miles)
cannondale = Bike(1000,35, )
giantdefy = Bike(600,20,)
bianchi = Bike(1500,35,)
cannondale.ride(3)
cannondale.reverse(1)
giantdefy.ride(2)
giantdefy.reverse(2)
print cannondale.displayinfo()
print giantdefy.displayinfo()
print bianchi.displayinfo()