class Vendor:
    def __init__(self, inventory=None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

        # refactor
        # try:
        #     self.inventory.remove(item)
        #     return item
        # except ValueError:
        #     return False

    def get_by_category(self, category):

        # utilized list comprehension
        category_items = [item for item in self.inventory if item.category == category]
        return category_items

