class Coffee:
    def __init__(self, sweetness, milk_level):
        self.sweetneess = sweetness
        self.milk_level = milk_level

    def sip(self):
        print("Sipping coffee...")

    def add_suger(self,amount):
        print("added the suger")   


my_coffee=Coffee(sweetness = 3,milk_level=3,)

my_coffee.add_suger(3)
