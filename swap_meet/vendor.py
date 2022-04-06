class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item_to_add):
        self.inventory.append(item_to_add)
        return item_to_add
    
    def remove(self, item_to_remove):
        if item_to_remove not in self.inventory:
            return False

        self.inventory.remove(item_to_remove)
        return item_to_remove

    def get_by_category(self, category):
        items_in_category = []
        
        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)
        
        return items_in_category
    
    def swap_items(self, friend, my_item, their_item):
        # check that each vendor has item to swap
        if not my_item in self.inventory or not their_item in friend.inventory:
            return False
        
        # swap items in each vendor's inventory
        self.add(their_item)
        friend.remove(their_item)

        friend.add(my_item)
        self.remove(my_item)

        return True