class Vendor:
    '''
    Class representing a single vendor with items to trade

    Functions:
        add(object, item)
        remove(object, item)
        get_by_category(object, category)
        swap_items(object, another object, my_item, their_item)
        swap_first_item(object, another object)
        get_best_by_category(self, category):
        swap_best_by_category(self, other, my_priority, their_priority):

    Variables:
        inventory: list of items for a vendor to see default is [] 
    '''
    def __init__(self, inventory=None):
        if not inventory == None:
            self.inventory = inventory
        else:
            self.inventory = []
        # self.inventory = inventory if inventory is not None else []


    def add(self, item):
        """Method to add passed item to instances inventory"""
        self.inventory.append(item)

        return item


    def remove(self, item):
        """Method to remove passed item to instances inventory"""
        if not item in self.inventory:
            return False

        self.inventory.remove(item)

        return item


    def get_by_category(self, category):
        """Method to return a list of items of a passed category"""
        category_list = []

        for item in self.inventory:
            if item.category == category:
                category_list.append(item)

        #category_list = [item for item in self.inventory if item.category == category]
        return category_list


    def swap_items(self, other, my_item, their_item):
        """Method to pass items of two Vendor Classes"""
        if (not my_item in self.inventory 
            or not their_item in other.inventory):
            return False
        
        self.add(their_item)
        other.add(my_item)

        self.remove(my_item)
        other.remove(their_item)

        return True


    def swap_first_item(self, other):
        """Method to swap first items of two Vendor Classes"""
        if self.inventory == [] or other.inventory == []:
            return False

        self.swap_items(other, self.inventory[0], other.inventory[0])

        return True


    def get_best_by_category(self, category):
        """Method to return the highest condition item of a category"""
        category_list = self.get_by_category(category)
        if not category_list:
            return None
        
        best = category_list[0]

        for item in category_list:
            if item.condition > best.condition:
                best = item

        #unsure if this can be done in one line

        return best
        

    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Method to swap two vendors best condition item of 
        the others chosen category
        """
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        if not my_item or not their_item:
            return False

        self.swap_items(other, my_item, their_item)

        return True