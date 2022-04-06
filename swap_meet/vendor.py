# from .item import Item
class Vendor:
    def __init__(self, inventory = None):
        """
        You should not make the default parameter 
        a mutable objest. Set inventory as an 
        empty list.
            Parameters: inventory(list) = If no parameter passed in,
            inventory is an empty list
        """
        if not inventory:
            inventory = []
        self.inventory  = inventory
    
    def add(self, added_item):
        """
        Adds items to inventory list

            Parameters:
                    added_item(str): String of item added inventory(list)
            

            Returns:
                    added_item(str): String of item added inventory(list)
        """
        self.inventory.append(added_item)
        return added_item

    def remove(self, remove_item):
        """
        Checks to make sure remove_item is in inventory
        Removes items to inventory list

            Parameters:
                    remove_item(str): String of item remove inventory(list)
            

            Returns:
                    remove_item(str): String of item remove inventory(list)
        """
        if remove_item not in self.inventory:
            return False
        self.inventory.remove(remove_item)
        return remove_item

    def get_by_category(self, category):
        """
        Get category from inventory list

            Parameters: category(str): String used make to
                        compare to the category(str) in 
                        inventory(list)
            

            Returns:
                    category_items(list): Empty list
        """
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items

    def swap_items(self, friend, my_item, friend_item):
        """
        Remove items (my_item & friend_item) in each respective
        list (self.inventory & friend.inventory) and put at 
        the end of the other list
        (my_items to friend_items and friend_items to my_items)

            Parameters: friend(instance) = An instance of Vender class
                        
                        my_item(str) = An instance of Item
                        
                        friend_item(str) = An instance of Item
            

            Returns:
                    False(bool): If my_item is NOT IN my inventory list 
                    or friend_item is NOT IN my friend's inventory list
                    
                    True(bool): If my_item IS IN my inventory list 
                    AND friend_item IS IN my friend's inventory list,
                    Exchange items
        """
        if my_item not in self.inventory or\
            friend_item not in friend.inventory:
            return False
        else:
            friend.inventory.append(my_item)
            self.inventory.append(friend_item)
            friend.inventory.remove(friend_item)
            self.inventory.remove(my_item)
            return True


    def swap_first_item(self, friend):
        """
        Remove first items in each lists (self.inventory & 
        friend.inventory) and put at the end of the other list
        (my inventory[first item] to friend's inventory[first item] 
        and friend's inventory[first item] to my inventory[first item])

            Parameters: friend(instance) = An instance of Vender class


            Returns:
                    False(bool): If one of the lists is empty
                    
                    True(bool): If both lists exists, Exchange items
        """
        if not self.inventory or\
            not friend.inventory:
            return False

        else:
            friend.inventory.append(self.inventory[0])
            self.inventory.append(friend.inventory[0])
            friend.inventory.remove(friend.inventory[0])
            self.inventory.remove(self.inventory[0])
            return True

    # def get_best_by_category(self, category):
    #     # best_condition = 0
    #     # for item in self.inventory:
    #     #     if self.get_by_category() == category or:
    #     #         if 
