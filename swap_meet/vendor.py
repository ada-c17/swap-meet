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
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
        # if items:
        #     return items
        # else:
        #     return False

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
            second_person.add(self.inventory.pop(0))
            self.add(second_person.inventory.pop(0))
            return True
        return False

    def get_best_by_category(self, best_cat):
        highest_rating = 0
        best_item = None
        for item in self.inventory:
            if item.category == best_cat and item.condition > highest_rating:
                highest_rating = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        if self.get_by_category(their_priority) and other.get_by_category(my_priority):
            my_item = self.get_best_by_category(their_priority)
            their_item = other.get_best_by_category(my_priority)
            self.swap_items(other, my_item, their_item)
            return True
        return False
