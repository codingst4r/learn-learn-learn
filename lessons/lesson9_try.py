from breezypythongui import EasyFrame

class SignUpForm(EasyFrame):
    """A form on top, a row of buttons underneath."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Sign Up")

        # Panel 1 (window row 0): a 2-by-2 grid of labels and fields
        formPanel = self.addPanel(row = 0, column = 0)
        formPanel.addLabel(text = "Username", row = 0, column = 0)
        self.userField = formPanel.addTextField(text = "", row = 0,
                                                column = 1)
        formPanel.addLabel(text = "Email", row = 1, column = 0)
        self.emailField = formPanel.addTextField(text = "", row = 1,
                                                 column = 1)

        # Panel 2 (window row 1): a 1-by-3 grid of buttons
        buttonPanel = self.addPanel(row = 1, column = 0)
        buttonPanel.addButton(text = "Submit", row = 0, column = 0,
                              command = self.submit)
        buttonPanel.addButton(text = "Clear", row = 0, column = 1,
                              command = self.clear)
        buttonPanel.addButton(text = "Help", row = 0, column = 2,
                              command = self.help)

        # Panel 3 (window row 2): a 1-by-1 grid of a label
        self.blankPanel = self.addPanel(row = 2, column = 0)
        self.blankLabel = self.blankPanel.addLabel(text = "Fields left blank: 2", row = 0, column = 0,
                             sticky = "EWSN")

    def submit(self):
        userName = self.userField.getText()
        email = self.emailField.getText()
        blankFields = None
        if userName and email:
            blankFields = 0
        elif userName or email:
            blankFields = 1
        elif not userName and not email:
            blankFields = 2

        self.blankLabel["text"] = "Fields left blank: " + str(blankFields)
        

        if blankFields == 0:    
            self.messageBox(title = "Welcome",
                        message = "Signed up as " + userName)

    def clear(self):
        self.userField.setText("")
        self.emailField.setText("")
        self.blankLabel["text"] = "Fields left blank: 2"

    def help(self):
        self.messageBox(title = "Help",
                        message = "Type a username and email, then Submit.")

def main():
    SignUpForm().mainloop()

if __name__ == "__main__":
    main()
