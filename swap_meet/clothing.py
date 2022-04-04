from .item import Item

class Clothing(Item):
    def __init__(self,condition=0,age=float("inf")):
        Item.__init__(self,category="Clothing",condition=condition,age=age)

    def __str__(self):
        return "The finest clothing you could wear."