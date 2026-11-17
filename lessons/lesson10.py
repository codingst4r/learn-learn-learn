from breezypythongui import EasyFrame

class TimesTable(EasyFrame):
    """Shows a times table in a text area."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Times Table")
        self.addLabel(text = "Number", row = 0, column = 0)
        self.numberField = self.addIntegerField(value = 7, row = 0,
                                                column = 1)
        self.addButton(text = "Make table", row = 1, column = 0,
                       columnspan = 2, command = self.makeTable)
        self.outputArea = self.addTextArea(text = "", row = 2,
                                           column = 0, columnspan = 2,
                                           width = 30, height = 12)

    def makeTable(self):
        number = self.numberField.getNumber()
        result = "%4s %4s %6s\n" % ("n", "x", "n*x")   # header row
        for x in range(1, 11):
            result += "%4d %4d %6d\n" % (number, x, number * x)
        self.outputArea.setText(result)

def main():
    TimesTable().mainloop()

if __name__ == "__main__":
    main()
