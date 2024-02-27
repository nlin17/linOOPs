class OS:
    multitasking = True
    name = "MacOS"

class Apple:
    website = "https://www.apple.com"
    name = "Apple"


class MacBook(Apple, OS):
    def __init__(self):
        if self.multitasking is True:
            print("This is a multitasking system. Visit {} for more details ".format(self.website))

macbook = MacBook()