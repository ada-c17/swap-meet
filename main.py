from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

sweater_red = Clothing(age = 4, condition = 3)
sweater_blue = Clothing(age = 0.6, condition = 5)
ipad = Electronics(age = 2, condition = 4)
cat_tree = Decor(age = 5, condition = 1)
shark = Vendor([sweater_red,sweater_blue,ipad, cat_tree])

switch = Electronics(age = 1.5, condition = 3)
hat = Clothing(age = 3, condition = 3)
easter_flag = Decor(age = 4, condition = 3)
garden_decor = Decor(age = 1, condition = 5)
turtle = Vendor([switch, hat, easter_flag, garden_decor])

print(shark.inventory)
print(turtle.inventory)
print(ipad.condition)
print(cat_tree.age)
print(switch.category)

shark.get_best_by_category("Clothing")
result = shark.get_by_category("Decor")
print(result)

result2 = shark.swap_best_by_category(turtle, "Electronics", "Electronics")
print(result2)
print(shark.inventory)