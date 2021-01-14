class Targy:
    def __init__(self,a,b):
        self.asztal=a
        self.busz = b

    def __str__(self):
        return "Első: {}, Második: {}".format(self.asztal,self.busz)