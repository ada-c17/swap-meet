class Item:
    '''
    A class to represent an item object

    ...

    ---Attributes---
    category : str, optional
        empty string by default, otherwise a specific category represented by a string
    condition : int or float, optional
        zero by default, otherwise a number representing the condition of the item

    ---Methods---
    __str__():
        sets dunder str to a string

    condition_description():
        based on an item instance's numerical condition, returns a string description of that condition

    '''
    def __init__(self, category="", condition=0):
        '''
        Constructs all the necessary attributes for the item object

        ---Paramters---
        category : str, optional
            empty string by default, otherwise a specific category represented by a string
        condition : int or float, optional
            zero by default, otherwise a number representing the condition of the item
        '''
        self.category = category
        self.condition = condition


    def __str__(self):
        '''sets dunder str to a string'''
        return "Hello World!"

    def condition_description(self):
        '''
        based on an item instance's numerical condition, returns a string description of that condition
        '''
        descriptors = [
            "Mint",
            "Like New",
            "Gently Used",
            "Used",
            "Well Used",
            "Bad Condition",
        ]
        if 1 > self.condition >= 0:
            return descriptors[0]
        elif 2 > self.condition >= 1:
            return descriptors[1]
        elif 3 > self.condition >= 2:
            return descriptors[2]
        elif 4 > self.condition >= 3:
            return descriptors[3]
        elif 5 > self.condition >= 4:
            return descriptors[4]
        elif self.condition == 5:
            return descriptors[5]