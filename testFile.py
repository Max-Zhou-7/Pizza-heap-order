from Pizza import Pizza
from PizzaOrder import PizzaOrder
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from OrderQueue import OrderQueue
def test_customPizzaDetails():
    cp1 = CustomPizza("L")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    #print(cp1.getPizzaDetails())
    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $14.00\n" 
def test_speciaPizzaDetials():
    sp1 = SpecialtyPizza("S", "Carne-more")
    #print(sp1.getPizzaDetails())
    assert sp1.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"
def test_orderDescription():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000) #12:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)
    #print(PizzaOrder.getOrderDescription(order))
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


