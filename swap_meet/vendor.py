from operator import attrgetter

class Vendor:

    def __init__(self, inventory=None):
        '''Initializes a Vendor object with optional inventory argument'''
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        '''Takes in item object, appends it to inventory'''
        self.inventory.append(item)
        return item

    def remove(self, item):
        '''Takes in item object, removes it from inventory''' 
        if item not in self.inventory:
            return False    
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        '''Input: category(string), returns inventory list
        with items of that category'''
        return [item for item in self.inventory if item.category == category]
        
    def swap_items(self, other, my_item, their_item):
        '''
        Inputs: other Vendor object, this vendor's item object, other vendor's item.
        Swaps item objects between this vendor and other vendor's inventories 
        '''  
        if my_item not in self.inventory or \
            their_item not in other.inventory:
            return False

        # remove() method returns item object 
        # which we can use as the argument for the add() method     
        self.add(other.remove(their_item))
        other.add(self.remove(my_item))
        
        return True
    
    def swap_first_item(self, other):
        '''Input: other vendor object.
        Swaps the first items in current and other vendor's inventories'''
        if not self.inventory or not other.inventory:
            return False   
        return self.swap_items(other, self.inventory[0], other.inventory[0])

    def get_best_by_category(self, category):
        '''Input: category(string). 
        Returns an item object with the highest condition in that category'''    
        if not self.get_by_category(category):
            return None
        #sort based on attribute of interest 
        return max(self.get_by_category(category), key=attrgetter("condition"))
        
    def swap_best_by_category(self, other, my_priority, their_priority):
        '''Inputs: other vendor object, this object's priority category, 
        other object's priority category.
        Swaps priority item objects between this vendor and other vendor's inventories
        '''
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        
        return self.swap_items(other, my_best_item, their_best_item)

    def swap_by_newest(self, other):
        '''Input: other vendor object.
        Swaps the newest items in current and other vendor's inventories'''
        if not self.inventory or not other.inventory:
            return False

        my_newest = min(self.inventory, key=attrgetter("age"))
        their_newest = min(other.inventory, key=attrgetter("age"))
        return self.swap_items(other, my_newest, their_newest)