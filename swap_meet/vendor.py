from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        #??? create a copy of inventory list for removing items 
        if item in list(self.inventory):
            self.inventory.remove(item)
            return item
        
        else:
            return False

    def get_by_category(self, category):
        """
        input : category name
        output: a list of items in the inventory w/ that category
        """
        #need self for the list created?
        self.items_by_category= []
        for item in self.inventory:
            if item.category == category:
                self.items_by_category.append(item)
        return self.items_by_category
    

    def swap_items(self, friend, my_item, their_item):
        """
        purpose:
        -It removes the my_item from this Vendor's inventory, and adds it to the friend's inventory
		-It removes the their_item from the other Vendor's inventory, and adds it to this Vendor's inventory
        
        input: 
        friend = Vendor() instance of a Vendor
        my_item = Item() 
        their_item = Item()
        
        Output:
		-It returns True
        -If this Vendor's inventory doesn't contain my_item or the friend's inventory doesn't contain their_item, the method returns False
        """
        if my_item in self.inventory and their_item in friend.inventory:
            #remove my item from my list and add to friend's list
            self.remove(my_item)
            friend.add(my_item)

            #remove their item from friend's list and add to my list
            friend.remove(their_item)
            self.add(their_item)
            return True


    def swap_first_item(self, friend):
        """
        purpose:
        remove my first item in inventory, add to friend's inventory
        remove friend's first item in inventory , add to my inventory

        input: friend = Vendor()
        output:		
        -It returns True
        -If either itself or the friend have an empty inventory, the method returns False

        """

        if len(self.inventory) >= 1 and len(friend.inventory) >= 1:
            self.swap_items(friend, self.inventory[0], friend.inventory[0])
            return True
            #does instance method self.swap_items() alreay return True?

    def get_best_by_category(self, category):
        """
        purpose: get the item with best condition in that category
        input : category
        output: -return the item with best condition in that category
                -if no item in matching category, return none
                -It returns a single item even if there are duplicates\n
                (two or more of the same item with the same condition

        Q: what if there are 2 or more different items in matching category\n
    with same highest score        
        """
        self.best_item = ""
        best_condition = 0
        category_list = self.get_by_category(category)
        if category_list != []: 
            for item in category_list:
                if item.condition > best_condition:
                    best_condition = item.condition
                    self.best_item = item
            return self.best_item




            

    def swap_best_by_category(self, other, my_priority, their_priority):
        """
        purpose:swap the best item of certain categories with another Vendor
        input: other:  Vendor()  a vendor instance to trade with
                my_priority:  a category that the Vendor wants to receive
                their_priority: a category that other wants to receive
        
        output: -return True
                - return False if vendor has no item that matches thier_priority category\n
                or others has no item thay matches vendor's priority category
        """     

        #get best item vendor want to have in "my_priority" category

        self.item_to_vendor = other.get_best_by_category(my_priority)
        self.item_to_other = self.get_best_by_category(their_priority)
        if self.item_to_vendor and self. item_to_other:
            self.swap_items(other, self.item_to_other, self.item_to_vendor)
            return True
        else:
            return False 


    def swap_by_newest(self, other, my_priority, their_priority):
        """
        purpose:swap the newest item of certain categories with another Vendor
        input: other:  Vendor()  a vendor instance to trade with
                my_priority:  a category that the Vendor wants to receive
                their_priority: a category that other wants to receive
        
        output: -return True
                - return False if vendor has no item that matches thier_priority category\n
                or others has no item thay matches vendor's priority category
        """     
        
        self.newest_item_from_mylist = ""
        self.newest_item_from_otherlist = ""
        my_category_list = self.get_by_category(their_priority)
        their_category_list = other.get_by_category(my_priority)
        
        if my_category_list!= [] and their_category_list!= []:
            my_min_age = my_category_list[0].age
            for item in my_category_list:
                if item.age < my_min_age:
                    my_min_age = item.age
                    self.newest_item_from_mylist = item
                else:
                    self.newest_item_from_mylist = my_category_list[0]

            other_min_age = their_category_list[0].age
            for item_other in their_category_list:
                if item_other.age < other_min_age:
                    other_min_age = item_other.age
                    self.newest_item_from_otherlist = item_other
                else:
                    self.newest_item_from_otherlist = their_category_list[0]
            

            self.swap_items(other, self.newest_item_from_mylist, self.newest_item_from_otherlist)
            return True

        else:
            return False