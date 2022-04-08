from operator import inv
from swap_meet.vendor import Vendor
from swap_meet.item import Item

item_a = Item("Clothing", condition = 4.0)
item_b = Item("Electronics", condition = 3.0)
item_c = Item("Decor")

vendor_1 = Vendor()

list = vendor_1.add(item_a)


print(vendor_1)