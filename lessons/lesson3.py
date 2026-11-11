from breezypythongui import EasyFrame

class GridDemo(EasyFrame):
    """Shows rows, columns, sticky and columnspan."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Grid Demo")
        self.addLabel(text = "top left (0, 0)", row = 0, column = 0,
                      sticky = "NSEW")
        self.addLabel(text = "top right (0, 1)", row = 0, column = 1,
                      sticky = "NSEW")
        self.addLabel(text = "I take up the whole bottom row",
                      row = 1, column = 0, columnspan = 2,
                      sticky = "NSEW")

def main():
    GridDemo().mainloop()

if __name__ == "__main__":
    main()
