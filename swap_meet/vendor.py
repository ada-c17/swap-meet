class Vendor:
    def __init__(self, inventory=None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

        # refactor
        # try:
        #     self.inventory.remove(item)
        #     return item
        # except ValueError:
        #     return False

    def get_by_category(self, category):

        # utilized list comprehension
        category_items = [item for item in self.inventory if item.category == category]
        return category_items

    def swap_items(self, friend, my_item, friend_item):
        if my_item not in self.inventory or friend_item not in friend.inventory:
            return False

        self.remove(my_item)
        friend.add(my_item)
        friend.remove(friend_item)
        self.add(friend_item)

        return True
    
    def swap_first_item(self, friend):

        if not self.inventory or not friend.inventory:
            return False
        
        my_item = self.inventory.pop(0)
        friend.add(my_item)
        friend_item = friend.inventory.pop(0)
        self.add(friend_item)

        return True