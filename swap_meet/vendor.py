from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    # This method adds the item to the inventory
    def add(self, item):
        self.inventory.append(item)
        return item

    # This method removes the matching item from the inventory
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item

    # Takes one argument: a string, representing a category
    # Returns a list of Items in the inventory with that category
    def get_by_category(self, category):
        #self.item = Item(category)
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

