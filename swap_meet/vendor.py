from operator import attrgetter

class Vendor:

    def __init__(self, inventory = None):
        if inventory == None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        # Use a try statement to check if the matching item can be removed from the inventory list
        try:
            self.inventory.remove(item)
            return item
        # Use except-clause to catch raised exception if there is no matching item in the inventory list 
        except ValueError as err:
            return False

    def get_by_category(self, category):
        # Create items list to store the item with matching category 
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items 

    def swap_items(self, friend, my_item, their_item):
        # Check if self.inventory contains my_item and friend.inventory contains their_item
        # Access the index of my_item and their_item in the inventory list 
        # Swap the value of my_index and their_index (so that the time complexity is constant O(1))
        if my_item in self.inventory and their_item in friend.inventory:
            my_index = self.inventory.index(my_item)
            their_index = friend.inventory.index(their_item) 
            
            self.inventory[my_index] = their_item
            friend.inventory[their_index] = my_item
            return True

    def swap_first_item(self, friend):

        # Calling helper function swap_first_item if either Vendor or Friend inventory list isn't empty
        if self.inventory and friend.inventory: 
            result = self.swap_items(friend,self.inventory[0],friend.inventory[0])
            return True
    
    def get_best_by_category(self, category):
        # Initialize max_condition and max_value variables to capture the item with the highest condition and matching category
        max_condition = 0
        max_value = None

        for item in self.inventory:
        # If the item matches the category and the item condition is greater than current max condition
        # We will update the value of max condition and max_value
            if item.category == category and item.condition > max_condition:
                max_condition = item.condition 
                max_value = item
        return max_value 

    def swap_best_by_category(self, other, my_priority, their_priority):
        # Call helper function get_best_by_category to return the best item avaiable that matches my_priority or their_priority category
        # Call helper function swap_items to swap my_best and their_best items
        if self.inventory and other.inventory:
            my_best = self.get_best_by_category(their_priority)
            their_best = other.get_best_by_category(my_priority)

            return self.swap_items(other,my_best,their_best)
    
    def swap_by_newest(self, other):

        # Find the newest item in vendor's inventory list and other's inventory list
        my_newest_item = min(self.inventory, key = attrgetter("age"))
        their_newest_item = min(other.inventory, key = attrgetter("age"))
        
        # Call helper function swap_items to my_newest item and their_newest_item
        return self.swap_items(other,my_newest_item,their_newest_item)
            




