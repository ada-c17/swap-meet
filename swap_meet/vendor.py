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