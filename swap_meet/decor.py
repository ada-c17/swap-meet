from swap_meet.item import Item

class Decor(Item):
    def __init__(self,condition = 0.0):
        super().__init__('Decor', condition) 

    def __str__(self):
        return "Something to decorate your space."
#____________________________

# class Decor:
#     def __init__(self, condition = 0.0):
#         self.category = 'Decor'
#         self.condition = condition

#     def __str__(self):
#         return "Something to decorate your space."
    
#     def condition_description(self):
#         if self.condition >=0 and self.condition <1:
#             return 'heavily_used'
#         elif self.condition >=1 and self.condition <2:
#             return 'often_used'
#         elif self.condition >=2 and self.condition <3:
#             return 'moderately_used'
#         elif self.condition >=3 and self.condition <4:
#             return 'occasionally_used'
#         elif self.condition >=4 and self.condition <5:
#             return 'rarely_used'
#         else:
#             return 'mint'