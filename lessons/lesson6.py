from breezypythongui import EasyFrame

class TipCalculator(EasyFrame):
    """Computes a tip from a bill and a percent."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Tip Calculator")
        # Inputs
        self.addLabel(text = "Bill ($)", row = 0, column = 0)
        self.billField = self.addFloatField(value = 0.0, row = 0,
                                            column = 1, precision = 2)
        self.addLabel(text = "Tip %", row = 1, column = 0)
        self.percentField = self.addIntegerField(value = 20, row = 1,
                                                 column = 1)
        # Button
        self.addButton(text = "Compute", row = 2, column = 0,
                       columnspan = 2, command = self.computeTip)
        # Output (readonly so the user can't type in it)
        self.addLabel(text = "Tip ($)", row = 3, column = 0)
        self.tipField = self.addFloatField(value = 0.0, row = 3,
                                           column = 1, precision = 2,
                                           state = "readonly")

    def computeTip(self):
        """Get inputs, compute, show output."""
        bill = self.billField.getNumber()
        percent = self.percentField.getNumber()
        tip = bill * percent / 100
        self.tipField.setNumber(tip)

def main():
    TipCalculator().mainloop()

if __name__ == "__main__":
    main()
