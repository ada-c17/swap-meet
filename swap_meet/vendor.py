from typing import ItemsView


class Vendor:
    def __init__(self, inventory=None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)
        return items_in_category
        
    def swap_items(self, friend, my_item, their_item):
        # if items are no in inventories, return False
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False

        # swap items
        self.remove(my_item)
        friend.add(my_item)
        friend.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, friend):
        # if either self or friend has nothing in inventory, return False
        if len(self.inventory) < 1 or len(friend.inventory) < 1:
            return False

        # store first items of self and friend's inventory into variables
        self_first_item = self.inventory[0]
        friend_first_item = friend.inventory[0]

        # use swap_items function to swap first items 
        self.swap_items(friend, self_first_item, friend_first_item)

        return True

    def get_best_by_category(self, category):
        # initiate two variables to store the highest condition and the item name
        highest_condition = 0
        item_best_condition = None

        # iterate through the items, check if the category matches, then check if the
        # item condition is highest. If so, reassign the two variables accordingly.
        for item in self.inventory:
            if item.category == category:
                if item.condition > highest_condition:
                    highest_condition = item.condition
                    item_best_condition = item
        return item_best_condition
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        # if either self or other does not have each other's prioirty, return False
        if self.get_best_by_category(their_priority) == None or other.get_best_by_category(my_priority)  == None:
            return False

        # store the best items for each other in two variables
        best_item_to_give = self.get_best_by_category(their_priority)
        best_item_to_receive = other.get_best_by_category(my_priority)

        # use the swap_items function to swap 
        self.swap_items(other, best_item_to_give, best_item_to_receive)
        return True


# optional_enhancements

    def get_newest_item(self):
        if len(self.inventory) == 0:
            return False
        newest_item = ''
        newest_age = float('inf')
        for item in self.inventory:
            if not item.age:
                raise ValueError
            elif item.age < newest_age:
                newest_item = item
                newest_age = item.age
        return newest_item

    def swap_by_newest(self, other):
        self_newest = self.get_newest_item()
        other_newest = other.get_newest_item()

        if not self_newest or not other_newest:
            return False

        self.swap_items(other, self_newest, other_newest)

        return True

