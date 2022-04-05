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
