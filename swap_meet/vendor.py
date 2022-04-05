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
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        self.remove(my_item)
        friend.add(my_item)
        friend.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, friend):
        if len(self.inventory) < 1 or len(friend.inventory) < 1:
            return False

        self_first_item = self.inventory[0]
        friend_first_item = friend.inventory[0]

        self.remove(self_first_item)
        friend.add(self_first_item)
        friend.remove(friend_first_item)
        self.add(friend_first_item)

        return True

    def get_best_by_category(self, category):
        highest_condition = 0
        item_best_condition = None
        for item in self.inventory:
            if item.category == category:
                if item.condition > highest_condition:
                    highest_condition = item.condition
                    item_best_condition = item
        return item_best_condition
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        if self.get_best_by_category(their_priority) == None or other.get_best_by_category(my_priority)  == None:
            return False
        best_item_to_give = self.get_best_by_category(their_priority)
        best_item_to_receive = other.get_best_by_category(my_priority)
        self.swap_items(other, best_item_to_give, best_item_to_receive)
        return True


