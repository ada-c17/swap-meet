from curses import beep
from nis import cat
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

class Vendor:
    """Vendor has a relationship with Item class called composition."""
    

    # Wave 1
    def __init__(self, inventory = None):
        """Inventory is keyword argument that optionally pass in."""
        
        # assign empty list to inventory when the if statement is falsy. 
        # Otherwise, assign inventory as value of object's inventory.
        if not inventory:
            inventory = []
        self.inventory = inventory
        
        
    def add(self, item):
        """Adding new item into inventory and returns that item."""
        
        # make sure input is not empty before adding
        if item:
            self.inventory.append(item)
            return item
        

    def remove(self, item):
        """Removing item from inventory if it is matching requirement and returns that removed item."""
        
        # make sure input is not empty before removing
        if item and item in self.inventory:
            self.inventory.remove(item)
            return item
        return False


    # Wave 2
    def get_by_category(self, category):
        """
        - Adding item in a list if it matches category then return that list of item,
        - Otherwise, return []
        """
        
        items_list = []
        # adding item into the new list if the inventory is not empty and matches category
        if category and len(self.inventory) > 0:
            for item in self.inventory:
                if item.category == category:
                    items_list.append(item)
            return items_list
        return []


    # Wave 3
    def swap_items(self, other_vendor, my_item, their_item):
        """
        Swapping item based on the priority:
            - In my inventory, removing my_item and adding their_item
            - In other inventory, removing their_item and adding my_item
            - then return True if it been swapped, otherwise return False
        """
        
        # checking validation to make sure all inputs are not empty before swapping
        if len(self.inventory) > 0 and len(other_vendor.inventory) > 0:
            if my_item and my_item in self.inventory:
                if their_item and their_item in other_vendor.inventory:
                    self.inventory.remove(my_item)
                    self.inventory.append(their_item)
                    other_vendor.inventory.append(my_item)
                    other_vendor.inventory.remove(their_item)
                    return True
        return False
            

    # Wave 4
    def swap_first_item(self, other_vendor):
        """ 
        Swapping the first item of both inventory:
            - If the first item of both inventories been swapped then return True,
            - Otherwise, return False.
        """
        
        # checking validation to make sure both inventories are not empty before swapping
        if len(self.inventory) > 0 and len(other_vendor.inventory) > 0:
            self.inventory[0], other_vendor.inventory[0] = other_vendor.inventory[0], self.inventory[0]
            return True
        return False


    # Wave 6
    def get_best_by_category(self, category):
        """ 
        Findding best item by category:
            - If it is highest condition and matches category then return that item
            - Otherwise, return None
        """
        
        # validating the input and finding the highest condition that matches category for best item
        if category and len(self.inventory) > 0:
            for item in self.inventory:
                if (isinstance(item.condition, int) or isinstance(item.condition, float)) and item.category == category :
                    if item.condition == max(item.condition for item in self.inventory if item.category == category):
                        return item
        return None

    
    def swap_best_by_category(self, other, my_priority, their_priority ):
        """
        Swapping by best item:
            - invoke function get_best_by_category() to find best item
            - invoked function swap_items() then it return True if item been swapped, otherwise, return False.
        """
        
        # find my best item and other best item base on each priority.
        my_best_item = self.get_best_by_category(their_priority)
        other_best_item = other.get_best_by_category(my_priority)
        # return True or False
        return self.swap_items(other, my_best_item, other_best_item)
        

    # Optional Enhancements
    def get_newest_by_category(self, category):
        """ 
        Findding newest item by category:
            - If it is youngest age and matches category then return that item
            - Otherwise, return None
        """
        
        # validate input and find min age that matches category for newest item
        if category and len(self.inventory) > 0:
            for item in self.inventory:
                if item.category == category and isinstance(item.age, int):
                    if item.age == min(item.age for item in self.inventory if item.category == category):
                        return item
        return None


    def swap_newest_by_category(self, other, my_priority, their_priority):
        """
        Swapping by newest item:
            - invoke function get_newest_by_category() to find newest item
            - invoked function swap_items() then it return True if item been swapped, otherwise, return False.
        """
        
        # find my newest item and other newest item base on each priority.
        my_newest_item = self.get_newest_by_category(their_priority)
        other_newest_item = other.get_newest_by_category(my_priority)
        # return True or False
        return self.swap_items(other, my_newest_item, other_newest_item)
        

