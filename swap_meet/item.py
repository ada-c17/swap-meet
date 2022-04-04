class Item:
    def __init__(self, category="", condition=0):
        self.condition =condition
        self.category =category

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        description={
            0:"You probably want a glove for this one...",
            1:"poor",
            2:"fair",
            3:"good",
            4:"like new",
            5:"new"
        }    
        return description[self.condition]

