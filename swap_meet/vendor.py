class Vendor:
    '''A class that represents a participant at the swap meet.'''

    def __init__(self, inventory = None):
        self.inventory = inventory if inventory else []
    
    def add(self, add_value):
        '''Adds one or more items to the inventory. 
        
        As input, accepts either a single item, or an iterable of multiple
        items. If the input value is a single item, it is appended to the
        inventory. If the input value is an iterable, the 'add_multiple()'
        instance method is called on the value. 
        
        Items that are already in the inventory are silently ignored.
        
        Returns the input value.
        '''

        if hasattr(add_value, '__iter__') and type(add_value) is not str:
            return self.add_multiple(add_value)
        
        if add_value not in self.inventory:
            self.inventory.append(add_value)
        return add_value
    
    def add_multiple(self, items):
        '''Adds multiple items to the inventory.'''

        if type(items) is dict:
            raise ValueError('Passing input as a dictionary is not supported.')
        for item in items:
            if item in self.inventory:
                continue
            self.inventory.append(item)
        return items

    def remove(self, remove_value):
        '''Removes one or more items from the inventory. 
        
        As input, accepts either a single item, or an iterable of multiple
        items. If the input value is a single item, it is removed from the
        inventory. If the input value is an iterable, the 'remove_multiple()'
        instance method is called on the value. 
        
        If any item in the input is not present in the inventory, no changes
        are made.
        
        Returns the input value or False in the case that input contains an
        item not present in the inventory.
        '''

        if hasattr(remove_value, '__iter__') and type(remove_value) is not str:
            return self.remove_multiple(remove_value)
        
        if remove_value not in self.inventory:
            return False
        self.inventory.remove(remove_value)
        return remove_value
    
    def remove_multiple(self, items):
        '''Removes multiple items from the inventory.'''

        if type(items) is dict:
            raise ValueError('Passing input as a dictionary is not supported.')
        if not set(items) <= set(self.inventory):
            return False

        for item in items:
            self.inventory.remove(item)
    
    def get_by_category(self, category):
        '''Returns a list of all items in inventory of input category.'''

        return [item for item in self.inventory 
                if item.category == category]
    
    def swap_items(self, other_vendor, own_item, swap_item):
        '''Swaps an inventory item for an item in another vendor's inventory.
        
        Returns False if either input item is not found in the inventory of 
        the appropriate vendor. Otherwise, returns True.
        '''

        try:
            own_index = self.inventory.index(own_item)
            other_index = other_vendor.inventory.index(swap_item)
        except ValueError:         # item not found in appropriate inventory
            return False
        
        # handoff by index
        self.inventory[own_index], other_vendor.inventory[other_index] = \
                other_vendor.inventory[other_index], self.inventory[own_index]
        return True
    
    def swap_first_item(self,other_vendor):
        '''Swaps first item in inventory with another vendor's first item.
        
        Returns False if either inventory is empty. Otherwise, returns True.
        '''

        if not (self.inventory and other_vendor.inventory):
            return False
        
        self.inventory[0], other_vendor.inventory[0] = \
                                other_vendor.inventory[0], self.inventory[0]
        return True
    
    def get_best_by_category(self, category):
        '''Returns the item in the best condition of the input category.'''

        items = self.get_by_category(category)
        if len(items) == 0:
            return None
        ratings = [item.condition for item in items]
        return items[ratings.index(max(ratings))]
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        '''Swaps item with another vendor based on category and condition.
        
        Looks for the highest rated item in the other vendor's inventory
        with a category matching 'my_priority' and the highest rated item
        in the local inventory with a category matching 'their_priority'.
        If found the two items are swapped between the two inventories.

        Returns False if two appropriate items aren't found. Otherwise
        returns True.
        '''
        
        own_item = self.get_best_by_category(their_priority)
        swap_item = other.get_best_by_category(my_priority)
        
        if not (own_item and swap_item):
            return False
        return self.swap_items(other,own_item,swap_item)