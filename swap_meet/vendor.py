from .item import Item


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

    def get_by_category(self, category_name):
        res = []
        for item in self.inventory:
            if item.category == category_name:
                res.append(item)
        return res

    def swap_items(self, another_vendor, my_item, their_item):
        
        if my_item in self.inventory and their_item in another_vendor.inventory:
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            another_vendor.inventory.append(my_item)
            another_vendor.inventory.remove(their_item)
            return True
        return False

    def swap_first_item(self, another_vendor):
        
        if not self.inventory or not another_vendor.inventory:
            return False
        # my_item = self.inventory.pop(0)
        # their_item = another_vendor.pop(0)
        # self.inventory.append(their_item)
        # another_vendor.inventory.append(my_item)
        my_item = self.inventory[0]
        their_item = another_vendor.inventory[0]
        self.swap_items(another_vendor, my_item, their_item)
        return True

    def get_best_by_category(self, target_category):
        if not self.inventory:
            return None
        flag = False
        counter = -1
        for item in self.inventory:
            if item.category == target_category:
                flag = True
                if item.condition > counter:  # return the first item if there is a tie
                    res = item
                    counter=item.condition
        if not flag:
            return None
        return res

    def swap_best_by_category(self, other, my_priority, their_priority):
        
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        if not my_item or not their_item:
            return False
        self.swap_items(other, my_item, their_item)
        return True
