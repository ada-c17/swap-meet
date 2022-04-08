from .item import Item

class Vendor:
    def __init__(self,inventory = []):
        self.inventory = inventory

    
    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
           

    def get_by_category(self,category):
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        return category_list
            

    def swap_items(self,vendor,my_item,their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
            vendor.inventory.remove(their_item) 
            self.inventory.append(their_item)
            return True
        else:
            return False

    def swap_first_item (self,vendor):
        if len(self.inventory) > 0 and len(vendor.inventory) > 0:
    
            item = self.inventory[0]
            vendor_item = vendor.inventory[0]

            self.inventory.remove(item)
            vendor.inventory.insert(0,item) 
            vendor.inventory.remove(vendor_item)
            self.inventory.insert(0,vendor_item)
            return True
        else:
            return False

    def get_best_by_category(self,category="Clothing"):
        best_item_list = []
        for best_item in self.inventory:
            if best_item.category == category:
                best_item_list.append(best_item)

        if len(best_item_list) == 0:
            return None
        else: 
            max = best_item_list[0]
            for best_item in best_item_list:
                if best_item.condition > max.condition:
                    max = best_item
            return max
            
            
    def swap_best_by_category(self,other,my_priority,their_priority):
        my_dict ={}
        for item in self.inventory:
            if item.category == their_priority.category:
                dict[item]= item.condition
                best_item_my_inventory = max(my_dict,key=my_dict.get)

        other_dict ={}
        for item in other.inventory:
            if item.category == my_priority.category:
                dict[item]= item.condition
                best_item_other_inventory = max(other_dict,key=other_dict.get)


        if len(self.inventory) > 0 and len(other.inventory) > 0:
    
            self.inventory.remove(best_item_my_inventory)
            other.inventory.insert(best_item_my_inventory) 
            other.inventory.remove(best_item_other_inventory)
            self.inventory.insert(best_item_other_inventory)
            return True
        else:
            return False


            


            





vendor = Vendor()
other = Vendor()





