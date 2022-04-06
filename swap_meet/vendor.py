class Vendor:
    def __init__(self, inventory=None):
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

    def get_by_category(self, specific_category):
        category_matches = []
        for item in self.inventory:
            if item.category == specific_category:
                category_matches.append(item)
        return category_matches

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            friend.inventory.append(my_item)
            self.inventory.remove(my_item)
            
            self.inventory.append(their_item)
            friend.inventory.remove(their_item)
            return True
        return False
    
    def swap_first_item(self, friend):
        '''
        1) Adds the first item from Jolie's (friend's) inventory.
        2) Removes first item from Fatimah's (self's) inventory.
        3) Adds the instances first item
        4) Remove the first item from Jolie's inventory
        '''
        if self.inventory and friend.inventory:
            friend.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])

            self.inventory.append(friend.inventory[0])
            friend.inventory.remove(friend.inventory[0])
            return True
        return False