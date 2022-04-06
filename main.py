from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

item_a = Clothing(condition=2.0)
item_b = Decor(condition=2.0)
item_c = Clothing(condition=4.0)
item_d = Decor(condition=5.0)
item_e = Clothing(condition=3.0)

thu = Vendor([item_a, item_b, item_c, item_d, item_e])

best_item = thu.get_best_by_category("Clothing")

print(best_item.condition)