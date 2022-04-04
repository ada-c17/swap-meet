class Vendor:
    def __init__(self, inventory =[]):
        self.inventory = inventory 

    def add(self, item_added):
        new_item = self.inventory.append(item_added)
        return item_added

    def remove(self, item_removed):
        if item_removed in self.inventory:
            self.inventory.remove(item_removed)
            return item_removed
        else:
            return False
        


