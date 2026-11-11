from breezypythongui import EasyFrame

class TriColorLabels(EasyFrame):
    """3 different colored labels stacked on each other"""

    def __init__(self):
        bgCol = "#000000"

        EasyFrame.__init__(self, title = "3 Different Labels yo",
                           background = bgCol, resizable = False)

        # Red Label
        self.addLabel(text = "RED", row = 0, column = 0, 
                      sticky = "NEW", background = bgCol, foreground = "#ff0000")

        # White Label
        self.addLabel(text = "WHITE", row = 1, column = 0,
                      sticky = "NSEW", background = bgCol, foreground = "#ffffff")

        # Blue Label
        self.addLabel(text = "BLUE", row = 2, column = 0,
                      sticky = "SEW", background = bgCol, foreground = "#0000ff")

def main():
    TriColorLabels().mainloop()

if __name__ == "__main__":
    main()