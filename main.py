from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# test ratings

clothing_1 = Clothing(1)
clothing_2 = Clothing(2)
clothing_3 = Clothing(3)
clothing_4 = Clothing(4)
clothing_5 = Clothing(5)
clothing_neg = Clothing(-1)
clothing_max = Clothing(10)
clothing_float = Clothing(3.5)

item_list = [
    clothing_1, 
    clothing_2, 
    clothing_3, 
    clothing_4, 
    clothing_5, 
    clothing_float, 
    clothing_max, 
    clothing_neg
]

for item in item_list:
    print(item.condition_description())

