from swap_meet.vendor import Vendor
from swap_meet.item import Item

moist_item = Item()
danielle = Vendor()

print(vars(danielle))#prints attributes of this object as dictionary
print(dir(danielle))#prints all methods for this object

danielle.get_by_category("clothing")