from swap_meet.item import Item

class Vendor:
    
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        """
        takes in one item
        adds item to inventory
        returns item that was added
        """
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False    

    def get_by_category(self, category_str):
        category_list = []
        for elem in self.inventory:
            if elem.category == category_str:
                category_list.append(elem)
        return category_list

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item \
            not in friend.inventory:
            return False
        self.inventory.remove(my_item)
        friend.inventory.append(my_item)
        friend.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True