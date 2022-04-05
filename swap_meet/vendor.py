'''
Vendor class represents individuals trading at swap meet.
Includes the attribute 'inventory', which is a list of Item instances.
Includes numerous methods to work with and modify vendors' inventories.
'''


class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        '''Method to add one item to vendor's inventory and return item. Helper function to swap_items method.'''
        self.inventory.append(item)
        return item

    def remove(self, item):
        '''Method to remove one item from vendor's inventory. Helper function to swap_items method.'''
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_category(self, category):
        '''Method to return inventory list filtered to only items belonging to given category. Helper function to get_best_by_category method.'''
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, other, item_given, item_received):
        '''Method to swap two items between the vendor instance's inventory and another given vendor instance's inventory. Helper function to several other methods.'''
        if item_given not in self.inventory or item_received not in other.inventory:
            return False

        self.remove(item_given)
        self.add(item_received)
        other.remove(item_received)
        other.add(item_given)
        return True

    def swap_first_item(self, other):
        '''Method to trade the first item listed in vendor instance's inventory with the first item listed in another given vendor instance's inventory'''
        if not self.inventory or not other.inventory:
            return False
        return self.swap_items(other, self.inventory[0], other.inventory[0])

    def get_best_by_category(self, category):
        '''Method to return the highest rated item in an inventory belonging to a given category. Helper method to swap_best_by_category method.'''
        category_inventory = self.get_by_category(category)
        if len(category_inventory) < 1:
            return None
        best_item = category_inventory[0]
        for item in category_inventory:
            if item.condition > best_item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        '''Method to swap the highest-rated item belonging to a preferred category specific to each vendor instance, given a trade partner and category for each vendor'''
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if not my_best or not their_best:
            return False
        return self.swap_items(other, my_best, their_best)

    def get_newest(self):
        '''Method to return the item in an inventory with the lowest age attribute. Helper function to swap_by_newest function.'''
        newest = self.inventory[0]
        for item in self.inventory:
            if not item.age:
                return False
            if item.age < newest.age:
                newest = item
        return newest

    def swap_by_newest(self, other):
        '''Method to trade the newest item from each vendor instance's inventory given a trading partner.'''
        my_newest = self.get_newest()
        their_newest = other.get_newest()
        if not my_newest or not their_newest:
            return False
        return self.swap_items(other, my_newest, their_newest)
