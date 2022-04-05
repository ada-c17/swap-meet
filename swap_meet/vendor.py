class Vendor:

    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        category_match = []
        for item in self.inventory:
            if item.category == category:
                category_match.append(item)
        return category_match

    def swap_items(self, Vendor, my_item, their_item):
        pass

    def swap_first_item(self, Vendor):
        pass

    def get_best_by_category(self, category=""):
        pass

    def swap_best_by_category(self, other, my_priority, their_priority):
        pass