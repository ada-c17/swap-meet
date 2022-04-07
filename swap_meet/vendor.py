class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        if type(item) == list:
            for object in item:
                self.inventory.append(object)
        else:
            self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        elif item not in self.inventory:
            return False

    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.inventory.remove(my_item)
        other_vendor.remove(their_item)
        self.inventory.append(their_item)
        other_vendor.inventory.append(my_item)
        return True

    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        else:
            results = self.swap_items(
                other_vendor, self.inventory[0], other_vendor.inventory[0])
        return results

        # if self.inventory == [] or other_vendor.inventory == []:
        #     return False
        # else:
        #     item = self.inventory.pop(0)
        #     other_item = other_vendor.inventory.pop(0)
        #     self.inventory.append(other_item)
        #     other_vendor.inventory.append(item)
        #     return True

    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)
        max_condition = 0
        best_item = None

        for item in category_list:
            if item.condition > max_condition:
                best_item = item
                max_condition = item.condition
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):

        my_best = self.get_best_by_category(
            their_priority)
        others_best = other.get_best_by_category(
            my_priority)

        if my_best == None or others_best == None:
            return False

        else:
            swap_items = self.swap_items(other, my_best, others_best)
            return True
