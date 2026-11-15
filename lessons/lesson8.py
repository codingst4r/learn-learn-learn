from breezypythongui import EasyFrame


class SafeTipCalculator(EasyFrame):
    """Tip calculator that handles bad input."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Safe Tip Calculator")
        self.addLabel(text = "Bill ($)", row = 0, column = 0)
        self.billField = self.addFloatField(value = 0.0, row = 0,
                                            column = 1, precision = 2)
        self.addLabel(text = "Tip %", row = 1, column = 0)
        self.percentField = self.addIntegerField(value = 20, row = 1,
                                                 column = 1)
        self.addButton(text = "Compute", row = 2, column = 0,
                       columnspan = 2, command = self.computeTip)
        self.addLabel(text = "Tip ($)", row = 3, column = 0)
        self.tipField = self.addFloatField(value = 0.0, row = 3,
                                           column = 1, precision = 2,
                                           state = "readonly")

    def computeTip(self):
        try:
            bill = self.billField.getNumber()
            percent = self.percentField.getNumber()
            self.tipField.setNumber(bill * percent / 100)
        except ValueError:
            self.messageBox(title = "Oops",
                            message = "Bill and Tip % have to be numbers.")


def main():
    SafeTipCalculator().mainloop()


if __name__ == "__main__":
    main()
