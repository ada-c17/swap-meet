from types import NoneType


class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

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
        self.category = category
        item_list = []
        for cat in self.inventory:
            if cat.category == self.category:
                item_list.append(cat)

        return item_list

    def get_best_by_category(self, category):
        self.category = category
        best_condition = 0.0
        best_item = ""
        cat_found = False

        for cat in self.inventory:
            if cat.category == self.category and cat.condition >= best_condition:
                cat_found = True
                best_condition = cat.condition
                best_item = cat

        if cat_found:
            return best_item
        else:
            return None

    def swap_items(self, vendor2, my_item, their_item):
        self.vendor2 = vendor2
        self.my_item = my_item
        self.their_item = their_item

        if self.my_item not in self.inventory or self.their_item not in vendor2.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            vendor2.inventory.append(my_item)
            vendor2.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True

    def swap_first_item(self, friend):
        if not len(self.inventory) >= 1 or not len(friend.inventory) >= 1:
            return False
        else:
            my_item = self.inventory[0]
            their_item = friend.inventory[0]

            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            friend.inventory.remove(their_item)
            friend.inventory.append(my_item)

            return True

    def swap_best_by_category(self, other, my_priority, their_priority):
        their_item = other.get_best_by_category(my_priority)
        my_item = self.get_best_by_category(their_priority)

        if not my_item or not their_item:
            return False
        else:
            self.swap_items(other, my_item, their_item)
            return True