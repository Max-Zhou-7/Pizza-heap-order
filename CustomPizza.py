from Pizza import Pizza
class CustomPizza(Pizza):
    def __init__(self,size):
        self.size = size
        if self.getSize() == "S":
            self.setPrice(8.0) 
        elif self.getSize() == "M":
            self.setPrice(10.0)
        else:
            self.setPrice(12.0)
        self.toppingList = []
    def addTopping(self, topping):
        self.toppingList.append(topping)
        if self.getSize() == "S":
            self.setPrice(self.getPrice()+0.5)
        elif self.getSize() == "M":
            self.setPrice(self.getPrice()+0.75)
        else:
            self.setPrice(self.getPrice()+1.0)
        
    def getPizzaDetails(self):
        str = ""
        for i in self.toppingList:
             str = str + "\t+ " + i + "\n" 
            
        return "CUSTOM PIZZA\nSize: {}\nToppings:\n{}\
Price: ${:.2f}\n".format(self.size, \
            str,self.getPrice())
    
# cp1 = CustomPizza("L")
# cp1.addTopping("extra cheese")
# cp1.addTopping("sausage")
# print(cp1.getPizzaDetails())
# assert cp1.getPizzaDetails() == \
# "CUSTOM PIZZA\n\
# Size: L\n\
# Toppings:\n\
# \t+ extra cheese\n\
# \t+ sausage\n\
# Price: $14.00\n" 
