class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory
        if inventory is None:
            self.inventory = []

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, item_to_remove):
        if item_to_remove in self.inventory:
            self.inventory.remove(item_to_remove)
            return item_to_remove
        else:
            return False

    def get_by_category(self, category):
        ''' input: string, representing a category. Output: list of Items in the inventory w/that category'''
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    
    # best_item = tai.get_best_by_category("Clothing")
    def get_best_by_category(self, category):
        items = self.get_by_category(category)

        if items == []:
            return None
        else:
            best_item = items[0]
            for item in items:
                if item.condition > best_item.condition:
                    best_item = item
            return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        their_category_item = self.get_best_by_category(their_priority)
        my_priority_item = other.get_best_by_category(my_priority)

        if not their_category_item or not my_priority_item:
            return None
        else:
            self.add(my_priority_item)
            self.remove(their_category_item)
            other.add(their_category_item)
            other.remove(my_priority_item)
            return True

    #  result = fatimah.swap_items(jolie, item_b, item_d)
    # passing in instance of Vendor, instance of Item, instance of Item
    def swap_items(self, vendor_friend, my_item, their_item):
        '''
        input: 3 parameters: One instance of vendor class (a friend), two instances of item classes.
            The items will be swapped: first item will be added to current vendor, second item will be added to 2nd vendor
            ouptut: True or False (False if items that should be swapped are not within their vendor's inventory)
        '''
        if my_item in self.inventory and their_item in vendor_friend.inventory:
            vendor_friend.add(my_item)
            self.remove(my_item)
            self.add(their_item)
            vendor_friend.remove(their_item)
            return True
        else: 
            return False

# result = fatimah.swap_first_item(jolie)
    def swap_first_item(self, vendor_friend):
        if self.inventory == [] or vendor_friend.inventory == []: 
            return False
        else: 
            my_first_item = self.inventory[0]
            their_first_item = vendor_friend.inventory[0]
            self.add(their_first_item)
            vendor_friend.add(my_first_item)
            self.remove(my_first_item)
            vendor_friend.remove(their_first_item)
            return True
