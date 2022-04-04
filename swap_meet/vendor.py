class Vendor:
    def __init__(self, inventory=[]): 
        self.inventory = inventory
    
    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item 
    
    def remove(self, rem_item):
        if rem_item in self.inventory:
            self.inventory.remove(rem_item)
            return rem_item
        return False 
