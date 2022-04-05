from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory


    def add(self, item):
        self.inventory.append(item)
        return item
        

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False 

        # if item not in self.inventory:
        #     return False
        # self.inventory.remove(item)
        # return item


    def get_by_category(self, category):
        inventory_by_category = [] 
        for item in self.inventory:
            if item.category == category:
                inventory_by_category.append(item)
        # if item.category != category:
        #     return False 
        #return inventory_by_category
        
        if len(inventory_by_category) > 0:
            return inventory_by_category
        else:
            return False 
                
        
