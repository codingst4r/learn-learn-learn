from breezypythongui import EasyFrame

class seatMaker(EasyFrame):
    """Shows rows, columns, sticky and columnspan."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Seat Maker")

        seatNum = 0
        for x in range(3):
            for y in range(4):
                seatNum += 1
                self.addLabel(text = "Seat " + str(seatNum), row = x, column = y,
                              sticky = "NSEW")

def main():
    seatMaker().mainloop()

if __name__ == "__main__":
    main()
