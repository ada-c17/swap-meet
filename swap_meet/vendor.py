# from unicodedata import category
from swap_meet.item import Item

class Vendor:
    
    def __init__(self, inventory = None):
        self.inventory = inventory
        if self.inventory is None:
            self.inventory = []
    def add(self, item):
        """
        takes in one item
        adds item to inventory
        returns item that was added
        """
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False    

    def get_by_category(self, category_str):
        category_list = []
        for elem in self.inventory:
            if elem.category == category_str:
                category_list.append(elem)
        return category_list

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item \
            not in friend.inventory:
            return False
        self.inventory.remove(my_item)
        friend.inventory.append(my_item)
        friend.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True

    def swap_first_item(self, friend):
        if self.inventory == [] or friend.inventory == []:
            return False
        self_first_item = self.inventory.pop(0)
        friend_first_item = friend.inventory.pop(0)
        self.inventory.insert(0, friend_first_item)
        friend.inventory.insert(0, self_first_item)
        return True    

    def get_best_by_category(self, category_str):
        max_condition = 0
        item_with_max = None

        for elem in self.inventory:
            if elem.category == category_str:
                if elem.condition >= max_condition:
                    max_condition = elem.condition
                    item_with_max = elem

        return item_with_max           


    def swap_best_by_category(self, other, my_priority,\
        their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if my_best_item is None or their_best_item is None:
            return False
        return self.swap_items(other, my_best_item, their_best_item)