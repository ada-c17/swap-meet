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
        return False

    def get_by_category(self, specific_category):
        category_matches = []
        for item in self.inventory:
            if item.category == specific_category:
                category_matches.append(item)
        return category_matches

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            friend.inventory.append(my_item)
            self.inventory.remove(my_item)
            
            self.inventory.append(their_item)
            friend.inventory.remove(their_item)
            return True
        return False
    
    def swap_first_item(self, friend):
        if self.inventory and friend.inventory:
            friend.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])

            self.inventory.append(friend.inventory[0])
            friend.inventory.remove(friend.inventory[0])
            return True
        return False
    
    def get_best_by_category(self, specific_category):
        best_by_category = None
        highest_condition = 0
        
        for item in self.inventory:
            if item.category == specific_category and item.condition > highest_condition:
                    best_by_category = item
                    highest_condition = item.condition

        return best_by_category
        
    def swap_best_by_category(self, other, my_priority, their_priority):
        
        their_best_item = self.get_best_by_category(their_priority)
        my_best_item = other.get_best_by_category(my_priority)

        if not their_best_item or not my_best_item:
            return False
        
        swapped_items = self.swap_items(other, their_best_item, my_best_item)
        return swapped_items