from breezypythongui import EasyFrame

class RectangleAreaCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Area of Rectangle Calculator",
                           resizable = False)

        # Add labels
        self.addLabel(text = "Enter width:", row = 0, column = 0,
                      sticky = "W")
        self.addLabel(text = "Enter height:", row = 1, column = 0,
                      sticky = "W")
        self.addLabel(text = "Area:", row = 3, column = 0,
                      sticky = "E")

        # Add int fields
        self.widthField = self.addIntegerField(value = 0, row = 0, column = 1,
                                                sticky = "W")
        self.heightField = self.addIntegerField(value = 0, row = 1, column = 1,
                                                sticky = "W")
        self.areaField = self.addIntegerField(value = 0, row = 3, column = 1,
                                           sticky = "E", state = "readonly")

        # Add compute button
        self.calcButton = self.addButton(text = "Compute", row = 2, column = 1,
                                         command = self.calc)

    def calc(self):
        area = self.widthField.getNumber() * self.heightField.getNumber()

        self.areaField.setNumber(area)

def main():
    RectangleAreaCalculator().mainloop()

if __name__ == "__main__":
    main()