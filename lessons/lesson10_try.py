from breezypythongui import EasyFrame

class SavingsTracker(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Savings tracker")

        # labels
        self.addLabel(text = "Starting amount:", row = 0, column = 0)
        self.addLabel(text = "Weekly deposit:", row = 1, column = 0)
        self.addLabel(text = "# of weeks:", row = 2, column = 0)

        # fields
        self.startAmntField = self.addFloatField(
            value = 0.0, row = 0, column = 1, width = 10, precision = 2,
        )
        self.weekDepositField = self.addFloatField(
            value = 0.0, row = 1, column = 1, width = 10, precision = 2
        )
        self.numWeeksField = self.addIntegerField(
            value = 0, row = 2, column = 1, 
        )

        # text area
        self.savingsArea = self.addTextArea(
            text = "",
            row = 4,
            column = 0,
            columnspan = 2,

        )

        # button
        self.addButton(
            text = "Calculate Savings",
            row = 3,
            column = 0,
            columnspan = 2,
            command = self.calcSavings
        )

    def calcSavings(self):
        startAmnt = self.startAmntField.getNumber()
        weekDeposit = self.weekDepositField.get()
        numWeeks = self.numWeeksField.getNumber()

        result = "%-7s %"

        

def main():
    SavingsTracker().mainloop()

if __name__ == "__main__":
    main()