from swap_meet.item import Item

class Vendor:
    '''
    Class that represents a vendor.
    ...

    Attributes
    - - - - - -
    inventory: default (None) -> empty list

    Methods
    -------
    add()
    remove()
    get_by_category()
    swap_items()
    swap_first_item()
    get_best_by_category()
    swap_best_by_category()
    '''
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
        
        self.inventory.remove(my_item)   # remove here being applied to a list
        vendor.inventory.remove(their_item) #add being applied to a list
        self.inventory.append(their_item)
        vendor.inventory.append(my_item)

        return True

    def swap_first_item(self, vendor):
        '''
        Swaps (removes/appends) first item from self.inventory and vendor.inventory, returns True
        If self.inventory or vendory.inventory empty, returns False.'''
        if not self.inventory or not vendor.inventory:
            return False
        
        first_item_self = self.inventory.pop(0)  #want to return value here and assign to variable
        first_item_vendor = vendor.inventory.pop(0)
        self.inventory.append(first_item_vendor)
        vendor.inventory.append(first_item_self)

        return True

    def get_best_by_category(self, category):
        '''
        Input: category (str), finds items in self.inventory whose category = input,
        returns item with highest value of attribute condition. 
        If self.inventory has no items with category, return None.
        '''
        category_list = self.get_by_category(category)
        if not category_list:
            return None
        condition = 0
        top_item = None
        for item in category_list:
                if item.condition > condition:
                    condition = item.condition
                    top_item = item
            
        return top_item 

    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        Input: other(instance of vendor), my_priority (category ->string), their_priority (category->string),
        swaps highest condition item from inventory of vendor and other based on priority category, 
        returns True.  If category not in inventories, return False.
        
        '''
        best_item_self = self.get_best_by_category(their_priority)
        best_item_other = other.get_best_by_category(my_priority)

        if not best_item_self or not best_item_other:
            return False
        
        return self.swap_items(other, best_item_self, best_item_other)

        



        