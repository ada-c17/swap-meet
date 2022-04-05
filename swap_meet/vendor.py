class Vendor:

    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        # Use try-clause to check if the matching item can be removed from the inventory list
        try:
            self.inventory.remove(item)
            return item
        # Use except-clause to catch raised exception if there is no matching item in the inventory list 
        except ValueError as err:
            return False

    def get_by_category(self, category):
        # Create items list to store the item in inventory with that category
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items 

    def swap_items(self, friend, my_item, their_item):
        # Use try_clause to access the index of my_item from Vendor's inventory and the index of their_item from friend's inventory
        # Swap the value of those indexes 
        try:
            index1 = self.inventory.index(my_item)
            index2 = friend.inventory.index(their_item) 

            self.inventory[index1] = their_item
            friend.inventory[index2] = my_item
            return True

        # Use except_clause to handle exception if the Vendor's inventory does not contain my_item or the friend's inventory does not contain their item
        except ValueError as err:
            return False

    def swap_first_item(self, friend):
        # If the length of both lists are greater or equal one:
        # Swap the first item in Vendor's inventory and friend's inventory lists
        if len(self.inventory) >= 1 and len(friend.inventory) >= 1:
            temp = self.inventory[0]
            self.inventory[0] = friend.inventory[0]
            friend.inventory[0] = temp
            return True
        # Return False if either Vendor or Friend has an empty inventory list
        else:
            return False
    
    def get_best_by_category(self, category):
        max_condition = 0
        max_value = None
        for item in self.inventory:
            if item.category == category and item.condition > max_condition:
                max_condition = item.condition 
                max_value = item
        return max_value 

    def swap_best_by_category(self, other, my_priority, their_priority):

        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False

        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)

        return self.swap_items(other,my_best,their_best)