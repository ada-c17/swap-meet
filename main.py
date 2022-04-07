import imp
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor


item_a = Clothing(condition=2.0)  # item_a.category = "clothing"
item_b = Decor(condition=2.0)
item_c = Clothing(condition=4.0)
item_d = Decor(condition=5.0)
item_e = Clothing(condition=3.0)
tai = Vendor(
    inventory=[item_a, item_b, item_c, item_d, item_e]
)
best_item = tai.get_best_by_category("Clothing")

print(vars(best_item))

# trenisha = Vendor()
# print(vars(items))
# print(vars(trenisha.inventory))
# print(vars(item_a))


# print(dir(moist_item))
# print(dir(trenisha))
