from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing


vendor = Vendor(inventory=["a", "b", "c"])
print(vendor.inventory)

hat = Item(category="clothing")
sock = Clothing()
shirt = Item(category="clothing")
phone = Item(category="electronics")
fatimah = Vendor(inventory=[hat, shirt, phone])
print(fatimah.inventory)
print(hat)
print(sock)