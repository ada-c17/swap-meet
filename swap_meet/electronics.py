from .item import Item


class Electronics(Item):
    def __init__(self, condition=0):
        super().__init__(category= "Electronics", condition=condition)

    def __str__(self):
        '''stringify (convert to a string) an instance of `Electronics` 
            using `str()`, and return `"A gadget full of buttons and secrets."`
        '''
        return "A gadget full of buttons and secrets."

    def condition_description(self):
        '''method assigning a description to items based on the value,
            ranging from 0 being the worst and 5 being best. Use super()
            to bring in the method from the parent class Item
        '''
        return super().condition_description()
