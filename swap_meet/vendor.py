class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, add_item):
        add = self.inventory.append(add_item)
        return add_item

    def remove(self, sub_item):
        if sub_item in self.inventory:
            self.inventory.remove(sub_item)
            return sub_item
        else:
            return False
    

        
        


