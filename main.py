from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.electronics import  Electronics
from swap_meet.decor import Decor
from swap_meet.clothing import Clothing

decor1 = Decor()
clothing1 = Clothing()
electronics1 = Electronics()
decor2 = Decor(condition = 5, age = 3)
item1 = Item(category = "Misc", condition = 1, age = 10)

lindsey = Vendor([decor1, clothing1, electronics1, decor2, item1])

print(vars(lindsey)) #shows attributes and their values

print(dir(lindsey)) #shows methods of an object

print(lindsey.inventory[0])