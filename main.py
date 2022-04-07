from swap_meet.vendor import Vendor
from swap_meet.item import Item 


Olly = Vendor(["ball", "bone"])

Olly.show_items()


Sarah = Vendor(["cameron", "hammond"])

Sarah.show_items()
Sarah.add("burger")
Sarah.show_items()
Sarah.remove("hammond")


# moist_item = Item 
# trenisha = Item 

# print(vars(trenisha))
