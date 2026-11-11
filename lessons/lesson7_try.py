from breezypythongui import EasyFrame

class ScoreKeeper(EasyFrame):
    """Keeps track of score without going into negatives."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Score Keeper", width = 250, height = 100)

        self.score = 0 # score instance var

        self.addLabel(text = "Score:", row = 0, column = 0,
                    sticky = "NSEW")
        self.scoreDisplay = self.addLabel(text = "_", row = 0, column = 1,
                                        columnspan = 2, sticky = "NSW")

        # buttons
        self.additionButton = self.addButton(text = "+1", row = 1, column = 0,
                                        command = self.add)
        self.subtractionButton = self.addButton(text = "-1", row = 1, column = 2,
                                                command = self.minus)
        self.resetButton = self.addButton(text = "Reset", row = 1, column = 1,
                                          command = self.reset)

    # methods
    def replaceText(self):
            self.scoreDisplay["text"] = str(self.score)

    def add(self):
        if self.subtractionButton["state"] == "disabled":
            self.subtractionButton["state"] = "normal"

        self.score += 1
        self.scoreDisplay["text"] = str(self.score)

    def minus(self):
        if self.score > 0:
            self.score -= 1
            self.scoreDisplay["text"] = str(self.score)
        else:            
            self.scoreDisplay["text"] = "Score will be negative!"
            self.subtractionButton["state"] = "disabled"
            self.after(2000, self.replaceText)

    def reset(self):
        self.score = 0
        self.scoreDisplay["text"] = "_"
        


def main():
    ScoreKeeper().mainloop()

if __name__ == "__main__":
    main()