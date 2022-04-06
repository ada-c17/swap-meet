from swap_meet.vendor import Vendor
from swap_meet.item import Item


headphone = Item("Electronics")
shoes = Item("Clothing")
laptop = Item("Electronics")

chi = Vendor([headphone, shoes, laptop])


print(chi.get_best_by_category("Electronics"))