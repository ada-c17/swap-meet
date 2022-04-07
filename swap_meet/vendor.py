class Vendor:
    
    def __init__(self, inventory=None):
        inventory = inventory if inventory is not None else []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        items_by_category = []
        for item in self.inventory:
            if item.category == category:
                items_by_category.append(item)
        return items_by_category
    
    def swap_items(self, other, my_item, their_item):
        if my_item not in self.inventory or their_item not in other.inventory:
            return False
        my_index = self.inventory.index(my_item)
        their_index = other.inventory.index(their_item)
        self.inventory[my_index] , other.inventory[their_index] = other.inventory[their_index] , self.inventory[my_index]
        return True


    def swap_first_item(self, other):
        if not self.inventory or not other.inventory:
            return False
        self.swap_items(other, self.inventory[0], other.inventory[0])
        return True

    
    def get_best_by_category(self, category):
        condition = -1
        best_item = None
        for item in self.inventory:
            if item.category == category and item.condition > condition:
                best_item = item
                condition = item.condition
        return best_item


    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if not my_best or not their_best:
            return False
        self.swap_items(other, my_best, their_best)
        return True


