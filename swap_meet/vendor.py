from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory
    
    def add(self, new_item):
        """Add a new item to inventory"""

        self.inventory.append(new_item)
        return new_item
    
    def remove(self, discarded_item):
        """Remove an item from inventory"""

        if discarded_item not in self.inventory:
            return False
        else: 
            self.inventory.remove(discarded_item)
            return discarded_item
    
    def get_by_category(self, category_string):
        """Return list of items from inventory of a certain category"""
        
        item_list = []
        for item in self.inventory:
            if item.category == category_string:
                item_list.append(item)
        if not item_list:
            return None
        else:
            return item_list