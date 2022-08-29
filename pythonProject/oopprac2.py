# Multilevel inheritance

# Ex1 . Make 3 classes named as electronic_gadgets, pocket_gadgets, phone and show multilevel
# inheritance and some meaningful attributes and methods

class Electronic_gadgets:
    def __init__(self, name, model):
        self.gadget_name = name
        self.model_name = model

    @staticmethod
    def print_details():
        return f"the details of the gadget "


class Pocket_gadgets(Electronic_gadgets):
    def __init__(self, name, model):
        self.gadget_name = name
        self.model_name = model


class phone(Electronic_gadgets, Pocket_gadgets):
    pass


Gadget = Phone("mixer", 1995)

# It's incomplete...
