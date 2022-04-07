from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
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
        self.category = category
        items = []

        for item in self.inventory:
            if item.category == category:
                items.append(item)
                
        return items

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False

        self.remove(my_item)
        self.add(their_item)
        vendor.add(my_item)
        vendor.remove(their_item)
        return True

    def swap_first_item(self, vendor):
        if len(self.inventory) == 0 or len(vendor.inventory) == 0:
            return False
            
        my_item = self.inventory[0]
        their_item = vendor.inventory[0]

        self.add(their_item)
        self.remove(my_item)
        vendor.add(my_item)
        vendor.remove(their_item)
        return True