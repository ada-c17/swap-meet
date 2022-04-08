
class Item:
    #test-wave_02
    def __init__(self, category = '', condition =0.0):
        self.category = category
        self.condition = condition

    #test_wave_03
    # Add__str__overload method for printing instances
    def __str__(self):
        return 'Hello World!'

    #test_wave_05
    '''
    class clothing, class Decor and class Electronics must have
    the same behavior in the method condition description
    describe conditions based on the value from 0 to 5
    value 5: 'mint'
    value 4: 'rarely_used'
    value 3: 'occasionally_used'
    value 2: 'moderately_used'
    value 1: 'often_used'
    value 0: 'heavily_used'
    '''
    def condition_description(self):
        if self.condition >=0 and self.condition <1:
            return 'heavily_used'
        elif self.condition >=1 and self.condition <2:
            return 'often_used'
        elif self.condition >=2 and self.condition <3:
            return 'moderately_used'
        elif self.condition >=3 and self.condition <4:
            return 'occasionally_used'
        elif self.condition >=4 and self.condition <5:
            return 'rarely_used'
        elif self.condition ==5:
            return 'mint'
    



