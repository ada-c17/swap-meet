class Vendor:
    """
    A class to represent a vendor.

    ...

    Attributes
    ----------
    inventory : list
        list of strings representing items in inventory

    Methods
    -------
    add(item):
        Adds an item to the inventory list.
        Returns item.
    
    remove(item):
        Removes an item from the inventory list.
        Returns item.
        If item not in list, returns False.

    get_by_category(category):
        Creates list of items whose category attribute matches the input category.
        Returns list. 

    swap_items(vendor_to_swap_with, item_vendor_swaps, item_vendor_gets):
        Removes item_vendor_swaps from vendor.inventory list and appends item_vendor_gets to list.
        Removes item_vendor_gets from vendor_to_swap_with.inventory list and appends.item_vendor_swaps to list
        Returns vendor's list.

    swap_first_item(vendor):
        swaps first items from my list and param vendor's list 
        Returns true if both lists are not empty

    return_best_by_category(category):
        returns item with best condition in vendor list given the category

    swap_best_by_category(other, my_priority, their_priority):
        checks for your best item given other's priority
        checks for their best item given your priority
        swaps those items
        returns true if swap occurs
    
    get_newest():
        returns item in self.inventory with the lowest age attribute value

    swap_by_newest(other):
        swaps your's and other vendor's newest items
        returns true if swap is successful
    """


    def __init__(self, inventory = None): #do not set keyword argument to list bc it is a mutable type
        """
        Constructs all the necessary attributes for the vendor object.

        Parameters
        ----------
            inventory : list
                list of strings representing items in inventory
        """

        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory


    def add(self, item):
        """
        Appends the item to the inventory list.

        Parameters
        ----------
        item : object

        Returns
        -------
        item
        """
        self.inventory.append(item)
        return item

    
    def remove(self, item):
        """
        Removes item from inventory list.

        Parameters
        ----------
        item : str

        Returns
        -------
        item or None
        """
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False
    

    def get_by_category(self, category):
        """
        Creates a list of items from inventory whose category attributes match the input category. 

        Parameters
        ----------
        category : str

        Returns
        -------
        items: list
        """

        return [item for item in self.inventory if item.category == category]
    

    def swap_items(self, vendor, my_item, vendor_item):
        """
        Removes and appends 2nd and 3rd parameters from my inventory respectively. Appends and removes 2nd and 3rd parameters from vendor's inventory respectively.

        Parameters
        -------
        vendor: composite object
        my item: component object 
        vendor_item: component object

        Returns
        -------
        self.inventory: object
        
        """
        if my_item in self.inventory and vendor_item in vendor.inventory:
                self.remove(my_item) 
                self.add(vendor_item)            
                vendor.remove(vendor_item)       
                vendor.add(my_item) 

                return True


    def swap_first_item(self, vendor):
        """
        Removes and appends first item from vendor and first item vendor_to_swap_with from my inventory respectively.Removes and appends first item from vendor_to_swap_with and first item vendor from vendor's inventory respectively.

        Parameters
        -------
        vendor: object

        Returns
        -------
        boolean
        """
        try:
            return self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
        except IndexError:
            return False


    def get_best_by_category(self, category):
        """
        Given the category, return the item with the best condition.

        Parameters
        -------
        category: str

        Returns
        -------
        best_item: object
        """

        inventory_by_category = self.get_by_category(category)

        try:
            return max(inventory_by_category, key = lambda item: item.condition) #max item of sorted items list where we compare number values from the item's condition attribute retreived via lambda function
        except ValueError:
            return None


    def swap_best_by_category(self,other, my_priority,their_priority):
        """
        Given the other vendor, your item category preference, and the vendor's item category preference, swap items that are the best in each category. 

        Parameters
        -------
        other: object
        my_priority: str
        their_priority: str

        Returns
        -------
        boolean
        """
        other_best = other.get_best_by_category(my_priority)
        my_best = self.get_best_by_category(their_priority)

        return self.swap_items(other, my_best, other_best)
    
    def get_newest(self):

        try:
            return min(self.inventory, key = lambda item: item.age)#min item of items list where we compare number values from the item's age attribute retreived via lambda function
        except ValueError:
            return None

    def swap_by_newest(self, other):
        """
        Swaps my newest item with other vendor's newest item.

        Parameters
        -------
        vendor: object

        Returns
        -------
        boolean
        """
        other_newest = other.get_newest()
        my_newest = self.get_newest()

        return self.swap_items(other, my_newest, other_newest)



            




