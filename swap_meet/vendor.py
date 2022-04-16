from .item import Item
class Vendor:
    """
    A class to represent a vendor.
    
    ...
    Attributes:

    inventory: list
        a list of item class or item child class objects, defaults to None which results in an empty list
    
    ...
    Methods:

    add(new_item):
        Adds provided item to instance inventory and returns the item. 

    remove(discarded_item):
        Removes provided item from instance inventory and returns the item.
        - Returns False if item not already in inventory.

    get_by_category(category_string):
        Returns list of items of provided category from instance inventory.

    swap_items(other, my_item, their_item):
        Swaps provided items between two instances' inventories and returns True.
        - Returns False if either item not found.

    swap_first_item(other):
        Swaps first items of two instances' inventories and returns True.
        - Returns false if either inventory is empty.

    get_best_by_category(desired_category):
        Returns item of provided category with best condition from an instance's inventory. 
        - Returns None if no items of provided category in inventory.

    swap_best_by_category(other, my_priority, their_priority):
        Swaps best items in provided categories between two instances' inventories and returns True.
        - Returns False if either item not found. 

    get_newest_item():
        Returns newest item from instance's inventory items with known ages.
        - Returns None if all items ages are unknown.

    swap_by_newest(other):
        Swaps newest items of two instances' inventories and returns True.
        - Returns False if either or both inventory items' ages are all unknown.
    
    """

    def __init__(self, inventory = None):
        ### OG code
        # if inventory is None:
        #     inventory = []
        # self.inventory = inventory
        #### Refactored code:
        # if inventory parameter is anything but None, assign to self.inventory, else (ie if None) assign empty list
        # retains ability to pass in empty list for inventory and not rewrite it 
        self.inventory = inventory if inventory is not None else []
    
    def add(self, new_item):
        """Add provided item to inventory"""

        self.inventory.append(new_item)
        return new_item
    
    def remove(self, discarded_item):
        """Remove an item from inventory"""

        if discarded_item not in self.inventory:
            return False
        ### Refactoring - remove else statements if else contains main logic of function
        self.inventory.remove(discarded_item)
        return discarded_item
    
    def get_by_category(self, category_string):
        """Return list of items from inventory of a certain category"""

        ### OG code
        item_list = []
        # for item in self.inventory:
        #     if item.category == category_string:
        #         item_list.append(item)
        ### Refactored to list comprehenstion
        # [ return element for element in source_list if some_condition(element)]
        item_list = [item for item in self.inventory if item.category == category_string]
        return item_list
    
    def swap_items(self, other, my_item, their_item):
        """Swaps items betwen self and another vendor's inventory"""

        # check valid input
        if my_item not in self.inventory or their_item not in other.inventory:
            return False
        ### removed unnecessary else statement here
        # remove items from original inventory
        self.remove(my_item)
        other.remove(their_item)
        # add items to new inventory 
        self.add(their_item)
        other.add(my_item)
        return True
    
    def swap_first_item(self, other):
        """Swaps first item in self and another vendor's inventory"""

        # check valid input
        if not self.inventory or not other.inventory:
            return False
        ### removed unnecessary else statement here
        my_first_item = self.inventory[0]
        vendor_first_item = other.inventory[0]
        self.swap_items(other, my_first_item, vendor_first_item)
        return True
    
    def get_best_by_category(self, desired_category):
        """Returns item in best condition within a certain category"""

        # get list of items of category
        potential_items = self.get_by_category(desired_category)
        # account for no items of desired category or only one of desired category
        if not potential_items:
            return None
        elif len(potential_items) == 1:
            return potential_items[0]
        # calculate max item condition
        else:
            best_item = max(potential_items, key = lambda item: item.condition)
            return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        """Swap best items in provided categories between self and another vendor"""

        # get best items in each category
        their_desired_item = self.get_best_by_category(their_priority)
        my_desired_item = other.get_best_by_category(my_priority)

        # check validity
        if not my_desired_item or not their_desired_item:
            return False
        ### removed unnecessary else statement here
        # swap items if valid
        return self.swap_items(other, their_desired_item, my_desired_item)
        
    def get_newest_item(self):
        """Returns newest item from inventory items with known ages"""

        ### OG Code:
        # potential_items = []
        # for item in self.inventory:
        #     if item.age:
        #         potential_items.append(item)
        ### Refactored to list comprehension
        potential_items = [item for item in self.inventory if item.age]

        if not potential_items:
            return None
        elif len(potential_items) == 1:
            return potential_items[0]
        else:
            newest_item = min(potential_items, key = lambda item: item.age)
            return newest_item 
    
    def swap_by_newest(self, other):
        """Swaps newest items of self and another vendor"""

        their_newest = other.get_newest_item()
        my_newest = self.get_newest_item()

        if not my_newest or not their_newest:
            return False
        ### removed unnecessary else statement here
        return self.swap_items(other, my_newest, their_newest)
