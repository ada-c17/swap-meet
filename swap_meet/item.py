class Item:
    '''
    A class indicating an object Item that a vendor might have.
    
    Attributes:
    category (str): optional descr. of item category. None if not defined,
        w/attribute set to an empty string. Otherwise set to input param.
    condition (float): optional descr. of item condition, 0 if not defined
    '''

    def __init__(self, category=None, condition=0):
        '''
        Parameters:
        category (str): optional descr. of item category. None if not defined,
            w/attribute set to an empty string. Otherwise set to input param.
        condition (float): optional descr. of item condition, 0 if not defined
        '''

        if category is None:
            self.category = ""
        else:
            self.category = category
        self.condition = condition

    def __str__(self):
        '''Stringifies Item and returns a string to say hello.'''

        return "Hello World!"

    def condition_description(self):
        '''
        Method to return string description related to item condition.
        Returns: a string for default condition of 0, and any float up to 5.0
        '''
        
        if self.condition == 0:
            return "I'm not sure about the condition of this item."
        elif self.condition <= 1:
            return "Why are you even swapping this?"
        elif self.condition <= 2:
            return "You could do better."
        elif self.condition <= 3:
            return "Blisteringly mediocre."
        elif self.condition <= 4:
            return "I'll accept this. I guess."
        elif self.condition <= 5:
            return "Wow, this is amazing!"