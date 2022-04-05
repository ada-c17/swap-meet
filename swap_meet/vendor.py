from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    # Adds the item to the inventory
    def add(self, item):
        self.inventory.append(item)
        return item

    # Removes the matching item from the inventory
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

    def swap_items(self, vendor, my_item, their_item):
  
        if (my_item not in self.inventory) or (their_item not in vendor.inventory):
            return False
        
        vendor.add(my_item)
        self.remove(my_item)

        self.add(their_item)
        vendor.remove(their_item)

        return True




