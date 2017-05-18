class product(object):
    def __init__(self, name,weight,brand,cost,status="for sale"):
        self.name=name
        self.weight=weight
        self.brand=brand
        self.cost=cost
        self.status='for sale'
    def sell(self):
        self.status="sold"
    def addTax(self):
        self.tax= self.cost*1.12
        print self.tax
        return self
    def returnit(reason):
        if reason == 'defective':
            self.cost=0
        else:
            self.cost=self.cost* 0.80
            return self
    def displayinfo(self):
        print "%s %s %s %s %s" % (self.name,self.weight,self.brand,self.cost,self.status)
sweetride = product('propel','7lbs','giant',700)
sweetride.displayinfo()
sweetride.sell()
sweetride.status
sweetride.addTax()

