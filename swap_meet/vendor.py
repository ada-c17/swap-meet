class Vendor:
    '''Creating Vendor class that has an inventory attribute which is an optional argument. Will be able to add, remove, look at
    item categories and item ages and be able to swap items with friends.'''
    def __init__(self, inventory=None): # O(1)
        if inventory is None: # O(1)
            inventory = [] 
        self.inventory = inventory 


    def add(self, item:str): # O(1)
        '''
        Returns item that has been appended to inventory list.
        Parameters: item '''
        self.inventory.append(item) # O(1)
        return item 
    

    def remove(self, item:str): # O(1)
        '''
        Returns item that has been removed from inventory list.
        Parameters: item''' 
        if item in self.inventory: # O(1)
            self.inventory.remove(item) # O(1) 
            return item
        return False      


    def get_by_category(self, category:str): # O(n)
        '''
        Returns list that has items of same type category stored. 
        Parameters: category'''
        items_same_categories = [item for item in self.inventory if item.category == category] # O(n)
        return items_same_categories 


    def swap_items(self, vendor:list, my_item:str, their_item:str): # O(1)
        '''
        Returns True if items were swapped. Returns False if items were not swapped.
        Parameters: vendor - instance of Vendor, my_item - instance of Item - my item to be swapped,
        their_item - instance of Item - their item to be swapped.'''
        if my_item in self.inventory and their_item in vendor.inventory: # O(1)
            vendor.add(my_item) # O(1)
            self.remove(my_item) # O(1)
            vendor.remove(their_item) # O(1)
            self.add(their_item) # O(1)
            return True
        return False 
    

    def swap_first_item(self, vendor:list): # O(1)
        '''
        Returns True if first items were swapped. Returns false if first items were not swapped.
        Parameters: vendor - instance of Vendor. 
        '''
        if len(self.inventory) and len(vendor.inventory) != 0: # O(1)
            my_first_item = self.inventory[0]
            their_first_item = vendor.inventory[0]
            first_items_swapped = self.swap_items(vendor, my_first_item, their_first_item) # O(1)
            return first_items_swapped


    def get_best_by_category(self, category:str): # O(n)
        '''
        Returns item in a specific category that has best item condition (max condition). 
        Parameters: category
        '''
        items_same_categories = self.get_by_category(category) # O(n)
        if len(items_same_categories) != 0:
            # Lambda uses item as arg and returns item.condition
            return max(items_same_categories, key = lambda item: item.condition) # O(n)


    def swap_best_by_category(self, other:list, my_priority:str, their_priority:str): # O(n)
        '''
        Returns True if items were swapped. Returns false if items were not swapped.
        Parameters: other - instance of Vendor class, my_priority, 
        their_priority
        '''
        vendor_best_item_by_category = self.get_best_by_category(their_priority) # O(n)
        other_best_item_by_category = other.get_best_by_category(my_priority) # O(n)
        best_swapped_items = self.swap_items(other, vendor_best_item_by_category, other_best_item_by_category) # O(1)
        return best_swapped_items 


    def get_by_newest(self, category:str): # O(n)
        '''
        Returns newest item in specific category.
        Parameters: category
        '''
        items_same_categories = self.get_by_category(category) # O(n)
        if len(items_same_categories) != 0: # O(1)
            # Lambda uses item as arg and returns item.age
            return min(items_same_categories, key = lambda item: item.age) # O(n)


    def swap_by_newest(self, other:list, my_priority_newest:str, their_priority_newest:str): # O(n)
        '''
        Returns True if items were swapped. Returns false if items were not swapped.
        Parameters: other - instance of Vendor class, my_priority_newest, 
        their_priority_newest
        '''
        vendor_newest_item = self.get_by_newest(their_priority_newest) # O(n)
        other_newest_item = other.get_by_newest(my_priority_newest) # O(n)
        newest_swapped_items = self.swap_items(other, vendor_newest_item, other_newest_item) # O(1)
        return newest_swapped_items
        




