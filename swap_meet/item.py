class Item:

    def __init__(self, category="", condition=0, age=None):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self, condition=0):
        '''Converts a condition's numeric value to a descriptive phrase.'''
        condition = self.condition
        if condition == 0:
            self.__str__ = "EWW! What is this?!"
        elif condition == 5:
            self.__str__ = "Brand new!"
        elif condition > 4:
            self.__str__ = "Still great condition!"
        elif condition > 3:
            self.__str__ = "Worn with love"
        elif condition > 2:
            self.__str__ = "Lots of wear and tear"
        elif condition > 1:
            self.__str__ = "Not worth fixing"
        else:
            self.__str__ = "Throw away immediately"
        return self.__str__
