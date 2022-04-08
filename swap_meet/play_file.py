
# class Vendor:

#     def __init__ (self):
#        self.inventory = [] 

#     def add(self, item):
#         self.inventory.append(item)
#         return self.inventory

#     def remove(self, item):
#         if item not in self.inventory:
#             return False
#         else :
#              self.inventory.remove(item)


# class Car:
#     def __init__(self, color):
#         self.color = color
#     def __str__(self):
#         return f"a {self.color} car"

# my_car = Car("green")
# print(type(my_car))
# str(my_car)
# print(str(my_car))
# print(type(str(my_car)))



#     item_d = Item(category="electronics")
#     item_e = Item(category="decor")
#     jolie = Vendor(
#         inventory=[item_d, item_e]
#     )

class Vendor:

    def __init__ (self, inventory=[]):
       self.inventory = inventory

     


    # def swap_items(self,vendor, my_item, their_item ):
    #     self.inventory.append(their_item)
    #     vendor.inventory.append(my_item)



# item_a = hat_1)
# item_b = Item(category="clothing")
# item_c = Item(category="clothing")


# item_d = Item(category="electronics")
# item_e = Item(category="decor")

book_1 = "Seaside"
coat_1 = "Red_Coat"
hat_1 = "Blue Hat"

coat_2 = "White_Coat"
hat_2 = "Green Hat"

vendor_1 = Vendor(inventory=[book_1,coat_1, hat_1])
vendor_2 = Vendor(inventory=[coat_2, hat_2])
def swap_first_item(self,vendor):
        if vendor.inventory == []:
            return False
        else:
            if self.inventory == []:
                return False
            self.inventory.append(vendor.inventory[0])
            vendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            vendor.inventory.remove(vendor.inventory[0])
        return True





print(vendor_1.inventory)
print(vendor_2.inventory)
print(vars(vendor_1))
print(dir(vendor_2))




# class Item:
#     def __init__(self,item = None, category = "" ):      
#          self.category = category
#          self.item = item

#     def __str__(self):      
#          return f"Hello World!"
# string = Item("Hello World")
# # string2 =str(string)
# print(str(string))



# inventory = ["books", "boots", "bins"]
# vendor_inventory = Vendor()
# print(vendor_inventory.inventory)
# print(vendor_inventory.add("shoes"))
# print(vendor_inventory.add("coat"))