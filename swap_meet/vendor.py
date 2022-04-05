class Vendor:
    def __init__(self,inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self,item):
        self.inventory.append(item)
        return item


    def remove(self,item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
    

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    
    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.add(their_item)
            friend.add(my_item)
            self.remove(my_item)
            friend.remove(their_item)
            return True
        return False

    