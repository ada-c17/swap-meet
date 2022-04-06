
from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory
        self.greeting = "Hi"
    
    def add(self, item):
        self.inventory.append(item)

        # print(f"This is the updated inventory: {updated_list}")
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)

        return item

    def get_by_category(self, category):
        if not category:
            return False

        category_list = []
        for item in self.inventory:
            if item.category == category:

                category_list.append(item)
            
        return category_list


    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False

        self.inventory.remove(my_item)
        friend.inventory.append(my_item)
        friend.inventory.remove(their_item)
        self.inventory.append(their_item)

        return True
        
    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False

        # elif self.inventory[0] not in friend.inventory:
        friend.inventory.append(self.inventory[0])
        self.inventory.remove(self.inventory[0])            

        # if friend.inventory[0] not in self.inventory:
        self.inventory.append(friend.inventory[0])
        friend.inventory.remove(friend.inventory[0])

        return True


    def get_best_by_category(self, category):
        """Get the item with the best condition in a certain category.
        It takes one argument: a string that represents a category"""

        # for item in self.inventory:
            # Need dictionary with key value pairs of item, condition, and category.
            # Iterate over this dictionary and return just the item (with the max condition for each category).
            # Perhaps create a new data structure with category and highest value item for that category.

            #Need guard clause for no items in inventory that match category and returns None 
            # If there are duplicate items (smae item and condition) return just one of them 
            #Figure out what else you can glean from the tests. 
            # best_item = max(Item.condition)  #where is condition located?

        category_list = self.get_by_category(category) 
        best_condition = 0
        best_item = None    
        
        for item in category_list:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item

        return best_item

    # my_priority = ??
    # their_priority = ??

    # # can I put item and condition in a dictionary that I can reference?


    def swap_best_by_category(self, other, my_priority, their_priority):
        friend_swap = other.get_best_by_category(my_priority)
        my_swap = self.get_best_by_category(their_priority)
    
        if not my_swap or not friend_swap:
            return False

        self.swap_items(other, my_swap, friend_swap)
        return True

    



            
            
    

