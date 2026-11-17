from breezypythongui import EasyFrame

class PizzaOrder(EasyFrame):
    """Radio buttons for size, check buttons for toppings."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Pizza Order")
        # Size: pick exactly one
        self.addLabel(text = "Size", row = 0, column = 0)
        self.sizeGroup = self.addRadiobuttonGroup(row = 1, column = 0,
                                                  rowspan = 3)
        small = self.sizeGroup.addRadiobutton(text = "Small")
        self.sizeGroup.addRadiobutton(text = "Medium")
        self.sizeGroup.addRadiobutton(text = "Large")
        self.sizeGroup.setSelectedButton(small)
        # Toppings: pick any
        self.addLabel(text = "Toppings ($1.50 each)", row = 0, column = 1)
        self.cheeseCB = self.addCheckbutton(text = "Extra cheese",
                                            row = 1, column = 1)
        self.pepCB = self.addCheckbutton(text = "Pepperoni",
                                         row = 2, column = 1)
        self.mushCB = self.addCheckbutton(text = "Mushrooms",
                                          row = 3, column = 1)
        self.addButton(text = "Order", row = 4, column = 0,
                       columnspan = 2, command = self.order)

    def order(self):
        size = self.sizeGroup.getSelectedButton()["text"]
        if size == "Small":
            price = 8.00
        elif size == "Medium":
            price = 10.00
        else:
            price = 12.00
        for box in [self.cheeseCB, self.pepCB, self.mushCB]:
            if box.isChecked():
                price += 1.50
        self.messageBox(title = "Your order",
                        message = size + " pizza: $%.2f" % price)

def main():
    PizzaOrder().mainloop()

if __name__ == "__main__":
    main()
