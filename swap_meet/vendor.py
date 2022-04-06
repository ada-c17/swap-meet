class Vendor:
    '''Creating Vendor class that has an inventory attribute which is an optional argument. The add instance method adds a new item to inventory and the remove instance method
    removes an item if that item is found in the inventory list. If item is not found in list to remove, False is returned. '''
    def __init__(self, inventory=None): 
        if inventory is None: # shouldn't use mutable type as default parameter, so use None and then assign to empty list # O(1)
            inventory = [] 
        self.inventory = inventory 

    def add(self, item):
        self.inventory.append(item) # O(1)
        return item 
    
    def remove(self, item):
        if item in self.inventory: # O(1)
            self.inventory.remove(item) # O(1) 
            return item
        return False 

    def get_by_category(self, category):
        items_with_categories = [] 
        for item in self.inventory: # O(n)
            if item.category == category: # O(1)
                items_with_categories.append(item) # O(1)      
        return items_with_categories 

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            vendor.inventory.append(my_item)
            self.remove(my_item)
            vendor.inventory.remove(their_item)
            self.add(their_item)
            return True
        return False 
    

