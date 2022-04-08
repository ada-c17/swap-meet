from operator import inv
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing

friend = Vendor(inventory = ["lamp", "phone", "vase", "picture"])
# print(friend.inventory)

# # print(vars(friend))
print(dir(friend))
# print(friend.add("pen"))
# print(friend.inventory)
# friend.remove("phone")
# print(friend.inventory)
top = Clothing(condition=1.1)
skirt = Clothing(condition=3.5)
jacket = Clothing(condition=4)
hoodie = Clothing(condition=2.6)
shorts = Clothing(condition=4)

[top, skirt, jacket, hoodie, shorts]

clothing_inv1 = {
    "top": 1.1, 
    "skirt": 3.5,
    "jacket": 4,
    "hoodie": 2.6,
    "shorts": 4
}
# decor_inv = ['vase', 'picture', "bell", "cat statue"]
# electronics_inv = ['phone', 'tablet', 'laptop', 'thermometer', 'calculator']
cloth_list = []

def get_cloth_list(inventory):
    for item, cond in inventory.items():
        item = Clothing(condition = cond)
        print(item)
        cloth_list.append(item)
    return cloth_list
        
print(get_cloth_list(clothing_inv1))