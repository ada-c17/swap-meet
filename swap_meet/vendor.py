class Vendor:
    '''Creating Vendor class that has an inventory attribute which is an optional argument. The add instance method adds a new item to inventory and the remove instance method
    removes an item if that item is found in the inventory list. If item is not found in list to remove, False is returned. '''
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
