class Tree:
    manufacturer = "Ireland"
    contactWebsite = "https://www.rentaboyfriend.com/contact"

    def contactDetails(self):
        print("to contact us, go to ", self.contactWebsite)

class Redwood(Tree):
    def __init__(self):
        self.year = 2007

    def manufacturerDetails(self):
        print("this tree was manufactured in the year {} by {}".format(self.year, self.manufacturer))

teddy = Redwood()
teddy.manufacturerDetails()
teddy.contactDetails()