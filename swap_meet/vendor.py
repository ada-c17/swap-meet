class Vendor:

    def __init__(self, inventory=[]):
        self.inventory = inventory


    def add(self, item):

        self.inventory.append(item)
        return item


    def remove(self, item):
        item_index = self.get_item_index(item)

        if item_index == -1:
            return False

        del self.inventory[item_index]

        return item


    def get_item_index(self, item):
        try:
            return self.inventory.index(item)
        except ValueError:
            return -1


    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]


    def swap_items(self, other, my_item, their_item):

        if my_item not in self.inventory or their_item not in other.inventory:
            return False

        self.add(their_item)
        self.remove(my_item)
        other.add(my_item)
        other.remove(their_item)
        return True


    def swap_first_item(self, other):

        if not self.inventory or not other.inventory:
            return False

        self.inventory[0], other.inventory[0] = other.inventory[0], self.inventory[0]
        return True


    def get_best_by_category(self, category):

        best_item = None

        items_in_category = self.get_by_category(category)

        if items_in_category:
            for item in items_in_category:
                if best_item is None or item.condition > best_item.condition:
                    best_item = item
        
        return best_item