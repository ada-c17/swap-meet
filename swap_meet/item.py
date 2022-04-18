class Item:
    def __init__(self, category = "", condition = 0):
        '''
        Its parameter category is an empty string, condition has a default value of 0
        '''
        self.category = category
        self.condition = condition

    def __str__(self):
        '''
        Overrides string representation to return "Hello World"
        '''
        return "Hello World!"

    def condition_description(self):
        '''
        It describe the condition in words based on the value, range from 0 to 5
        Return: a string that describes condition
        '''
        if self.condition == float(5):
            return "Like New"
        elif self.condition == float(4):
            return "Pretty Good"
        elif self.condition == float(3):
            return "Good"
        elif self.condition == float(2):
            return "Fair"
        elif self.condition == float(1):
            return "Used"
        else:
            return "Poorly Used"