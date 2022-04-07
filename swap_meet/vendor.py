class Vendor:
    
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def swap_items(self, second_person, user_item, second_item):
        if user_item in self.inventory and second_item in second_person.inventory:
            # Add and remove from 'my' inventory
            self.add(second_item)
            self.remove(user_item)

            # Add and remove from second vendor's inventory
            second_person.add(user_item)
            second_person.remove(second_item)
            return True
        return False

    def swap_first_item(self, second_person):
        if len(self.inventory) > 0 and len(second_person.inventory) > 0:
            # return True/False by calling swap_items method
            return self.swap_items(second_person, self.inventory[0], second_person.inventory[0])
    
    def get_by_category(self, category):
        items = [item for item in self.inventory if item.category == category]
        # Line 38 in integration tests wave 1/2/3 expects empty list if no category match
        return items

    def get_best_by_category(self, best_cat):
        items_list = self.get_by_category(best_cat)
        # max looks at item's self.condition value bc key points to lambda func
        best_item = max(items_list, default=None, key=lambda x: x.condition)
        # Return a single Item object, or None if items_list is empty
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        # Get Item objects based on category and condition (None if no match)
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        # return True/False by calling swap_items method
        return self.swap_items(other, my_item, their_item)

    # (tests in new file, unit tests-wave 7)
    def get_by_newest(self):
        """ Return newest item in vendor's inventory, or return None 
            If two items have the same lowest age, use the first one
        """
        low_age = 1000 # assuming no item will likely be greater than 1000 yrs old
        newest_item = None
        for item in self.inventory:
            if item.age and item.age < low_age:
                low_age = item.age
                newest_item = item
        return newest_item

    def swap_by_newest(self, other):
        """ 
        Swap newest item in each vendor's inventory

        Parameters:
        other: instance of Vendor object

        Returns:
        boolean: True if vendors can swap items, False if not
        """
        my_newest = self.get_by_newest()
        their_newest = other.get_by_newest()
        # return True/False by calling swap_items method
        return self.swap_items(other, my_newest, their_newest)