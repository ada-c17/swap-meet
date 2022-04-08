class Vendor:

    def __init__(self, inventory = None):
        '''Vendor class is instantiated'''

        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        '''Function used to add items to vendor's inventory'''

        self.inventory.append(item)
        return item

    def remove(self, item):
        '''Function used to remove items from vendor's inventory'''

        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item

    def get_by_category(self, category):
        '''Function returns items in vendor's inventory if they belong to the category passed within the parameter'''

        items_in_category = []
        
        for item in self.inventory:
            if category == item.category:
                items_in_category.append(item)
        return items_in_category

    def swap_items(self, other, my_item, their_item):
        '''Function allows this vendor and another vendor to swap items from their respective inventories'''

        if my_item not in self.inventory or their_item not in other.inventory:
            return False
        else:
            self.remove(my_item)
            other.add(my_item)
            
            other.remove(their_item)
            self.add(their_item)
        return True

    def swap_first_item(self, other):
        '''Function allows this vendor and another vendor to swap the first item from their respective inventories'''

        if not self.inventory or not other.inventory:
            return False
        else:
            return self.swap_items(other, self.inventory[0], other.inventory[0])

    def get_best_by_category(self, category):
        '''Function identifies the item in the best condition within a certain category of a vendor's inventory'''

        current_condition = 0
        best_condition = None

        for item in self.inventory:
            if item.category == category:
                if item.condition > current_condition:
                    current_condition = item.condition
                    best_condition = item
        
        return best_condition

    def swap_best_by_category(self, other, my_priority, their_priority):
        '''Function swaps the items in the best condition with that of other vendors if in a certain category'''

        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False
        else:
            self.swap_items(other, my_best_item, their_best_item)
            return True

    def get_newest_by_category(self, category):
        '''Function identifies the newest item within a certain category of a vendor's inventory'''

        item_age_flag_max_30 = 30
        newest_item = None

        for item in self.inventory:
            if item.category == category:
                if item.age <= item_age_flag_max_30:
                    item_age_flag_max_30 = item.age
                    newest_item = item
        
        return newest_item

    def swap_newest_by_category(self, category, other):
        '''Function swaps the newest item with that of other vendors newest item if in a certain category'''

        my_newest_item = self.get_newest_by_category(category)

        their_newest_item = other.get_newest_by_category(category)

        if not my_newest_item or not their_newest_item:
            return False
        else:
            self.swap_items(other, my_newest_item, their_newest_item)
            return True