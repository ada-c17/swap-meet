from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
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
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, friend, given_item, received_item):
        if given_item in self.inventory and received_item in friend.inventory:
            friend.add(given_item)
            self.remove(given_item)
            self.add(received_item)
            friend.remove(received_item)
            return True
        return False 

# ********************************
# DELETE LATER
# ********************************

# ********************************
# ********************************