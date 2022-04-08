def check_if_empty(lst):
    if len(lst) == 0:
        return False
    return True


class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return False
        return item

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, person, item_to_person, item_to_self):
        '''
        This method removes items from Vendor inventory and appends it to
        person's inventory.  If this is successful, then the method returns
        True.  Else, False.
        '''
        if (item_to_person not in self.inventory) or (item_to_self not in person.inventory):
            return False

        self.inventory.remove(item_to_person)
        person.inventory.append(item_to_person)

        person.inventory.remove(item_to_self)
        self.inventory.append(item_to_self)
        return True

    def swap_first_item(self, person):
        if check_if_empty(self.inventory) and check_if_empty(person.inventory):
            self.swap_items(person, self.inventory[0], person.inventory[0])
            return True
        else:
            return False

    def get_best_by_category(self, category):
        list_by_cat = self.get_by_category(category)

        if list_by_cat == []:
            return None

        list_by_cat.sort(key=lambda item:item.condition, reverse=True)
        return list_by_cat[0]

    def swap_best_by_category(self, other, my_priority, their_priority):
        item_to_self = other.get_best_by_category(my_priority)
        item_to_other = self.get_best_by_category(their_priority)

        if not (item_to_self and item_to_other):
            return False

        self.swap_items(other, item_to_other, item_to_self)
        return True
