# from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
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
        return False
    
    def get_by_category(self, category):
        category_items =[]
        for item in self.inventory:
            if category == item.category:
                category_items.append(item)
        return category_items
        
    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        self.remove(my_item)
        friend.add(my_item)
        friend.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, friend):
        if self.inventory == [] or friend.inventory == []:
            return False
        self.swap_items(friend, self.inventory[0], friend.inventory[0])
        return True

    def get_best_by_category(self, category):
        categoty_items = self.get_by_category(category)
        if categoty_items == []:
            return None
        best_item = categoty_items[0]
        for item in categoty_items:
            if item.condition > best_item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        if my_best_item is None or their_best_item is None:
            return False
        self.swap_items(other, my_best_item, their_best_item)
        return True
