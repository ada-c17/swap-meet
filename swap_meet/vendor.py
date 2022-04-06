class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        try:
            self.inventory.remove(item)
        except ValueError:
            print("That item is not in the inventory.")
            return False
        else:
            return item
    
    def get_by_category(self, category):
        items_with_category = [item for item in self.inventory if item.category == category]
        return items_with_category