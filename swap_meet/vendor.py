"""
### Wave 1

In Wave 1 we will create the `Vendor` class.

- There is a module (file) named `vendor.py` inside of the `swap_meet` package (folder)
- Inside this module, there is a class named `Vendor`
- Each `Vendor` will have an attribute named `inventory`, which is an empty list by default
- When we instantiate an instance of `Vendor`, we can optionally pass in a list with the keyword argument `inventory`


- Every instance of `Vendor` has an instance method named `add`, which takes in one item
- This method adds the item to the `inventory`
- This method returns the item that was added

- Similarly, every instance of `Vendor` has an instance method named `remove`, which takes in one item
- This method removes the matching item from the `inventory`
- This method returns the item that was removed
- If there is no matching item in the `inventory`, the method should return `False`

### Wave 2

- When we initialize an instance of `Item`, we can optionally pass in a string with the keyword argument `category`
- Instances of `Vendor` have an instance method named `get_by_category`
  - It takes one argument: a string, representing a category
  - This method returns a list of `Item`s in the inventory with that category

### Wave 3

- Instances of `Vendor` have an instance method named `swap_items`
  - It takes 3 arguments:
    1. an instance of another `Vendor`, representing the friend that the vendor is swapping with
    2. an instance of an `Item` (`my_item`), representing the item this `Vendor` instance plans to give
    3. an instance of an `Item` (`their_item`), representing the item the friend `Vendor` plans to give
  - It removes the `my_item` from this `Vendor`'s inventory, and adds it to the friend's inventory
  - It removes the `their_item` from the other `Vendor`'s inventory, and adds it to this `Vendor`'s inventory
  - It returns `True`
  - If this `Vendor`'s inventory doesn't contain `my_item` or the friend's inventory doesn't contain `their_item`, the method returns `False`

### Wave 4

- Instances of `Vendor` have an instance method named `swap_first_item`
  - It takes one argument: an instance of another `Vendor`, representing the friend that the vendor is swapping with
  - This method considers the first item in the instance's `inventory`, and the first item in the friend's `inventory`
  - It removes the first item from its `inventory`, and adds the friend's first item
  - It removes the first item from the friend's `inventory`, and adds the instances first item
  - It returns `True`
  - If either itself or the friend have an empty `inventory`, the method returns `False`

### Wave 6

In Wave 6 we will write two methods, `get_best_by_category` and `swap_best_by_category`.

- `Vendor`s have a method named `get_best_by_category`, which will get the item with the best condition in a certain category
  - It takes one argument: a string that represents a category
  - This method looks through the instance's `inventory` for the item with the highest `condition` and matching `category`
    - It returns this item
    - If there are no items in the `inventory` that match the category, it returns `None`
    - It returns a single item even if there are duplicates (two or more of the same item with the same condition)

The remaining tests in wave 6 imply:

- `Vendor`s have a method named `swap_best_by_category`, which will swap the best item of certain categories with another `Vendor`
  - It takes in three arguments
    - `other`, which represents another `Vendor` instance to trade with
    - `my_priority`, which represents a category that the `Vendor` wants to receive
    - `their_priority`, which represents a category that `other` wants to receive
  - The best item in my inventory that matches `their_priority` category is swapped with the best item in `other`'s inventory that matches `my_priority`
    - It returns `True`
    - If the `Vendor` has no item that matches `their_priority` category, swapping does not happen, and it returns `False`
    - If `other` has no item that matches `my_priority` category, swapping does not happen, and it returns `False`

"""

from asyncio.format_helpers import _format_callback_source

