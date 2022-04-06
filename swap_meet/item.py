class Item:

    def __init__(self, category = ""):
        self.category = category
        
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        """ 
        5: "This is brand new"
        4: "This is mint condition"
        3: "Has wear commiserate of age"
        2: "Almost time to retire"
        1: "About to fall apart"
        0: "I will disentegrate just by looking at me."
        """
        
        
