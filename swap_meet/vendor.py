class Vendor:
    def __init__(self, inventory =[]):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            indx=self.inventory.index(item)
            item_removed=self.inventory.pop(indx)   
        else:
            return False
        return item_removed    

    def get_by_category(self, category):
        return [i for i in self.inventory if i.category ==category]  

    def swap_items(self, friend,my_item, their_item ):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        self.remove(my_item)
        self.add(their_item)
        friend.remove(their_item)
        friend.add(my_item)
        return True



