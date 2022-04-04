
class Vendor:
    def __init__(self, inventory=[]):
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