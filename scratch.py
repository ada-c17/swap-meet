# pytest --cov=swap_meet --cov-report html --cov-report term
# open htmlcov/index.html
# run from project root folder

# double check no changes made to inventroy
# still had all items in it

from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.electronics import Electronics

new_item = Item()
new_vendor = Vendor(inventory=[new_item])
phone = Electronics(5)

# print(new_item)
# print(vars(new_vendor))

# new_vendor.get_by_category("")

# print(dir(new_vendor))
# print(new_item.color)
# print(phone.category)
# print(phone.color)
# print(phone.condition)

print(type(new_vendor))