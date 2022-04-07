class Vendor:
    # TODO: Create a better docstring and add comments in parts to explain logic
    '''Creating Vendor class that has an inventory attribute which is an optional argument. The add instance method adds a new item to inventory and the remove instance method
    removes an item if that item is found in the inventory list. If item is not found in list to remove, False is returned. '''
    def __init__(self, inventory=None): 
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
        items_same_categories = [] 
        for item in self.inventory: # O(n)
            if item.category == category: # O(1)
                items_same_categories.append(item) # O(1)      
        return items_same_categories 

    def swap_items(self, vendor, my_item, their_item): # O(1)
        if my_item in self.inventory and their_item in vendor.inventory: # O(1)
            vendor.inventory.append(my_item) # O(1)
            self.remove(my_item) # O(1)
            vendor.inventory.remove(their_item) # O(1)
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
        # TODO: write comments for lambda f(x)
        items_same_categories = self.get_by_category(category) # O(n)
        if len(items_same_categories) != 0:
            return max(items_same_categories, key = lambda item: item.condition) # O(n)
    
        # item_best_condition = None
        # max_condition = 0.0
        # for item in items_same_categories: # O(n)
        #     if item.condition > max_condition: # O(1)
        #         max_condition = item.condition
        #         item_best_condition = item 
        # return item_best_condition
    
    def swap_best_by_category(self, other, my_priority, their_priority): # O(n)
        vendor_best_item_by_category = self.get_best_by_category(their_priority) # O(n)
        other_best_item_by_category = other.get_best_by_category(my_priority) # O(n)
        best_swapped_items = self.swap_items(other, vendor_best_item_by_category, other_best_item_by_category) # O(1)
        return best_swapped_items 

    def get_by_newest(self, category):
        items_same_categories = self.get_by_category(category) # O(n)
        print(items_same_categories)
        if len(items_same_categories) != 0:
            return min(items_same_categories, key = lambda item: item.age)

    def swap_by_newest(self, other , my_priority_newest, their_priority_newest):
        vendor_newest_item = self.get_by_newest(their_priority_newest)
        other_newest_item = other.get_by_newest(my_priority_newest)
        newest_swapped_items = self.swap_items(other, vendor_newest_item, other_newest_item)
        return newest_swapped_items
            




