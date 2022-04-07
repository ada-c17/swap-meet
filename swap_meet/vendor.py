
class Vendor:
    def __init__(self, inventory=None):
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
        except ValueError as error:
            return False
    
    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory: 
            if item.category == category:
                items_in_category.append(item)
        return items_in_category

    def swap_items(self, other, my_item, their_item):
        
        if my_item not in self.inventory or their_item not in other.inventory:
            return False
        
        self.add(their_item)
        other.add(my_item)
        self.remove(my_item)
        other.remove(their_item)
        return True
    
    def swap_first_item(self, other):

        if not self.inventory or not other.inventory:
            return False

        self.swap_items(other, self.inventory[0], other.inventory[0])
        return True

    def get_best_by_category(self, category):
        
        items_in_category = [item for item in self.inventory if item.category == category]
        
        if not items_in_category:
            return None
        
        best_item = max(items_in_category, key=lambda item: item.condition)

        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        if not my_item or not their_item: 
            return False
        
        self.swap_items(other, my_item, their_item)
        return True

                

        
    