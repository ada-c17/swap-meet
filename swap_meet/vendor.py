class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, other, my_item, their_item):
        if my_item not in self.inventory or their_item not in other.inventory:
            return False
        else:
            self.add(other.remove(their_item))
            other.add(self.remove(my_item))
            return True
    
    def swap_first_item(self, other):
        if self.inventory and other.inventory:
            return self.swap_items(other, self.inventory[0], other.inventory[0])

    def get_best_by_category(self, category):
        cat_items = self.get_by_category(category)
        highest_rating = 0.0
        best_item = None
        for item in cat_items:
            if item.condition > highest_rating:
                highest_rating = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_item, their_item)

    def get_newest_item(self):
        newest_item = None
        smallest_age = None

        for item in self.inventory:
            if item.age and (not smallest_age or item.age < smallest_age):
                newest_item, smallest_age = item, item.age
        return newest_item

    def swap_by_newest(self, other):
        my_newest = self.get_newest_item()
        their_newest = other.get_newest_item()

        return self.swap_items(other, my_newest, their_newest)