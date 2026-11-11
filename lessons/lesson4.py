from breezypythongui import EasyFrame
from tkinter.font import Font
from tkinter import PhotoImage

class TitleScreen(EasyFrame):
    """A styled title screen."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Title Screen",
                           background = "#1e3a5f")
        self.setResizable(False)
        heading = self.addLabel(text = "LEVEL 1", row = 0, column = 0,
                                sticky = "NSEW",
                                background = "#1e3a5f",
                                foreground = "gold")
        heading["font"] = Font(family = "Courier", size = 28,
                               weight = "bold")
        self.addLabel(text = "press start", row = 1, column = 0,
                      sticky = "NSEW", background = "#1e3a5f",
                      foreground = "white")

class PictureDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Picture")
        self.picLabel = self.addLabel(text = "", row = 0, column = 0)
        # Must be saved in self.something, or the image vanishes!
        self.picture = PhotoImage(file = "smokey.gif")
        self.picLabel["image"] = self.picture

def main():
    check = input("Title Screen(1) or Picture Demo(2): ")
    if int(check) == 1:
        TitleScreen().mainloop()
    elif int(check) == 2:
        PictureDemo().mainloop()
    else:
        print("invalid bru u dum asl")


if __name__ == "__main__":
    main()
