# from swap_meet.item import Item

class Vendor:
    #insert doc strings

    def __init__(self, inventory = None):
        '''
        Constructs attributes for Vendor object, default inventory value is empty list.
        '''
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        '''
        Adds item to attribute inventory, returns item.
        '''
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        '''
        Removes item from attribute inventory if item in list, returns item; else returns False.
        ''' 
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        '''
        Returns list of items from inventory whose attribute category equals input category string.
        '''
        category_list = []
        for item in self.inventory:
            if category == item.category:
                category_list.append(item)
        return category_list

    def swap_items(self, vendor, my_item, their_item):
        '''
        Swaps (removes/appends) items from instance inventory and vendor inventory; returns True.
        '''
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        
        self.inventory.remove(my_item)
        vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        vendor.inventory.append(my_item)

        return True
        