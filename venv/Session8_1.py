# Session 8
# Problem 1: Advanced Counter Class

""" STATEMENT: Implement an advanced counter class. It can keep track of the quantity of each item
swiped and the price of a unit. See the pattern you must follow on the left and the example of
how it will be used and tested below.

It is probably best to use a dictionary with string keys and list values for the implementation,
but such details are up to you.

TEMPLATE:

TESTS:

See #Test1, #Test2, … in Statement """

class Counter:

    def __init__(self, my_id):
        self._items = 0
        self._total = 0
        self._items_added = dict()
        self._amounts_added = dict()
        self._id = my_id

#complete the code below;
#id is string;

    def add(self, item_name, amount, price_of_unit):
        self._items_added[item_name] = price_of_unit
        self._amounts_added[item_name] = amount
        self._items += amount
        self._total += amount * price_of_unit

#implement this method;
#item_name is string, amount is integer, price of unit is float
#adds amount of items with item_name and specifies price_of_unit
#you may assume that every addition for the same item_name will set
#the same price_of_unit
#see the examples of use in the instructions (right pane)

    def remove(self, item_name, amount):
        for key in self._amounts_added:
            if key == item_name:
                if self._amounts_added[item_name] >= amount:
                    self._amounts_added[item_name] -=amount
                    self._total -= amount * self._items_added[item_name]
                else:
                    self._total -= self._items_added[item_name] * self._amounts_added[item_name]
                    self._amounts_added.pop(item_name)

#implement this method;

#if the item_name is not among the items previously added, do nothing;
#if the item_name is among them but the amount is greater or equal to the
#number of previously added items with this name, remove the record
#associated with item_name;
#if the item_name is among them but the amount is less than the
#number of previously added items with this name, subtract the former quantity from the latter
#see the examples of use in the instructions (right pane)

    def reset(self):
        self._items = 0
        self._total = 0
        self._items_added = dict()
        self._amounts_added = dict()

#implement this method;

#simply erases info about all the items previously added;
#see the examples of use in the instructions (right pane)

    def get_total(self):
        return self._total

#implement this method;

#returns the float number representing the total price
#of all the items (think of due to pay) rounded to the 2nd fractional digit,
#use standard round(x,2) function

    def status(self):
        return "" + self._id + " " + str(self._items) + " " + str(self._total)

#implement this method;

#returs string "Id N M"
#where Id is id of counter, N is total amount of all items and M total price of them
#round M to the 2nd fractional digit
#see the examples of use in the instructions (right pane)


c = Counter("C001")
# Test1 checks if above not crashes
c.add("Spaghetti", 5, 1.8)
assert c.status()=="C001 5 9.0"
c.add("Ice Cream", 2, 3.4)
assert c.status()=="C001 7 15.8"
assert c.get_total()==15.8
c.add("Spaghetti", 3, 1.8)
assert c.status()=="C001 10 21.2"
c.remove("Ice Cream", 1)
assert c.status()=="C001 9 17.8"
c.reset()
c.add("Coke", 5, 1.45)
assert c.status()== "C001 5 7.25"