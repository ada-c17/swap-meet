class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, add_item):
        add = self.inventory.append(add_item)
        return add_item

    def remove(self, sub_item):
        if sub_item in self.inventory:
            self.inventory.remove(sub_item)
            return sub_item
        else:
            return False
    

    def get_by_category(self, category):
        each_category = []
        for item in self.inventory:
            if item.category == category:
                each_category.append(item)
        return each_category


    


        
        


