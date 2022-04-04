class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory # empty list by default
    
    def add(self, one_item):
        self.inventory.append(one_item)
        return one_item

    def remove(self, one_item):
        try:
            self.inventory.remove(one_item)
            return one_item
        except ValueError:
            return False
        
    def get_by_category(self, category_to_check):
        list_by_cat = [item for item in self.inventory if item.category == category_to_check]
        return list_by_cat