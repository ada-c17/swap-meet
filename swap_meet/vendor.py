class Vendor:
    """
    A class to represent a Vendor.
    . . .

    Attributes 
    - - - - - -
    inventory : list
            store list of items in vendor
        default : None

    Methods 
    - - - - - -
    add(item):
        Adds the item to vendor's inventory

    remove(item):
        Removes the item from vendor's inventory

    get_by_category(category):
        Returns a list of items in inventory with the category equivalent to the input category

    swap_items(other_vendor, my_item, their_item):
        Removes my_item from vendor and adds it into other_vendor. Removes their_item from other_vendor and adds it into vendor 

    swap_first_item(other_vendor):
        Removes first item in other_vendor and adds it into vendor. Removes first item in vendor and adds it into other_vendor

    get_best_by_category(category):
        Returns item in category with the highest condition

    swap_best_by_category(other, my_priority, their_priority):
        Removes my_priority from other and adds it to vendor. Removes their_priority and adds it to other
    """

    def __init__(self, inventory=None):
        """
        Constructs all the necessary attributes for the vendor
        . . .

        Parameters 
        - - - - - -
        inventory : list 
                stores the items in vendor
            default : None
        """

        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        """
        Adds the item to Vendor's inventory.

            Parameters:
                item: string, the item to be added into inventory
            Returns:
                item if added. False if not
        """
        if type(item) == list:
            for object in item:
                self.inventory.append(object)
        else:
            self.inventory.append(item)
        return item

    def remove(self, item):
        """
        Removes the item from Vendor's inventory if inventory contains the itmm.

            Parameters:
                item: string, the item to be removed 

            Returns:
                item if removed. False is not
        """
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        """
        Returns a list of items in inventory with the category equivalent to the input category

            Parameters:
                category: string, the name of category

            Returns:
                item_list (list): List storing all strings representing the category of input category
        """
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

    def swap_items(self, other_vendor, my_item, their_item):
        """
        Removes my_item from vendor and adds it into other_vendor. Removes their_item from other_vendor and adds it into vendor 

            Parameters:
                other_vendor: item
                my_item: string
                their_item: string

            Returns:
                True : bool 
                False : bool

        """
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        other_vendor.remove(their_item)
        other_vendor.add(my_item)
        self.add(their_item)
        return True

    def swap_first_item(self, other_vendor):
        """
        Removes first item in other_vendor and adds it into vendor. Removes first item in vendor and adds it into other_vendor

            Parameters:
                other_vendor: item : other inventory

            Returns:
                True : bool : when first items have been removed and added between the two vendors

                False : bool : if either the vendor's list or the other_vendor list is empty

        """
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        else:
            results = self.swap_items(
                other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True

        # if self.inventory == [] or other_vendor.inventory == []:
        #     return False
        # else:
        #     item = self.inventory.pop(0)
        #     other_item = other_vendor.inventory.pop(0)
        #     self.inventory.append(other_item)
        #     other_vendor.inventory.append(item)
        #     return True

    def get_best_by_category(self, category):
        """
        Returns item in category with the highest condition

            Parameters:
                category : str

            Returns:
                best_item : item with the highest condition and in the category equivalent to the inputed category  
        """
        category_list = self.get_by_category(category)
        max_condition = 0
        best_item = None

        for item in category_list:
            if item.condition > max_condition:
                best_item = item
                max_condition = item.condition
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        Removes my_priority from other(other vendor) and adds it to vendor (self vendor). Removes their_priority and adds it to other

            Parameters:
                other: other inventory 

                my_priority: str : item that wants to be added to own inventory

                their_priority: str : item that wants to be added to other

            Returns:
                best_item : item with the highest condition and in the category equivalent to the inputed category  
        """
        my_best = self.get_best_by_category(
            their_priority)
        others_best = other.get_best_by_category(
            my_priority)

        if my_best == None or others_best == None:
            return False
        else:
            swap_items = self.swap_items(other, my_best, others_best)
            return True
