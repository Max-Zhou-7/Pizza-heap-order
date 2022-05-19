from Pizza import Pizza
class SpecialtyPizza(Pizza):
    def __init__(self,size,name):
        self.size = size
        self.name = name
        if self.getSize() == "S":
            self.setPrice(12.0)
        elif self.getSize() == "M":
            self.setPrice(14.0)
        else:
            self.setPrice(16.0)
    def getPizzaDetails(self):
        return "SPECIALTY PIZZA\nSize: {}\nName: {}\n\
Price: ${:.2f}\n".format(self.size, \
self.name,self.getPrice())
    
# sp1 = SpecialtyPizza("S", "Carne-more")
# print(sp1.getPizzaDetails())
# assert sp1.getPizzaDetails() == \
# "SPECIALTY PIZZA\n\
# Size: S\n\
# Name: Carne-more\n\
# Price: $12.00\n"