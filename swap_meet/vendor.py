class Vendor:
    def __init__(self, inventory =[]):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            indx=self.inventory.index(item)
            item_removed=self.inventory.pop(indx)   
        else:
            return False
        return item_removed    

