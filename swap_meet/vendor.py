class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item_to_add):
        self.inventory.append(item_to_add)
        return item_to_add
    
    def remove(self, item_to_remove):
        if item_to_remove not in self.inventory:
            return False

        self.inventory.remove(item_to_remove)
        return item_to_remove

    def get_by_category(self, category):
        items_in_category = []
        
        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)
        
        return items_in_category