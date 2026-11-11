from breezypythongui import EasyFrame

class WelcomeWindow(EasyFrame):
    """A window that says hi."""

    def __init__(self):
        """Sets up the window and its label."""
        EasyFrame.__init__(self, title = "This is my own widnow B)",
                           width = 300, height = 100)
        self.addLabel(text = "Hey, it works!", row = 0, column = 0)
        self.addLabel(text = "The names mike yoyoyo", row = 1, column = 0)

def main():
    """Makes the window and pops it up."""
    WelcomeWindow().mainloop()

if __name__ == "__main__":
    main()