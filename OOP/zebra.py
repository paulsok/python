class Zebra:
    def __init__(self, counter=0):
        self.counter = counter
        
    def which_stripe(self):
        if self.counter % 2 == 0:
            print('Полоска белая')
            self.counter += 1   
        else:
            print('Полоска черная')
            self.counter += 1


z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая

