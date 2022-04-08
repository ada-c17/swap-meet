class Vendor():
  def __init__ (self, inventory = None):
    """Constructor with parameter as None. The parameter
    cannot be a mutable object, but is defined in the code below"""
    if inventory is None:
      inventory = []
    self.inventory = inventory
  
  def add(self, item):
    """Add instance method where item is appended to
    the instance self.inventory, return item"""
    self.inventory.append(item)
    return item

  def remove(self, item):
    """remove instance method where item removed if
    it is checked in self.inventory instance"""
    if item in self.inventory:
      self.inventory.remove(item)
      return item
    else:
      return False

  def get_by_category(self,string_category):
    """This function recieves a string parameter, and checks
    multiple items if they have the same category. The ouput is a list
    of items with the same category"""
    inventory_same_category = []
    for item in self.inventory:
      if item.category == string_category: 
        inventory_same_category.append(item) #only append item associated with category
    return inventory_same_category
  
  def swap_items(self, vendor, my_item, their_item):
    """This function receives three parameters that will
    be used when swapping items from self/vendor and my_item
    with their_item"""
    if my_item in self.inventory and their_item in vendor.inventory:
      self.inventory.remove(my_item)
      vendor.inventory.append(my_item)
      vendor.inventory.remove(their_item)
      self.inventory.append(their_item)
      return True
    else:
      return False

  def swap_first_item(self, vendor):
    """This function checks to make sure the list has at least
    one element, and switches the first element between self and vendor.
    The helper function swap_items is used"""
    if len(vendor.inventory) and len(self.inventory) != 0:
      self_first_item = self.inventory[0]
      vendor_first_item = vendor.inventory[0]
      swapped_item = self.swap_items(vendor, self_first_item, vendor_first_item)
      return True
    else:
      return False

  def get_best_by_category(self, string_category):
    """This function uses the helper function get_by_category 
    to get the condition of each catgory, finds the best condition
    and returns the item associated"""
    max_condition = 0
    stored_item = None 
    inventory_by_cat = self.get_by_category(string_category)
    for item in inventory_by_cat:
      if item.condition >= max_condition:
        max_condition = item.condition
        stored_item = item #include this to return item
    return stored_item

  def swap_best_by_category(self,other,my_priority,their_priority):
    """This function uses both helper functions get_best_by_category
    and swap_items to get the best item from self and vender, and
    swap those items. True is returned"""
    best_self_item = self.get_best_by_category(their_priority)
    best_their_item = other.get_best_by_category(my_priority)
    best_item_swapped = self.swap_items(other, best_self_item, best_their_item)
    return best_item_swapped #is True

  def find_newest_item(self):
    """This function is used to determine the newest_item by
    comparing the ages. I want the item associated with shortest_age
    to be the newest_item that is returned"""
    shortest_age = 100
    newest_item = None
    for item in self.inventory:
      if item.age < shortest_age:
        shortest_age = item.age 
        newest_item = item #assigning item of shortest_age to newest_item
    return newest_item

  def swap_by_newest(self, other):
    """This function uses the helper function find_newest_item for
    both self and other. Helper function swap_items is used to swap the
    newest items, and returns True"""
    my_newest_item = self.find_newest_item() #age of 2.0 
    their_newest_item = other.find_newest_item() #age of 1.0
    swapped_transaction = self.swap_items(other, my_newest_item, their_newest_item)
    return swapped_transaction