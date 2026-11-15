from breezypythongui import EasyFrame

class EnterKeyDemo(EasyFrame):
    """Press Enter in the box to shout it."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Enter Key Demo")
        self.addLabel(text = "Type, then press Enter", row = 0,
                      column = 0)
        self.inputField = self.addTextField(text = "", row = 1,
                                            column = 0)
        self.inputField.bind("<Return>", lambda event: self.shout())
        self.output = self.addLabel(text = "", row = 2, column = 0)

    def shout(self):
        self.output["text"] = self.inputField.getText().upper() + "!!!"

def main():
    EnterKeyDemo().mainloop()

if __name__ == "__main__":
    main()
