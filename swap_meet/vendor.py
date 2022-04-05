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
        # Wave 1 directions
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
            self.swap_items(second_person, self.inventory[0], second_person.inventory[0])
            return True
        return False

    def get_best_by_category(self, best_cat):
        cat_list = self.get_by_category(best_cat)
        # max goes through cat_list, where each element is passed through the lambda func
        # lambda func returns the float value from condition attr.
        # based on that value, max finds the max and returns the element
        # How does it know to return the element and not x.condition value
        best_item = max(cat_list, default=None, key=lambda x: x.condition)
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        # if my_item and their_item:
        #     self.swap_items(other, my_item, their_item)
        #     return True
        # return False
        return self.swap_items(other, my_item, their_item)
