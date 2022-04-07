class Vendor:

    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self,item):
        '''Add an item to the inventory.'''
        self.inventory.append(item)
        return item

    def remove(self, item):
        '''Remove an item from the inventory. If item doesn't exist then function will return False.'''
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        '''Will return item(s) from your inventory that match the category given.'''
        category_match = []
        for item in self.inventory:
            if item.category == category:
                category_match.append(item)
        return category_match

    def swap_items(self, Vendor, my_item, their_item):
        '''Swap items between you and another vendor's inventory.'''
        if my_item not in self.inventory  or their_item not in Vendor.inventory:
            return False
        self.add(their_item)
        Vendor.add(my_item)
        self.remove(my_item)
        Vendor.remove(their_item)
        return True

    def swap_first_item(self, Vendor):
        '''Swap the first items between you and another vendor's inventory.'''
        if not self.inventory or not Vendor.inventory:
            return False
        self.swap_items(Vendor, self.inventory[0], Vendor.inventory[0])
        return True

    def get_best_by_category(self, category=""):
        '''Returns item with the best condition which matches the category.'''
        condition = 0
        best_condition = None
        for item in self.inventory:
            if item.category == category:
                if item.condition > condition:
                    condition = item.condition
                    best_condition = item
        return best_condition

    def swap_best_by_category(self, other, my_priority, their_priority):
        '''Swaps items with best conditions if item matches desired category.'''
        other_best = other.get_best_by_category(my_priority)
        my_best = self.get_best_by_category(their_priority)
        if not other_best or not my_best:
            return False
        self.swap_items(other, my_best, other_best)
        return True

    def get_newest(self, age=None):
        '''Returns item with the lowest age'''
        if not self.inventory:
            return None
        newest = self.inventory[0]
        age = (self.inventory[0]).age
        for item in self.inventory:
            if age > item.age:
                age = item.age
                newest = item
        return newest

    def swap_by_newest(self, Vendor):
        '''Swaps newest items between you and another vendor's inventory.'''
        my_newest = self.get_newest()
        their_newest = Vendor.get_newest()
        if not my_newest or not their_newest:
            return False
        self.swap_items(Vendor, my_newest, their_newest)
        return True
