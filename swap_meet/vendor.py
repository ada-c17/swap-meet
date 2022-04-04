class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        result = [item for item in self.inventory if item.category is category]
        return result

    def swap_items(self, vendor, my_item, their_item):
        if (my_item in self.inventory and
                their_item in vendor.inventory):
            self.remove(my_item)
            self.add(their_item)
            vendor.remove(their_item)
            vendor.add(my_item)
        else:
            return False
        return True
    
    def swap_first_item(self, vendor):
        if not (self.inventory or vendor.inventory):
            return False
        else:
            my_first = self.inventory.pop(0)
            their_first = vendor.inventory.pop(0)
            self.add(their_first)
            vendor.add(my_first)
        return True
        
