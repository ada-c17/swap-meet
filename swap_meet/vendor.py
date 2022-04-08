class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self,item):
        """
        Adding item to user's inventory
        """
        self.inventory.append(item)
        return item

    def remove(self,item):
        """
        Removing item to user's inventory
        """
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item


    def get_by_category(self, category):
        """
        Return list of items that matches specific category
        """
        item_list = [item for item in self.inventory if item.category == category]
        return item_list

    def swap_items(self, friend_vendor, my_item, friend_item):
        """
        Takes parameters friend's inventory, my item, and friends item
        Method returns T/F based on if the items are in the appropriate inventory
        If items are in appripriate invetory, swap the items between user and friend
        """
        if my_item not in self.inventory or friend_item \
            not in friend_vendor.inventory:
            return False
        self.inventory.remove(my_item)
        self.inventory.append(friend_item)
        friend_vendor.inventory.remove(friend_item)
        friend_vendor.inventory.append(my_item)
        return True
    
    def swap_first_item(self, friend_vendor):
        """
        Takes parameter friend's inventory
        Method returns T/F based on if the inventories are empty or not
        If there are items in inventory, swap the FIRSTitems between user and friend
        """

        if not self.inventory or not friend_vendor.inventory:
            return False 
        self.inventory.append(friend_vendor.inventory[0])
        friend_vendor.inventory.append(self.inventory[0])
        self.inventory.pop(0)
        friend_vendor.inventory.pop(0)
        return True
    
    def get_best_by_category(self, category):
        """
        Takes parameter category
        Method returns the item that has the highest condition rating in that category
        """
        max_condition = 0
        max_item = None
        for item in self.inventory:
            if item.category == category and item.condition >= max_condition:
                max_item = item 
                max_condition = item.condition
        return max_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Takes parameters friend's inventory, my priority category, and their priority cateogry
        Method returns T/F based on if the inventories/categories are empty or not
        If there are valid items within the desired category for both parties,
        swap the items between user and friend
        """
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False
        self.swap_items(other, my_best_item, their_best_item)
        return True



