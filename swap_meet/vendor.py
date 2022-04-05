from .item import Item
class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        
    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        return category_list
    
    def swap_items(self, vendor_friend, my_item, their_item):
        
        if my_item in self.inventory and their_item in vendor_friend.inventory:
            self.remove(my_item)
            vendor_friend.add(my_item)
            vendor_friend.remove(their_item)
            self.add(their_item)
            return True
        else:
            return False
        
    def swap_first_item(self, vendor_friend):
        if len(self.inventory) == 0 or len(vendor_friend.inventory) == 0:
            return False
        self.add(vendor_friend.inventory[0])
        vendor_friend.add(self.inventory[0])
        self.remove(self.inventory[0])
        vendor_friend.remove(vendor_friend.inventory[0])
        return True