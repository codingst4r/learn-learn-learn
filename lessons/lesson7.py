from breezypythongui import EasyFrame

class ClickCounter(EasyFrame):
    """Counts clicks."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Clicker", width = 240,
                           height = 100)
        self.clicks = 0     # instance variable: remembered between clicks
        self.display = self.addLabel(text = "0", row = 0, column = 0,
                                     columnspan = 2, sticky = "NSEW")
        self.addButton(text = "Click me", row = 1, column = 0,
                       command = self.click)
        self.addButton(text = "Reset", row = 1, column = 1,
                       command = self.reset)

    def click(self):
        self.clicks += 1
        message = str(self.clicks)  # temporary: gone after this method
        if self.clicks >= 10:
            message += "  (you hit 10!)"
        self.display["text"] = message

    def reset(self):
        self.clicks = 0
        self.display["text"] = "0"

"""class newClass():
    def newMethod(self):
        print(self)"""

def main():
    ClickCounter().mainloop()

if __name__ == "__main__":
    main()