from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    #with .pop()
    def remove(self, item):
        for i in range(len(self.inventory)):
            if self.inventory[i] == item:
                removed = self.inventory.pop(i)
                return removed
        return False

    #with .remove()
    # def remove(self,item):
    #     aList = self.inventory
    #     for thing in aList:
    #         if thing == item:
    #             self.inventory.remove(thing)
    #             return thing
    #     return False

    def get_by_category(self, category):
        itemList = []
        
        for item in self.inventory:
            if item.category == category:
                itemList.append(item)
        #returns a list of `Item`s in the inventory with that category
        return itemList

    # using list comprehension, don't have to use append
    # itemList = [item for item in self.inventory if item.category == category]
    """
    
    To further reduce the amount of repeated code in your project, 
    consider how `swap_best_by_category` and `swap_first_item` might be able to make use of `swap_items`. 
    Is there a way that these methods could incorporate a call to `swap_items` into the body of these methods?

    ###To do this, could create default paremeters or is it keyword arguments for my_item and their item in swap items
    then create an if, elif situation in swap items, then replace the expression in the if statement of swap_first_item with
    the swap_items function ???? not sure what the default parameters/keyword args would be tho...
    update: Oh my gosh I don't know why I thought about this like this, can just use in the other funcs like Hailey and Philomena did....
    
    """    
    
    def swap_items(self,friend, my_item, their_item):
        #If this `Vendor`'s inventory doesn't contain `my_item` or the friend's inventory doesn't contain `their_item`, the method returns `False`
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False

        #remove the `my_item` from this `Vendor`'s inventory, and add it to the friend's inventory
        my_removed = self.remove(my_item)
        friend.inventory.append(my_removed)

        #remove the `their_item` from the other `Vendor`'s inventory, and add it to this `Vendor`'s inventory
        their_removed = friend.remove(their_item)
        self.inventory.append(their_removed)
        
        return True

    def swap_first_item(self,friend):
        #If either itself or the friend have an empty `inventory`, the method returns `False`

        #can use not like Anya did because I think empty lists are falsey
        #if not self.inventory or not friend.inventory:
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False

        #remove the first item from its `inventory`, and adds the friend's first item
        #remove the first item from the friend's `inventory`, and adds the instances first item

        #need to add first to both and then remove otherwise it won't work...
        #can just use self.swap_items and pass in the first items of each list
        self.add(friend.inventory[0])
        friend.add(self.inventory[0])
        
        self.remove(self.inventory[0])
        friend.remove(friend.inventory[0])
        
        return True

    """
    
    Gets the item with the best condition in a certain category, one argument: a string that represents a category
    
    """
    def get_best_by_category(self, category):
        #looks through the instance's `inventory` for the item with the highest `condition` and matching `category`, returns this item
        highestCondition = 0
        bestItem = None
        for item in self.inventory:
            if item.category == category:
                if item.condition > highestCondition:
                    highestCondition = item.condition
                    bestItem = item
        return bestItem

#If there are no items in the `inventory` that match the category, it returns `None`
#It returns a single item even if there are duplicates (two or more of the same item with the same condition)





#three arguments
    #`other`, which represents another `Vendor` instance to trade with
    #`my_priority`, which represents a category that the `Vendor` wants to receive
    #`their_priority`, which represents a category that `other` wants to receive
#the best item in my inventory that matches `their_priority` category is swapped with the best item in `other`'s inventory that matches `my_priority`
    #It returns `True`
    #If the `Vendor` has no item that matches `their_priority` category, swapping does not happen, and it returns `False`
    #If `other` has no item that matches `my_priority` category, swapping does not happen, and it returns `False`

    #swap the best item of certain categories with another `Vendor`
    #oh my gosh I made my code so longgggg, could have used get best by category function and then the swap items function.....
    def swap_best_by_category(self, other, my_priority, their_priority):
        myHighestCondition = 0
        theirHighestCondition = 0
        myBestItem = None
        theirBestItem = None
        
        for myItem in self.inventory:
            if myItem.category == their_priority:
                if myItem.condition > myHighestCondition:
                    myHighestCondition = myItem.condition
                    myBestItem = myItem
        
        for theirItem in other.inventory:
            if theirItem.category == my_priority:
                if theirItem.condition > theirHighestCondition:
                    theirHighestCondition = theirItem.condition
                    theirBestItem = theirItem
        
        if myBestItem is None or theirBestItem is None:
            return False
        
        #I think I can use swap_items here with theirBestItem and myBestItem as the args.....
        self.inventory.append(theirBestItem)
        self.inventory.remove(myBestItem)
        other.inventory.append(myBestItem)
        other.inventory.remove(theirBestItem)

        return True