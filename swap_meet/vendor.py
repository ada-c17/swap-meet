class Vendor:
    
    def __init__(self, inventory = []):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in set(self.inventory):
            self.inventory.remove(item)
            return item
        else:
            return False
    
    def get_by_category(self, category):
        cat_list = []
        for i in self.inventory:
            if i.category == category:
                cat_list.append(i)
        return cat_list
