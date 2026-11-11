from breezypythongui import EasyFrame
import random

class CoinFlip(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Coin Flipper",
                           resizable = False)

        self.coinLabel = self.addLabel(text = "Your coin landed on...", row = 0, column = 0,
                                       columnspan = 2, sticky = "NEW")
        self.coinPosition = self.addLabel(text = "", row = 1, column = 0,
                                          columnspan = 2, sticky = "NSEW")

        self.flipButton = self.addButton(text = "Flip!", row = 2, column = 0, 
                                         command = self.flip)
        self.resetButton = self.addButton(text = "Reset", row = 2, column = 1,
                                          command = self.reset)

    def flip(self):
        status = random.randint(1, 2)

        if status == 1:
            self.coinPosition["text"] = "Heads!"
        else:
            self.coinPosition["text"] = "Tails!"

    def reset(self):
        self.coinPosition["text"] = ""


def main():
    CoinFlip().mainloop()

if __name__ == "__main__":
    main()