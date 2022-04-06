from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.electronics import Electronics
from swap_meet.decor import Decor


i = Item("bag")

string_return = i.__str__()

print(string_return)

print(repr(i))

shirt = Clothing()

print(str(shirt))
print(repr(shirt))
print(shirt.condition)
print(shirt.category)
print(shirt.condition_description())