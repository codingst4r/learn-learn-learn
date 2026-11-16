from breezypythongui import EasyFrame


class RectangleAreaCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Area of Rectangle Calculator",
                           resizable = False)

        # Add labels
        self.addLabel(text = "Enter width:", row = 0, column = 0,
                      sticky = "W")
        self.addLabel(text = "Enter height:", row = 1, column = 0,
                      sticky = "W")
        self.addLabel(text = "Area:", row = 3, column = 0,
                      sticky = "E")

        # Add int fields
        self.widthField = self.addIntegerField(value = 0, row = 0, column = 1,
                                               sticky = "W")
        self.heightField = self.addIntegerField(value = 0, row = 1, column = 1,
                                                sticky = "W")
        self.areaField = self.addIntegerField(value = 0, row = 3, column = 1,
                                              sticky = "E", state = "readonly")

        # Add compute button
        self.calcButton = self.addButton(text = "Compute", row = 2, column = 1,
                                         command = self.calc)

        # Binds
        self.widthField.bind("<Return>", lambda event: self.calc())
        self.heightField.bind("<Return>", lambda event: self.calc())

    def errorHandler(self, wVal, hVal):
        widthError = False
        heightError = False

        # test and catch the errors, if error: indicate which field caused it
        try:
            width = self.widthField.getNumber()
        except ValueError:
            widthError = 'Invalid input, "' + wVal + '", in the Width Field!'
        try:
            height = self.heightField.getNumber()
        except ValueError:
            heightError = 'Invalid input, "' + hVal + '", in the Height Field!'

        # if no error, calculate area and set areaField
        if not widthError and not heightError:
            area = width * height
            return area

        # if there's an error(s), check how/where it happened, and show the error(s)
        if widthError and not heightError:
            errMsg = widthError + "\n\nInput only whole numbers (integers)!"

        elif heightError and not widthError:
            errMsg = heightError + "\n\nInput only whole numbers (integers)!"

        elif widthError and heightError:
            errMsg = 'Invalid inputs, "' + wVal + '" and "' + hVal + \
                '", in Width Field and Height Field respectively.\n\nInput only whole numbers (integers)!'

        hgt = 3
        if len(errMsg) // 50 >= 3:
            hgt = len(errMsg) // 50 + 1
            
        self.messageBox(title = "Invalid Input",
                        message = errMsg,
                        width = 50,
                        height = hgt + 1)

    def calc(self):
        wVal = self.widthField.getValue()
        hVal = self.heightField.getValue()

        area = self.errorHandler(wVal, hVal)
        if area is not None:
            self.areaField.setNumber(area)


def main():
    RectangleAreaCalculator().mainloop()


if __name__ == "__main__":
    main()
