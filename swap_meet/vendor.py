class Vendor:   
    def __init__(self, inventory=[]):
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
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        if items == []:
            return False
        return items

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            friend.inventory.remove(their_item)
            friend.inventory.append(my_item)
            return True

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False
        else:
            self.inventory.insert(1, friend.inventory[0])
            friend.inventory.insert(1, self.inventory[0])
            self.inventory.pop(0)
            friend.inventory.pop(0)
            return True
        