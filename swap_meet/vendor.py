class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory
        if self.inventory is None:
            self.inventory = []

    def add(self, item):
        '''adds item to inventory'''
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        '''removes item from inventory'''
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        '''returns list of items of a given category from inventory'''
        same_category_items = []
        for item in self.inventory:
            if item.category == category:
                same_category_items.append(item)
        return same_category_items

    def swap_items(self, vendor, my_item, their_item):
        '''swaps items between vendor inventories'''
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
            vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
    
    def swap_first_item(self, vendor):
        '''
        swaps items between vendor inventories 
        by first position in inventory
        '''
        if self.inventory and vendor.inventory:
            return self.swap_items(vendor, self.inventory[0], \
            vendor.inventory[0])
    
    def get_best_by_category(self, category):
        '''returns best condition item of a given category'''
        get_same_category = self.get_by_category(category)
        if not get_same_category:
            best_item = None
        else:
            best_item = get_same_category[0]
            for item in get_same_category:
                if item.condition > best_item.condition:
                    best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        swaps best condition items of a given category 
        between vendor inventories
        '''
        if not self.inventory or not other.inventory:
            return False
        elif not self.get_by_category(their_priority) or \
            not other.get_by_category(my_priority):
            return False
        else:
            self_best_item = self.get_best_by_category(their_priority)
            their_best_item = other.get_best_by_category(my_priority)
            self.swap_items(other, self_best_item, their_best_item)
            return True