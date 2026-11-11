from breezypythongui import EasyFrame

class LightSwitch(EasyFrame):
    """Two buttons that turn a 'light' on and off."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Light Switch")
        self.status = self.addLabel(text = "The light is OFF",
                                    row = 0, column = 0,
                                    columnspan = 2, sticky = "NSEW")
        self.onButton = self.addButton(text = "On", row = 1,
                                       column = 0,
                                       command = self.turnOn)
        self.offButton = self.addButton(text = "Off", row = 1,
                                        column = 1,
                                        command = self.turnOff,
                                        state = "disabled")

    # Event handlers: these run when the buttons are clicked
    def turnOn(self):
        self.status["text"] = "The light is ON"
        self.onButton["state"] = "disabled"
        self.offButton["state"] = "normal"

    def turnOff(self):
        self.status["text"] = "The light is OFF"
        self.onButton["state"] = "normal"
        self.offButton["state"] = "disabled"

def main():
    LightSwitch().mainloop()

if __name__ == "__main__":
    main()
