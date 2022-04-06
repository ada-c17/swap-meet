from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

stereo = Electronics(3)
print(vars(stereo))
dress = Clothing(5)
print (dress.condition_description())
