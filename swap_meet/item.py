class Item:
    def __init__(self, category = ""):
        self.category = category

    def __str__(self):
        return("Hello World!")

    def __repr__(self): #created repr dunder method just for funzies
        rep = 'Item(' + self.category + ')'
        return rep