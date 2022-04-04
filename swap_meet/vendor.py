class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        try:
            item_index = self.inventory.index(item)
            return self.inventory.pop(item_index)
        except ValueError:
            return False

    def get_by_category(self, category):
        # Returns a list of Items in the inventory with that category
        items_by_category = [item for item in self.inventory if item.category == category]
        return items_by_category