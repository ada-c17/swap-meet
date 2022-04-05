# from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
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
        category_items =[]
        for item in self.inventory:
            if category == item.category:
                category_items.append(item)
        return category_items
        
    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        self.remove(my_item)
        friend.add(my_item)
        friend.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, friend):
        if self.inventory == [] or friend.inventory == []:
            return False
        self.swap_items(friend, self.inventory[0], friend.inventory[0])
        return True
