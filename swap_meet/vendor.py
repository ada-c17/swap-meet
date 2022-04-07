class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_category(self, category):
        """gets items in inventory of given category"""
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

        self.inventory[my_index], other.inventory[their_index] = other.inventory[their_index], self.inventory[my_index]
        
        return True
    
    def swap_first_item(self, other):
        if not self.inventory or not other.inventory:
            return False

        my_item = self.inventory[0]
        their_item = other.inventory[0]

        return self.swap_items(other, my_item, their_item)
    
    def get_best_by_category(self, category):
        items_by_category = self.get_by_category(category)
        best_item = None
        best_condition = 0

        for item in items_by_category:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item

        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item_by_category = self.get_best_by_category(their_priority)
        their_best_item_by_category = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_best_item_by_category, their_best_item_by_category)
