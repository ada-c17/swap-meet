from swap_meet.item import Item

class Vendor:
    
    # constructor for class Vendor
    def __init__(self, inventory = []):
        self.inventory = inventory

    # method to add item to inventory
    def add(self, item):
        self.inventory.append(item)
        return item
    
    # method to remove item from inventory
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    # method to return list of items by item category
    def get_by_category(self, category):
        item = Item()
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    # method to swap from vendor's inventory to friend's inventory
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            other_vendor.add(my_item)
            return True
        return False