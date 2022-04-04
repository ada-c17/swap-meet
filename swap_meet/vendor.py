class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if not item in self.inventory:
            return False 
        self.inventory.remove(item)
        return item
    
    def get_by_category(self, category):
        list_items = []
        for item in self.inventory:
            if item.category == category:
                list_items.append(item)
        return list_items

    def swap_items(self, vendor, my_item, their_item):
        if not my_item in self.inventory or not their_item in vendor.inventory:
            return False
        self.remove(my_item)
        vendor.add(my_item)
        vendor.remove(their_item)
        self.add(their_item)
        return True
    
    def swap_first_item(self, vendor):
        if len(self.inventory) == 0 or len(vendor.inventory) == 0:
            return False
        my_first_item = self.inventory[0]
        friend_first_item = vendor.inventory[0]
        self.swap_items(vendor, my_first_item, friend_first_item)
        return True
