from swap_meet.item import Item


class Decor(Item):
    def __init__(self, condition=0):
        super().__init__(category= "Decor", condition=condition)

    def __str__(self):
        '''stringify (convert to a string) an instance of `Decor` 
            using `str()`, and return `"Something to decorate your space."`
        '''
        return "Something to decorate your space."

    def condition_description(self):
        '''method assigning a description to items based on the value,
            ranging from 0 being the worst and 5 being best. Use super()
            to bring in the method from the parent class Item
        '''
        return super().condition_description()