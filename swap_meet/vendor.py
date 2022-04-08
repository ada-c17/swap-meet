class Vendor:
    def __init__(self, inventory= None):
        if not inventory:
            inventory = []
        self.inventory = inventory


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
        list_items = []
        for item in self.inventory:
            if item.category == category:
                list_items.append(item)
        return list_items


    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        other_index = vendor.inventory.index(their_item)
        self_index = self.inventory.index(my_item)
        temp_item = my_item
        self.inventory[self_index] = their_item
        vendor.inventory[other_index] = temp_item
        return True


    def swap_first_item(self, vendor):
        if self.inventory and vendor.inventory:
            return self.swap_items(vendor, self.inventory[0], vendor.inventory[0])


    def get_best_by_category(self, category):
        condition = 0
        item_to_return = None
        for item in self.inventory:
            if item.category == category:
                if condition < item.condition:
                    condition = item.condition
                    item_to_return = item
        return item_to_return


    def swap_best_by_category(self, other, my_priority, their_priority):
        vendor_best_item = self.get_best_by_category(their_priority)
        other_best_item = other.get_best_by_category(my_priority)
        return self.swap_items(other, vendor_best_item, other_best_item)


    def swap_by_newest(self, other, category):
        '''The function takes another vendor as "other" 
        and a category of items we'd like to exchange as parameters.
        First, it makes a list of all items in this category,
        then picks up the newest item in each of the lists and swaps them.
        Returns True if the swap was made.
        '''
        my_category_list = self.get_by_category(category)
        other_category_list = other.get_by_category(category)
        my_newest_item = min(my_category_list, key=lambda x: x.age)
        other_newest_item = min(other_category_list, key=lambda x: x.age)
        return self.swap_items(other, my_newest_item, other_newest_item)