
class Item:

   
    def __init__(self, category = "", condition = 0.0):
        """
        def __init__ creates attribute of empty string category and condition with default value
        """
        self.category = category
        self.condition = condition

    def __str__(self):
        string_item = "Hello World!"
        return string_item
    
    def condition_description(self):
        """
        def condition_description() creates key/values of level of \
        condition which will be used in other files
        """
        CONDITION_DICT = {0: "Brand-spanking new!", 
                        1: "New-but really not",
                        2: "Just okay",
                        3: "Not so okay",
                        4: "Don't know what to tell ya",
                        5: "Wouldn't touch with a 10ft pole"}
        condition_value = CONDITION_DICT[self.condition]
        return condition_value

        