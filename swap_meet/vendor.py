class Vendor():
    # create inventory parameters, where deafalt is empty list
    def __init__(self,inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    

    # create instance method add which add things in inventory list
    def add(self,item):
        self.inventory.append(item)
        return item


    # create instance method remove which remove item from inventory list
    def remove(self,item):
        for items in self.inventory:
            if item == items:
                self.inventory.remove(items)
                return items
        return False


    # create instance method which return a list of Items in the inventory with that category
    def get_by_category(self,category):
        list_of_items = []
        for item in self.inventory:
            if category == item.category:
                list_of_items.append(item)
        return list_of_items


    # create instance method implement swaping process
    def swap_items(self, friend, my_item, friends_item):
        
        if not my_item or not friends_item:
            return False
        
        else:
            if my_item in self.inventory and friends_item in friend.inventory:
                # vendor swap his item
                self.remove(my_item)
                friend.add(my_item)
                # friend swap his item
                friend.remove(friends_item)
                self.add(friends_item)
                return True

    # create instance method implement swaping process first item
    def swap_first_item(self, friend):

        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False
        else:
            # grab first element from self list 
            first_item = self.inventory[0]
            # remove from self inventory
            self.remove(first_item)
            # add to friends inventory 
            friend.add(first_item)

            # grab first element from friends list
            first_item = friend.inventory[0]
            # remove this elem from friensd list
            friend.remove(first_item)
            # add to self inventory
            self.add(first_item)
            return True

    def get_best_by_category(self, consider_category):

        # creating dictionary to store matching category with highet rate
        best_dict_category = {}
        best_dict_category[consider_category] = 0.0
        # creating counter to check no matches categories in vendors inventory
        count = 0

        # consider given represents string of category, add to dictionary 
        # matching category is key and value is rate. Setup first element
        # of dictionary like max and matching other rate, if higher add to dict 
        for category_from_inv in self.inventory:
            if consider_category == category_from_inv.category:
                count += 1
                if category_from_inv.condition > best_dict_category[consider_category]:
                    best_dict_category[category_from_inv.category] = category_from_inv.condition
                    best_category = category_from_inv
            if count == 0:
                return None
        return best_category

    def swap_best_by_category(self, other, my_priority, their_priority):

        if len(self.inventory) == 0 or len(other.inventory) == 0:
            return False
        else:
            # get best result of category by prioriry for friend
            best_item_for_friend = self.get_best_by_category(their_priority)
            print(best_item_for_friend)
            # get best result of category by prioriry for vendor
            best_item_for_vendor = other.get_best_by_category(my_priority)
            print(best_item_for_vendor)

            if best_item_for_friend == None or best_item_for_vendor == None:
                return False
            else:
                #swapping items: 
                #remove from self inventory
                self.remove(best_item_for_friend)
                # add to friends inventory 
                other.add(best_item_for_friend)
                # remove this elem from friensd list
                other.remove(best_item_for_vendor)
                # add to self inventory
                self.add(best_item_for_vendor)

                return True