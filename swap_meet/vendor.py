class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory
    
    def add(self, item_to_add):
        self.inventory.append(item_to_add)
        return item_to_add
    
    def remove(self, item_to_remove):
        if item_to_remove in self.inventory:
            self.inventory.remove(item_to_remove)
            return item_to_remove
        return False

    def get_by_category(self, category):
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items
    
    def swap_items(self, another_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in another_vendor.inventory:
            return False
        self.remove(my_item)
        self.add(their_item)
        another_vendor.add(my_item)
        another_vendor.remove(their_item)
        return True
    
    def swap_first_item(self, another_vendor):
        if len(self.inventory) == 0 or len(another_vendor.inventory) == 0:
            return False
        self.add(another_vendor.remove(another_vendor.inventory[0]))
        another_vendor.add(self.remove(self.inventory[0]))
        return True