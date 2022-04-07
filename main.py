from swap_meet.vendor import Vendor
from swap_meet.item import Item

happy_item = Item(category = "Decor")
dan = Vendor(inventory = [happy_item])

# print(vars(dan))

# print(dir(dan))

dan.get_by_category("Hello")
# print(Vendor.__doc__)



print(happy_item.__doc__)
print(happy_item.category)
print(happy_item.condition_description())