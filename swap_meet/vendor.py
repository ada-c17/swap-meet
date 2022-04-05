#from .item import Item
class Vendor:
    
    def __init__(self, inventory=None):
        if not inventory:
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
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    
    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.inventory.remove(my_item)
            friend.inventory.append(my_item)
            friend.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        #return False

    def swap_first_item(self, friend):
        if self.inventory and friend.inventory:
            self.inventory[0] , friend.inventory[0] = friend.inventory[0] , self.inventory[0]
            return True
        #return False
    
    def get_best_by_category(self, category):
        condition = 0
        best_item = None
        for item in self.inventory:
            if item.category == category:
                if item.condition > condition:
                    best_item = item
                    condition = item.condition
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if my_best and their_best:
            self.swap_items(other, my_best, their_best)
            return True


