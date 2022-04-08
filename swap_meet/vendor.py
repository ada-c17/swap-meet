from swap_meet.item import Item

class Vendor:

    
    def __init__(self, inventory = None):
        """
        def __init__ creates attribute of empty inventory to hold items
        """
        if inventory == None:
            inventory = []
        self.inventory = inventory

    
    def add(self, item):
        """
        def add() adds items to inventory and returns the item that was added 
        """
        self.inventory.append(item)
        return item

    
    def remove(self, item):
        """
        def remove() removes  matching item from inventory \
        and returns the item that was removed
        """
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    
    
    def get_by_category(self, input_category):
        """
        def get_by_category() takes in a category string \
        and returns a list of items in the inventory with that category
        """
        item_list = []
        for item in self.inventory:
            if item.category == input_category:
                item_list.append(item)
        return item_list

    
    def swap_items(self, other_vendor, my_item, their_item):
        """
        def swap_items() returns false if self doesn't contain my_item \
        or other_vendor doesn't contain their_item\
        It swaps my_item from self with their_item from other_vendor \
        and returns trues
        """
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.add(their_item)
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        return True

    
    def swap_first_item(self, other_vendor):
        """
        def swap_first_item() returns false if self or other_vendor have an empty list\
        It swaps first item from self and other_vendor and swaps those items\
        and returns true
        """
        if len(self.inventory) ==0 or len(other_vendor.inventory) ==0:
            return False
        my_first_item = self.inventory[0]
        friend_first_item = other_vendor.inventory[0]
        return self.swap_items(other_vendor, my_first_item, friend_first_item)
    
    def get_best_by_category(self, category):
        """
        def get_best_by_category() returns false if self or other_vendor have an empty list\
        It swaps first item from self and other_vendor and swaps those items\
        and returns true
        """
        cat_item_list = self.get_by_category(category)
        best_condition = 0
        best_item = None
        for item in cat_item_list:
            item_condition = item.condition
            if best_condition < item_condition:
                best_condition = item_condition
                best_item = item
        return best_item 

       
    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        def swap_best_by_category() uses get_best_by_category to return a list of items in matching priority category\
        if items don't match priority returns false\
        otherwise swaps items and returns true
        """ 
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)

        if my_best == None or their_best == None:
            return False
        self.swap_items(other, my_best, their_best)
        return True