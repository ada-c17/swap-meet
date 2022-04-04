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
        return False
    
    def get_by_category(self, category):
        output = [Item for Item in self.inventory if category == Item.category]
        return output
        
    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            friend.add(my_item)
            friend.remove(their_item)
            self.remove(my_item)
            self.add(their_item)
            return True
        return False