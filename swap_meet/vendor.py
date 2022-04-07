class Vendor:
    '''Creates a Vendor class with an inventory attribute. Inventory is an empty list by default or 
    you can optionally pass in a list with the keyword inventory'''
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        '''Adds an item to a vendor's inventory'''
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        '''Removes an item from a vendor's inventory'''
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        "Returns a list of items of a category in a vendor's inventory"
        item_list = [item for item in self.inventory if item.category == category]
        return item_list

    def swap_items(self, vendor, my_item, their_item):
        '''Swaps items (my_item and their_item) between two vendor inventories (self and vendor)'''
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        self.inventory.remove(my_item)
        self.inventory.append(their_item)
        vendor.inventory.remove(their_item)
        vendor.inventory.append(my_item)
        return True

    def swap_first_item(self, vendor):
        '''Swaps the first item in two vendor inventories (self and vendor)'''
        if self.inventory and vendor.inventory:
            return self.swap_items(vendor, self.inventory[0], vendor.inventory[0])

    def get_best_by_category(self, category):
        items_list = self.get_by_category(category)
        if not items_list:
            return None
        best_item = items_list[0]
        for item in items_list:
            if item.condition > best_item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        if not my_item or not their_item:
            return False
        self.swap_items(other, my_item, their_item)
        return True

    def get_newest_by_category(self, category):
        pass

