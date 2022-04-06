# from item import Item


class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item


    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

    def swap_items(self, friend_vendor, my_item, friend_item):
        if my_item not in self.inventory or friend_item \
            not in friend_vendor.inventory:
            return False
        self.inventory.remove(my_item)
        self.inventory.append(friend_item)
        friend_vendor.inventory.remove(friend_item)
        friend_vendor.inventory.append(my_item)
        return True
    
    def swap_first_item(self, friend_vendor):
        if not self.inventory or not friend_vendor.inventory:
            return False 
        self.inventory.append(friend_vendor.inventory[0])
        friend_vendor.inventory.append(self.inventory[0])
        self.inventory.pop(0)
        friend_vendor.inventory.pop(0)
        return True
        




# item_a = Item(category="clothing")
# item_b = Item(category="clothing")
# item_c = Item(category="clothing")
# fatimah = Vendor(
#     inventory=[item_a, item_b, item_c]
# )

# item_d = Item(category="electronics")
# item_e = Item(category="decor")
# jolie = Vendor(
#     inventory=[item_d, item_e]
# )

# result = fatimah.swap_first_item(jolie)