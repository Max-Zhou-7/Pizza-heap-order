from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
class PizzaOrder(Pizza):
    def __init__(self,time):
        self.pizzas = []
        self.time = time
    def getTime(self):
        return self.time
    def setTime(self, time):
        self.time = time
    def addPizza(self,pizza):
        self.pizzas.append(pizza)
    def getOrderDescription(self):
        str = ""
        totalPrice = 0.0
        for i in self.pizzas:
            str = str + i.getPizzaDetails() +"\n"+"----\n"
            totalPrice = totalPrice + i.getPrice()
        return "******\nOrder Time: {}\n{}TOTAL ORDER PRICE: ${:.2f}\n******\n"\
.format(self.time,str,totalPrice)

cp1 = CustomPizza("S")
cp1.addTopping("extra cheese")
cp1.addTopping("sausage")
sp1 = SpecialtyPizza("S", "Carne-more")
order = PizzaOrder(123000) #12:30:00PM
order.addPizza(cp1)
order.addPizza(sp1)
print(PizzaOrder.getOrderDescription(order))
assert order.getOrderDescription() == \
"******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"