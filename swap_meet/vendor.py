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

    def get_by_category(self, category):
        items = [item for item in self.inventory if item.category == category]
        # Line 38 in integration tests wave 1/2/3 expects empty list if no category match
        return items

    def swap_items(self, second_person, user_item, second_item):
        if user_item in self.inventory and second_item in second_person.inventory:
            self.add(second_item)
            self.remove(user_item)
            second_person.add(user_item)
            second_person.remove(second_item)
            return True
        return False

    def swap_first_item(self, second_person):
        if len(self.inventory) > 0 and len(second_person.inventory) > 0:
            return self.swap_items(second_person, self.inventory[0], second_person.inventory[0])


    def get_best_by_category(self, best_cat):
        items_list = self.get_by_category(best_cat)
        # max goes through items_list, where each element is passed through the lambda func
        # lambda func returns the float value from condition attr.
        # based on that value, max finds the max and returns the element
        # How does it know to return the element and not x.condition value
        best_item = max(items_list, default=None, key=lambda x: x.condition)
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        return self.swap_items(other, my_item, their_item)


    # Implement a Vendor method named swap_by_newest
    # My logic:
    # swap whatever the newest item is in each inventory
    # doesn't matter category or what vendors "want"
    # both items must have an age
    # if one inventory list has no age attributes for any items, return False
    # return True if can swap
    # tie will go to first item in inventory
    # (tests in new file, unit tests-wave 7)
    def swap_by_newest(self, other):
        my_newest_item = None
        my_low_age = 1000
        for item in self.inventory:
            if item.age and item.age < my_low_age:
                my_low_age = item.age
                my_newest_item = item

        their_newest_item = None
        their_low_age = 1000
        for item in other.inventory:
            if item.age and item.age < their_low_age:
                their_low_age = item.age
                their_newest_item = item

        return self.swap_items(other, my_newest_item, their_newest_item)