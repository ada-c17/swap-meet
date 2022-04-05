from swap_meet.item import Item

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
        Removes item from attribute inventory if item in list, returns item. 
        If item not in self.inventory, returns False.
        ''' 
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        '''
        Returns list of items from inventory whose attribute category == input category string.
        '''
        category_list = []
        for item in self.inventory:
            if category == item.category:
                category_list.append(item)
        return category_list
        
    def swap_items(self, vendor, my_item, their_item):
        '''
        Swaps (removes/appends) input items (my_item, their_item) from instance inventory and vendor inventory; returns True.
        If my_item, their_item not in self.inventory and vendor.inventory, respsectively, returns False.
        '''
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        
        #can/cannot invoke previously made instances methods remove()/add() on instances self and vendor b/c of return?
        self.inventory.remove(my_item)   # have you overwritten python fnx for remove?
        vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        vendor.inventory.append(my_item)

        return True

    def swap_first_item(self, vendor):
        '''
        Swaps (removes/appends) first item from self.inventory and vendor.inventory, returns True
        If self.inventory or vendory.inventory empty, returns False'''
        if not self.inventory or not vendor.inventory:
            return False
        
        first_item_self = self.inventory.pop(0)  #want to return value here and assign to variable
        first_item_vendor = vendor.inventory.pop(0)
        self.inventory.append(first_item_vendor)
        vendor.inventory.append(first_item_self)

        return True

        