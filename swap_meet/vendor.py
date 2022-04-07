class Vendor:
    '''Creating Vendor class that has an inventory attribute which is an optional argument. Will be able to add, remove, look at
    item categories and item ages and be able to swap items with friends.'''
    def __init__(self, inventory=None): # O(1)
        if inventory is None: # shouldn't use mutable type as default parameter, so use None and then assign to empty list # O(1)
            inventory = [] 
        self.inventory = inventory 

    def add(self, item): # O(1)
        self.inventory.append(item) # O(1)
        return item 
    
    def remove(self, item): # O(1)
        if item in self.inventory: # O(1)
            self.inventory.remove(item) # O(1) 
            return item
        return False 

    def get_by_category(self, category): # O(n)
        '''Using list comprehension to store all items in self.inventory that have same category as category arg.
        Stores those items in items_same_categories list.'''
        items_same_categories = [item for item in self.inventory if item.category == category] # O(n)
        return items_same_categories 

    def swap_items(self, vendor, my_item, their_item): # O(1)
        if my_item in self.inventory and their_item in vendor.inventory: # O(1)
            vendor.add(my_item) # O(1)
            self.remove(my_item) # O(1)
            vendor.remove(their_item) # O(1)
            self.add(their_item) # O(1)
            return True
        return False 
    
    def swap_first_item(self, vendor): # O(1)
        if len(self.inventory) and len(vendor.inventory) != 0: # O(1)
            my_first_item = self.inventory[0]
            their_first_item = vendor.inventory[0]
            first_items_swapped = self.swap_items(vendor, my_first_item, their_first_item) # O(1)
            return first_items_swapped
    
    def get_best_by_category(self, category): # O(n)
        '''High order function. Using max with key that uses lambda function. Lambda function uses item as an argument and returns item.condition.
        Max sorts the items_same_categories list by customized key order and returns item with max item.condition.'''
        items_same_categories = self.get_by_category(category) # O(n)
        if len(items_same_categories) != 0:
            return max(items_same_categories, key = lambda item: item.condition) # O(n)
    
    def swap_best_by_category(self, other, my_priority, their_priority): # O(n)
        '''Using the get_best_by_category and swap_items as helper functions to swap
        items based on the category and the condition'''
        vendor_best_item_by_category = self.get_best_by_category(their_priority) # O(n)
        other_best_item_by_category = other.get_best_by_category(my_priority) # O(n)
        best_swapped_items = self.swap_items(other, vendor_best_item_by_category, other_best_item_by_category) # O(1)
        return best_swapped_items 

    def get_by_newest(self, category): # O(n)
        '''Looks at items in a certain category (passed as arg) and returns the item with the minimum age.
        High order function. Using min with key that uses lambda function. Lambda function uses item as an argument and returns item.age.
        Min sorts the items_same_categories list by customized key order and returns item with min item.age.'''
        items_same_categories = self.get_by_category(category) # O(n)
        if len(items_same_categories) != 0: # O(1)
            return min(items_same_categories, key = lambda item: item.age) # O(n)

    def swap_by_newest(self, other, my_priority_newest, their_priority_newest): # O(n)
        '''Using get_by_newest and swap_items as helper functions to swap items 
        based on the category and the age'''
        vendor_newest_item = self.get_by_newest(their_priority_newest) # O(n)
        other_newest_item = other.get_by_newest(my_priority_newest) # O(n)
        newest_swapped_items = self.swap_items(other, vendor_newest_item, other_newest_item) # O(1)
        return newest_swapped_items
        




