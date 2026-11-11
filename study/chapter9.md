# Chapter 9: GUIs

_Graphical User Interfaces with breezypythongui_

> **Reading this in VS Code:** press `Ctrl+K` then `V` to open the preview next to your code (or `Ctrl+Shift+V` for a full tab). Click **Hint**, **One way to do it** and **Answer** to open them. The same guide with clickable quizzes and a progress bar is online: https://claude.ai/artifact/APHNZk4AFdUey7iubt5ayx

## How to use this

<p>This chapter is about making programs with <b>windows, buttons and boxes</b> instead of a terminal. The book uses a helper module called <code>breezypythongui</code> that makes this way easier than raw tkinter.</p>
<p>The good news: <b>every GUI program in this chapter has the same skeleton.</b> Once that skeleton clicks, each new lesson is just "here's one more kind of widget."</p>

- **One lesson at a time.** Most take 10 to 15 minutes. Busy day? One lesson still counts.
- **Run every example yourself** and change things. Break it on purpose and read the error.
- **Do the Try it before peeking** at the answer. Getting stuck for a few minutes is where the learning happens.
- Working on a graded exercise? Jump to the [exercise map](#exercise-map) to see which lessons it uses, or ask Claude Code `/lesson` with the exercise number.
- When you finish a lesson, check it off in `study/progress.md` (or let `/leftoff` do it).

## Setup

<p><b>In your Cengage Codespace you're already set.</b> Every Chapter 9 exercise's <code>student</code> folder comes with <code>breezypythongui.py</code> (version 1.2), so the import just works.</p>
<p><b>Seeing your window:</b> run the program, then click <b>Open GUI</b> in the Cengage sidebar, click <b>Connect</b>, and enter the password <code>vscode</code>. Close your program's window before running it again, or your changes won't show up.</p>
<p><b>Running the examples somewhere else</b> (like on Starlight without the Codespace): copy <code>breezypythongui.py</code> from any Chapter 9 <code>student</code> folder into the same folder as the example. Avoid the pip version: when I tested it, its radio buttons crash with <code>AttributeError: 'str' object has no attribute '_root'</code>. Your Cengage copy doesn't have that bug.</p>

## The skeleton every GUI program follows

<ol><li>Make a class that <b>extends EasyFrame</b>. That class <i>is</i> your window.</li><li>In <code>__init__</code>, add your widgets (labels, fields, buttons) to the window's <b>grid</b>.</li><li>Give each button <code>command = self.someMethod</code> so it knows what to run when clicked.</li><li>Write those methods. They almost always go: <b>read the inputs &rarr; do the math &rarr; show the output.</b></li><li>A <code>main()</code> function makes the window and calls <code>mainloop()</code>.</li></ol>

> Pro move from the book: build the layout first with no button logic, run it, and make sure it looks right. Then add the methods.

## Lessons

1. [Terminal vs. GUI: who's in charge?](#lesson-1-terminal-vs-gui-whos-in-charge) · about 5 min
2. [Your first window](#lesson-2-your-first-window) · about 10 min
3. [The grid: putting things where you want](#lesson-3-the-grid-putting-things-where-you-want) · about 10 min
4. [Making it look right: colors, fonts, images](#lesson-4-making-it-look-right-colors-fonts-images) · about 10 min
5. [Buttons and event handlers](#lesson-5-buttons-and-event-handlers) · about 15 min
6. [Input and output with entry fields](#lesson-6-input-and-output-with-entry-fields) · about 15 min
7. [Instance variables: how the window remembers stuff](#lesson-7-instance-variables-how-the-window-remembers-stuff) · about 10 min
8. [Bad input? Don't crash, pop up a message](#lesson-8-bad-input-dont-crash-pop-up-a-message) · about 10 min
9. [Panels: grids inside your grid](#lesson-9-panels-grids-inside-your-grid) · about 10 min
10. [Text areas: lots of lines of output](#lesson-10-text-areas-lots-of-lines-of-output) · about 15 min
11. [Pop-ups and file dialogs](#lesson-11-pop-ups-and-file-dialogs) · about 15 min
12. [Check buttons and radio buttons](#lesson-12-check-buttons-and-radio-buttons) · about 15 min
13. [Keyboard events: pressing Enter](#lesson-13-keyboard-events-pressing-enter) · about 5 min

→ [Exercise map](#exercise-map)

---

## Lesson 1: Terminal vs. GUI: who's in charge?

_About 5 minutes_

#### The idea

<p>A terminal program is in charge. It asks question 1, waits, asks question 2, waits, prints the answer, done. You can't go back and change question 1.</p>
<p>A GUI program flips that. It opens a window and then just <b>sits there waiting</b> for you to do something: type in a box, click a button. Each click is an <b>event</b>, and the program runs a method in response. This is called <b>event-driven programming</b>.</p>
<p>Think of a terminal program like a cashier asking you questions in order, and a GUI like a vending machine that does nothing until you press something.</p>
<p>That's why GUI code doesn't have a big <code>while</code> loop asking for input. The window's <code>mainloop()</code> is the loop. It runs behind the scenes, waiting for clicks.</p>

#### Quick check

**In a GUI program, what makes your code run after the window opens?**

- a) A while loop you write that keeps calling input()
- b) The user doing something, like clicking a button, which triggers a method
- c) Python runs every method in the class from top to bottom

<details>
<summary>Answer</summary>

**b) The user doing something, like clicking a button, which triggers a method**

GUIs are event-driven: mainloop() waits, and a click (an event) runs the method connected to that button.

</details>

#### Watch out for

- Don't use `input()` or `print()` for the user in a GUI program. Input comes from fields, output goes to labels or fields.

---

## Lesson 2: Your first window

_About 10 minutes_

#### The idea

<p>Here's the smallest real GUI program. Read the comments, then run it.</p>
<ul>
<li><code>class WelcomeWindow(EasyFrame)</code> means "my window is a kind of EasyFrame." That's <b>subclassing</b>: you get all of EasyFrame's window powers for free and just add your own stuff.</li>
<li><code>EasyFrame.__init__(self, ...)</code> lets EasyFrame set up the basic window first. Always do this as the first line of your <code>__init__</code>.</li>
<li><code>self</code> is the window itself. <code>self.addLabel(...)</code> means "add a label to <i>this</i> window."</li>
</ul>

#### See it, then run it

```python
from breezypythongui import EasyFrame

class WelcomeWindow(EasyFrame):
    """A window that says hi."""

    def __init__(self):
        """Sets up the window and its label."""
        EasyFrame.__init__(self, title = "My First GUI",
                           width = 300, height = 100)
        self.addLabel(text = "Hey, it works!", row = 0, column = 0)

def main():
    """Makes the window and pops it up."""
    WelcomeWindow().mainloop()

if __name__ == "__main__":
    main()
```

> The last five lines are the same in basically every GUI program. Copy them and just change the class name.

#### Try it yourself

Add a second label under the first one (row 1) that shows your name. Then change the window title to anything you want.

<details>
<summary>Hint</summary>

Copy the `self.addLabel(...)` line and change `row = 0` to `row = 1`.

</details>

<details>
<summary>One way to do it (try first!)</summary>

```python
from breezypythongui import EasyFrame

class WelcomeWindow(EasyFrame):
    """A window that says hi."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Mike's Window",
                           width = 300, height = 100)
        self.addLabel(text = "Hey, it works!", row = 0, column = 0)
        self.addLabel(text = "Made by Mike", row = 1, column = 0)

def main():
    WelcomeWindow().mainloop()

if __name__ == "__main__":
    main()
```

</details>

#### Quick check

**Why does the class say WelcomeWindow(EasyFrame)?**

- a) So WelcomeWindow gets all of EasyFrame's window features and adds its own
- b) It's calling a function named EasyFrame
- c) It makes WelcomeWindow run faster

<details>
<summary>Answer</summary>

**a) So WelcomeWindow gets all of EasyFrame's window features and adds its own**

That's subclassing and inheritance: WelcomeWindow inherits everything EasyFrame can do, then customizes it.

</details>

#### Watch out for

- Forgetting `EasyFrame.__init__(self, ...)` at the top of `__init__`. Without it, the window never gets set up properly.
- Forgetting `self` as the first parameter of a method: `def __init__(self):`
- Typing `_init_` with one underscore. It needs two on each side: `__init__`.

---

## Lesson 3: The grid: putting things where you want

_About 10 minutes_

#### The idea

<p>Every window is an invisible table of rows and columns. You place each widget with <code>row</code> and <code>column</code>. <b>Counting starts at 0</b>, so the top-left spot is <code>(0, 0)</code>.</p>
<ul>
<li><code>sticky</code> controls where a widget sits inside its cell. Use compass letters: <code>"N"</code>, <code>"S"</code>, <code>"E"</code>, <code>"W"</code>. <code>"NSEW"</code> centers it and lets it stretch.</li>
<li><code>columnspan = 2</code> makes a widget take up 2 columns, like merging cells in Excel. It only centers across them if it's also <code>sticky = "NSEW"</code>.</li>
</ul>
<p>Labels hug the top-left (northwest) by default. Buttons are centered by default.</p>

#### See it, then run it

```python
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
```

> Run it, then drag the window corner to make it bigger. Watch how the labels stay centered because of NSEW.

#### Try it yourself

Use a <b>nested for loop</b> to make 3 rows and 4 columns of labels that say Seat 1, Seat 2, ... Seat 12, going left to right.

<details>
<summary>Hint</summary>

Outer loop over rows, inner loop over columns. Keep a counter variable that you add 1 to each time you make a label, and use `"Seat " + str(counter)` for the text.

</details>

<details>
<summary>One way to do it (try first!)</summary>

```python
from breezypythongui import EasyFrame

class Seats(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Seating Chart")
        seatNumber = 1
        for row in range(3):
            for column in range(4):
                self.addLabel(text = "Seat " + str(seatNumber),
                              row = row, column = column,
                              sticky = "NSEW")
                seatNumber += 1

def main():
    Seats().mainloop()

if __name__ == "__main__":
    main()
```

</details>

#### Quick check

**A label at row = 1, column = 0 shows up where?**

- a) First row, second column
- b) Second row, first column
- c) Second row, second column

<details>
<summary>Answer</summary>

**b) Second row, first column**

Rows and columns count from 0. Row 1 is the second row, column 0 is the first column.

</details>

#### Watch out for

- Putting two widgets in the same row and column. The second one covers the first.
- Using `columnspan` without `sticky = "NSEW"` and wondering why it isn't centered.

---

## Lesson 4: Making it look right: colors, fonts, images

_About 10 minutes_

#### The idea

<p>You can change how the window and widgets look in three ways:</p>
<ul>
<li><b>When you create them:</b> <code>EasyFrame.__init__(self, title = "...", background = "black")</code> or <code>self.addLabel(..., foreground = "gold")</code></li>
<li><b>With EasyFrame methods:</b> <code>self.setSize(400, 200)</code>, <code>self.setResizable(False)</code>, <code>self.setTitle("New title")</code>, <code>self.setBackground("navy")</code></li>
<li><b>Like a dictionary, later:</b> <code>myLabel["foreground"] = "red"</code>. Every widget keeps its settings in a dictionary you can change anytime.</li>
</ul>
<p><b>Colors</b> can be names like <code>"red"</code> or <b>hex strings</b> like <code>"#1e3a5f"</code>. That's <code>#RRGGBB</code>: two hex digits each for red, green, blue (00 is none, ff is max).</p>
<p><b>Fonts</b> use a <code>Font</code> object from <code>tkinter.font</code>. <b>Images</b> use a <code>PhotoImage</code> from <code>tkinter</code>. The book uses GIF files for these.</p>

#### See it, then run it

```python
from breezypythongui import EasyFrame
from tkinter.font import Font

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

def main():
    TitleScreen().mainloop()

if __name__ == "__main__":
    main()
```

> Notice heading = self.addLabel(...). Every add method returns the widget, so you can keep it in a variable and change it after.

#### Showing an image

```python
from breezypythongui import EasyFrame
from tkinter import PhotoImage

class PictureDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Picture")
        self.picLabel = self.addLabel(text = "", row = 0, column = 0)
        # Must be saved in self.something, or the image vanishes!
        self.picture = PhotoImage(file = "cat.gif")
        self.picLabel["image"] = self.picture

def main():
    PictureDemo().mainloop()

if __name__ == "__main__":
    main()
```

> Put a GIF named cat.gif in the same folder as the program, or change the file name.

#### Try it yourself

Make a window with three labels stacked vertically that say RED, WHITE, BLUE, each in its own color, on a black background. Make the window not resizable.

<details>
<summary>Hint</summary>

Give each label `foreground = "red"` (and so on) and `background = "black"`. The window's background goes in `EasyFrame.__init__`.

</details>

<details>
<summary>One way to do it (try first!)</summary>

```python
from breezypythongui import EasyFrame

class Colors(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Colors", background = "black")
        self.setResizable(False)
        names = ["red", "white", "blue"]
        for row in range(3):
            self.addLabel(text = names[row].upper(), row = row,
                          column = 0, sticky = "NSEW",
                          background = "black",
                          foreground = names[row])

def main():
    Colors().mainloop()

if __name__ == "__main__":
    main()
```

</details>

#### Quick check

**Why does the image example save the picture as self.picture instead of just picture?**

- a) self makes the image load faster
- b) A plain variable disappears when `__init__` ends, and then the image disappears from the window too
- c) PhotoImage only works with names that start with self

<details>
<summary>Answer</summary>

**b) A plain variable disappears when `__init__` ends, and then the image disappears from the window too**

A temporary variable dies when the method ends. Saving it on self keeps it alive as long as the window exists.

</details>

#### Watch out for

- Image shows up blank? You probably stored the PhotoImage in a temporary variable instead of `self.something`.
- Hex colors need the `#` and exactly 6 digits: `"#ff0000"`, not `"ff0000"`.

---

## Lesson 5: Buttons and event handlers

_About 15 minutes_

#### The idea

<p>This is where GUIs come alive. A button does nothing until you connect it to a method with <code>command</code>:</p>
<p><code>self.addButton(text = "On", row = 1, column = 0, command = self.turnOn)</code></p>
<p>Now when someone clicks it, Python runs <code>self.turnOn()</code> for you. A method connected like this is called an <b>event handler</b>.</p>
<p><b>No parentheses after the method name!</b> <code>command = self.turnOn</code> means "here's the method, run it later." <code>command = self.turnOn()</code> would run it right now, once, while the window is being built.</p>
<p>Buttons also have a <code>state</code>: <code>"normal"</code> (clickable) or <code>"disabled"</code> (grayed out). To change a label's text later: <code>self.myLabel["text"] = "new text"</code>.</p>

#### See it, then run it

```python
from breezypythongui import EasyFrame

class LightSwitch(EasyFrame):
    """Two buttons that turn a 'light' on and off."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Light Switch")
        self.status = self.addLabel(text = "The light is OFF",
                                    row = 0, column = 0,
                                    columnspan = 2, sticky = "NSEW")
        self.onButton = self.addButton(text = "On", row = 1,
                                       column = 0,
                                       command = self.turnOn)
        self.offButton = self.addButton(text = "Off", row = 1,
                                        column = 1,
                                        command = self.turnOff,
                                        state = "disabled")

    # Event handlers: these run when the buttons are clicked
    def turnOn(self):
        self.status["text"] = "The light is ON"
        self.onButton["state"] = "disabled"
        self.offButton["state"] = "normal"

    def turnOff(self):
        self.status["text"] = "The light is OFF"
        self.onButton["state"] = "normal"
        self.offButton["state"] = "disabled"

def main():
    LightSwitch().mainloop()

if __name__ == "__main__":
    main()
```

> The label and buttons are saved as self.status, self.onButton, etc. because the handler methods need to reach them later.

#### Try it yourself

Make a coin flip window: one label and one Flip button. Each click shows Heads or Tails at random.

<details>
<summary>Hint</summary>

`import random` at the top, then in your handler use `random.choice(["Heads", "Tails"])` and put the result in the label's `"text"`.

</details>

<details>
<summary>One way to do it (try first!)</summary>

```python
import random
from breezypythongui import EasyFrame

class CoinFlip(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Coin Flip", width = 200,
                           height = 100)
        self.result = self.addLabel(text = "Click Flip", row = 0,
                                    column = 0, sticky = "NSEW")
        self.addButton(text = "Flip", row = 1, column = 0,
                       command = self.flip)

    def flip(self):
        self.result["text"] = random.choice(["Heads", "Tails"])

def main():
    CoinFlip().mainloop()

if __name__ == "__main__":
    main()
```

</details>

#### Quick check

**Which line connects a button to a method correctly?**

- a) command = self.flip()
- b) command = self.flip
- c) command = flip

<details>
<summary>Answer</summary>

**b) command = self.flip**

You hand over the method itself (no parentheses) so Python can call it later when the button is clicked. And it needs self. because flip lives in your class.

</details>

#### Watch out for

- `command = self.flip()` with parentheses: the method runs once at startup and the button does nothing after.
- Handler can't find a widget? Save it as `self.something` in `__init__`, not as a plain variable.
- Event handler methods take only `self`: `def flip(self):`

---

## Lesson 6: Input and output with entry fields

_About 15 minutes_

#### The idea

<p>Entry fields are the boxes people type in. You'll use these constantly:</p>
<div class="table-wrap"><table>
<tr><th>Field</th><th>Add it with</th><th>Read it</th><th>Write to it</th></tr>
<tr><td>Text</td><td><code>addTextField(text = "", ...)</code></td><td><code>.getText()</code></td><td><code>.setText("hi")</code></td></tr>
<tr><td>Whole numbers</td><td><code>addIntegerField(value = 0, ...)</code></td><td><code>.getNumber()</code></td><td><code>.setNumber(5)</code></td></tr>
<tr><td>Decimals</td><td><code>addFloatField(value = 0.0, ...)</code></td><td><code>.getNumber()</code></td><td><code>.setNumber(2.5)</code></td></tr>
</table></div>
<p>Use the number fields for numbers. They convert for you, so no <code>int()</code> or <code>float()</code> needed.</p>
<ul>
<li><code>precision = 2</code> on a FloatField shows 2 decimal places (great for money).</li>
<li><code>state = "readonly"</code> on an output field stops the user from typing in it. Your code can still <code>setNumber</code> it.</li>
</ul>
<p>Almost every handler you write in this chapter looks like: <b>get the inputs, compute, set the output.</b></p>

#### See it, then run it

```python
from breezypythongui import EasyFrame

class TipCalculator(EasyFrame):
    """Computes a tip from a bill and a percent."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Tip Calculator")
        # Inputs
        self.addLabel(text = "Bill ($)", row = 0, column = 0)
        self.billField = self.addFloatField(value = 0.0, row = 0,
                                            column = 1, precision = 2)
        self.addLabel(text = "Tip %", row = 1, column = 0)
        self.percentField = self.addIntegerField(value = 20, row = 1,
                                                 column = 1)
        # Button
        self.addButton(text = "Compute", row = 2, column = 0,
                       columnspan = 2, command = self.computeTip)
        # Output (readonly so the user can't type in it)
        self.addLabel(text = "Tip ($)", row = 3, column = 0)
        self.tipField = self.addFloatField(value = 0.0, row = 3,
                                           column = 1, precision = 2,
                                           state = "readonly")

    def computeTip(self):
        """Get inputs, compute, show output."""
        bill = self.billField.getNumber()
        percent = self.percentField.getNumber()
        tip = bill * percent / 100
        self.tipField.setNumber(tip)

def main():
    TipCalculator().mainloop()

if __name__ == "__main__":
    main()
```

> Look at how little code is in computeTip. Most of a GUI program is setting up widgets. The actual logic is usually just a few lines.

#### Try it yourself

Make a rectangle area calculator: two IntegerFields (width and height), a Compute button, and a readonly IntegerField that shows the area.

<details>
<summary>Hint</summary>

Copy the tip calculator and change it. In your handler: get width, get height, multiply, `setNumber` the result.

</details>

<details>
<summary>One way to do it (try first!)</summary>

```python
from breezypythongui import EasyFrame

class AreaCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Area")
        self.addLabel(text = "Width", row = 0, column = 0)
        self.widthField = self.addIntegerField(value = 0, row = 0,
                                               column = 1)
        self.addLabel(text = "Height", row = 1, column = 0)
        self.heightField = self.addIntegerField(value = 0, row = 1,
                                                column = 1)
        self.addButton(text = "Compute", row = 2, column = 0,
                       columnspan = 2, command = self.computeArea)
        self.addLabel(text = "Area", row = 3, column = 0)
        self.areaField = self.addIntegerField(value = 0, row = 3,
                                              column = 1,
                                              state = "readonly")

    def computeArea(self):
        width = self.widthField.getNumber()
        height = self.heightField.getNumber()
        self.areaField.setNumber(width * height)

def main():
    AreaCalculator().mainloop()

if __name__ == "__main__":
    main()
```

</details>

#### Quick check

**Your FloatField shows 12.500000 but you want 12.50. What's the fix?**

- a) Use round() before setNumber
- b) Add precision = 2 when you create the field
- c) Switch to an IntegerField

<details>
<summary>Answer</summary>

**b) Add precision = 2 when you create the field**

precision controls how many decimal places a FloatField displays.

</details>

#### Watch out for

- IntegerField fields use `value =`, TextFields use `text =`. Mixing them up gives an error.
- Typing `3.5` into an IntegerField crashes `getNumber()` with a ValueError. Lesson 8 shows how to handle that.
- Calling `getNumber()` on the label instead of the field. Read from the <b>field</b> variable.

---

## Lesson 7: Instance variables: how the window remembers stuff

_About 10 minutes_

#### The idea

<p>Variables inside a method normally vanish the second the method ends. So how does a counter remember its count between clicks?</p>
<p><b>Instance variables.</b> Anything you save as <code>self.something</code> belongs to the window object and sticks around as long as the window does. Every method in the class can see it.</p>
<ul>
<li><b>Instance variable</b> (<code>self.clicks</code>): set it up in <code>__init__</code>, use and change it in any method. Like stuff in your backpack, it comes with you everywhere.</li>
<li><b>Temporary variable</b> (<code>message</code>): only exists inside one method, then it's gone. Like notes on a napkin.</li>
</ul>
<p>Rule of thumb from the book: only make something an instance variable if the window needs to <b>remember it between method calls</b>. Otherwise use a temporary.</p>

#### See it, then run it

```python
from breezypythongui import EasyFrame

class ClickCounter(EasyFrame):
    """Counts clicks."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Clicker", width = 240,
                           height = 100)
        self.clicks = 0     # instance variable: remembered between clicks
        self.display = self.addLabel(text = "0", row = 0, column = 0,
                                     columnspan = 2, sticky = "NSEW")
        self.addButton(text = "Click me", row = 1, column = 0,
                       command = self.click)
        self.addButton(text = "Reset", row = 1, column = 1,
                       command = self.reset)

    def click(self):
        self.clicks += 1
        message = str(self.clicks)  # temporary: gone after this method
        if self.clicks >= 10:
            message += "  (you hit 10!)"
        self.display["text"] = message

    def reset(self):
        self.clicks = 0
        self.display["text"] = "0"

def main():
    ClickCounter().mainloop()

if __name__ == "__main__":
    main()
```

#### Try it yourself

Make a score keeper: a label showing the score and three buttons: +1, -1, Reset. When the score is 0, the -1 button should be disabled so the score never goes negative.

<details>
<summary>Hint</summary>

Keep `self.score` in `__init__`. Save the -1 button as `self.minusButton`. After every change, check: if the score is 0, set its `"state"` to `"disabled"`, otherwise `"normal"`.

</details>

<details>
<summary>One way to do it (try first!)</summary>

```python
from breezypythongui import EasyFrame

class ScoreKeeper(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Score")
        self.score = 0
        self.display = self.addLabel(text = "0", row = 0, column = 0,
                                     columnspan = 3, sticky = "NSEW")
        self.addButton(text = "+1", row = 1, column = 0,
                       command = self.plusOne)
        self.minusButton = self.addButton(text = "-1", row = 1,
                                          column = 1,
                                          command = self.minusOne,
                                          state = "disabled")
        self.addButton(text = "Reset", row = 1, column = 2,
                       command = self.reset)

    def update(self):
        """Helper: shows the score and fixes the -1 button."""
        self.display["text"] = str(self.score)
        if self.score == 0:
            self.minusButton["state"] = "disabled"
        else:
            self.minusButton["state"] = "normal"

    def plusOne(self):
        self.score += 1
        self.update()

    def minusOne(self):
        self.score -= 1
        self.update()

    def reset(self):
        self.score = 0
        self.update()

def main():
    ScoreKeeper().mainloop()

if __name__ == "__main__":
    main()
```

</details>

#### Quick check

**In ClickCounter, why is clicks saved as self.clicks instead of just clicks?**

- a) So its value survives between clicks and every method can use it
- b) Because numbers always need self
- c) So it shows up on the screen automatically

<details>
<summary>Answer</summary>

**a) So its value survives between clicks and every method can use it**

A plain variable would reset every time click() runs. self.clicks lives as long as the window.

</details>

#### Watch out for

- Creating the instance variable inside a handler instead of `__init__`. If another method uses it before that handler runs, you get an AttributeError.
- Writing `clicks += 1` without `self.` gives an error, because that's a different, local variable that doesn't exist yet.

---

## Lesson 8: Bad input? Don't crash, pop up a message

_About 10 minutes_

#### The idea

<p>If someone types <code>abc</code> into a number field, <code>getNumber()</code> raises a <code>ValueError</code>. In a GUI the window survives, but nothing happens and an ugly error prints in the terminal.</p>
<p>The fix is <code>try</code> / <code>except</code>. Python <b>tries</b> the risky code. If an error happens anywhere in the <code>try</code> part, it jumps straight to <code>except</code> instead of crashing.</p>
<p>Pair it with <code>self.messageBox(title = "...", message = "...")</code> to pop up a little window explaining what went wrong. When they close it, they can fix the input and try again. No loop needed, because the window is still waiting for events.</p>

#### See it, then run it

```python
from breezypythongui import EasyFrame

class SafeTipCalculator(EasyFrame):
    """Tip calculator that handles bad input."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Safe Tip Calculator")
        self.addLabel(text = "Bill ($)", row = 0, column = 0)
        self.billField = self.addFloatField(value = 0.0, row = 0,
                                            column = 1, precision = 2)
        self.addLabel(text = "Tip %", row = 1, column = 0)
        self.percentField = self.addIntegerField(value = 20, row = 1,
                                                 column = 1)
        self.addButton(text = "Compute", row = 2, column = 0,
                       columnspan = 2, command = self.computeTip)
        self.addLabel(text = "Tip ($)", row = 3, column = 0)
        self.tipField = self.addFloatField(value = 0.0, row = 3,
                                           column = 1, precision = 2,
                                           state = "readonly")

    def computeTip(self):
        try:
            bill = self.billField.getNumber()
            percent = self.percentField.getNumber()
            self.tipField.setNumber(bill * percent / 100)
        except ValueError:
            self.messageBox(title = "Oops",
                            message = "Bill and Tip % have to be numbers.")

def main():
    SafeTipCalculator().mainloop()

if __name__ == "__main__":
    main()
```

> Run it and type letters into the Bill box, then click Compute.

#### Try it yourself

Add try/except to your area calculator from Lesson 6 so letters (or decimals) in the boxes pop up a message instead of doing nothing.

<details>
<summary>Hint</summary>

Wrap the three lines inside `computeArea` in `try:`, and add `except ValueError:` with a `self.messageBox(...)`.

</details>

<details>
<summary>One way to do it (try first!)</summary>

Only the computeArea method changes. The rest of the program stays the same.

```python
    def computeArea(self):
        try:
            width = self.widthField.getNumber()
            height = self.heightField.getNumber()
            self.areaField.setNumber(width * height)
        except ValueError:
            self.messageBox(title = "Error",
                            message = "Width and height must be whole numbers.")
```

</details>

#### Quick check

**If line 1 inside try works but line 2 raises a ValueError, what happens?**

- a) Line 3 still runs, then except runs
- b) Python jumps straight to except, and line 3 is skipped
- c) The program crashes anyway

<details>
<summary>Answer</summary>

**b) Python jumps straight to except, and line 3 is skipped**

The moment an error happens in the try block, Python leaves it and runs the matching except.

</details>

#### Watch out for

- Putting only one line in `try`. Put all the input-and-compute lines in there.
- Writing `except:` with no error type catches <i>everything</i>, including your own typos. Use `except ValueError:`.

---

## Lesson 9: Panels: grids inside your grid

_About 10 minutes_

#### The idea

<p>Say you want two rows of label + text box, then three buttons evenly spaced underneath. In one grid, that's a mess: the top part has 2 columns, the bottom wants 3.</p>
<p>The fix: <b>panels</b>. A panel is a box that sits in one cell of the window but has <b>its own separate grid</b> inside. <code>self.addPanel(row, column)</code> gives you a panel, and you add widgets to <i>it</i> instead of to <code>self</code>.</p>
<p>Panels have almost all the same add methods as the window: <code>panel.addLabel</code>, <code>panel.addButton</code>, <code>panel.addTextField</code>, and so on.</p>
<p>Tip: sketch your layout on paper first. Draw the panels as boxes with their own little grids.</p>

#### See it, then run it

```python
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

    def submit(self):
        self.messageBox(title = "Welcome",
                        message = "Signed up as " + self.userField.getText())

    def clear(self):
        self.userField.setText("")
        self.emailField.setText("")

    def help(self):
        self.messageBox(title = "Help",
                        message = "Type a username and email, then Submit.")

def main():
    SignUpForm().mainloop()

if __name__ == "__main__":
    main()
```

> Both panels have a widget at their own (0, 0). That's fine, because each panel's grid is separate.

#### Try it yourself

Add a third panel at window row 2 with a single label that says "Fields left blank: 0". When Submit is clicked, update it to show how many of the two fields are empty.

<details>
<summary>Hint</summary>

Save that label as `self.statusLabel`. In `submit`, start a count at 0 and add 1 for each field whose `getText()` equals `""`.

</details>

<details>
<summary>One way to do it (try first!)</summary>

Add the panel code at the end of `__init__` and replace the old submit method.

```python
        # In __init__, after the button panel:
        statusPanel = self.addPanel(row = 2, column = 0)
        self.statusLabel = statusPanel.addLabel(
            text = "Fields left blank: 0", row = 0, column = 0)

    def submit(self):
        blank = 0
        if self.userField.getText() == "":
            blank += 1
        if self.emailField.getText() == "":
            blank += 1
        self.statusLabel["text"] = "Fields left blank: " + str(blank)
```

</details>

#### Quick check

**You add a button to buttonPanel at row 0, column 0. Where does it go?**

- a) The top-left of the whole window
- b) The top-left of buttonPanel's own grid
- c) It replaces whatever is at the window's (0, 0)

<details>
<summary>Answer</summary>

**b) The top-left of buttonPanel's own grid**

Each panel has its own independent grid, so row and column are counted inside that panel.

</details>

#### Watch out for

- Adding a widget to `self` when you meant the panel (or the other way around). It'll show up in the wrong spot.

---

## Lesson 10: Text areas: lots of lines of output

_About 15 minutes_

#### The idea

<p>A text field holds one line. A <b>text area</b> holds many lines, scrolls, and is perfect for tables of results.</p>
<p><code>self.addTextArea(text = "", row = ..., column = ..., width = 40, height = 10)</code>. Width is in characters, height is in lines. breezypythongui's text areas come with scrollbars already.</p>
<ul>
<li><code>.setText(s)</code> replaces everything</li>
<li><code>.appendText(s)</code> adds to the end</li>
<li><code>.getText()</code> gives you everything in it</li>
</ul>
<p>To make neat columns, build one big string with <b>format codes</b>, line by line, ending each line with <code>"\n"</code>:</p>
<ul>
<li><code>"%5d" % 42</code> puts the whole number 42 in a space 5 characters wide</li>
<li><code>"%10.2f" % 3.14159</code> puts 3.14 in a space 10 wide with 2 decimals</li>
<li><code>"%-8s" % "Name"</code> puts the text in a space 8 wide, lined up on the left</li>
</ul>

#### See it, then run it

```python
from breezypythongui import EasyFrame

class TimesTable(EasyFrame):
    """Shows a times table in a text area."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Times Table")
        self.addLabel(text = "Number", row = 0, column = 0)
        self.numberField = self.addIntegerField(value = 7, row = 0,
                                                column = 1)
        self.addButton(text = "Make table", row = 1, column = 0,
                       columnspan = 2, command = self.makeTable)
        self.outputArea = self.addTextArea(text = "", row = 2,
                                           column = 0, columnspan = 2,
                                           width = 30, height = 12)

    def makeTable(self):
        number = self.numberField.getNumber()
        result = "%4s %4s %6s\n" % ("n", "x", "n*x")   # header row
        for x in range(1, 11):
            result += "%4d %4d %6d\n" % (number, x, number * x)
        self.outputArea.setText(result)

def main():
    TimesTable().mainloop()

if __name__ == "__main__":
    main()
```

> The pattern is: start with a header line, add one line per loop, then setText once at the end.

#### Try it yourself

Make a savings tracker: FloatFields for starting amount and weekly deposit, an IntegerField for number of weeks, and a text area that shows a table with columns Week and Total for each week.

<details>
<summary>Hint</summary>

Before the loop, set `total` to the starting amount. In the loop, add the deposit to the total, then add a line like `"%4d %12.2f\n" % (week, total)`.

</details>

<details>
<summary>One way to do it (try first!)</summary>

```python
from breezypythongui import EasyFrame

class SavingsTracker(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Savings")
        self.addLabel(text = "Starting amount", row = 0, column = 0)
        self.startField = self.addFloatField(value = 100.0, row = 0,
                                             column = 1, precision = 2)
        self.addLabel(text = "Weekly deposit", row = 1, column = 0)
        self.depositField = self.addFloatField(value = 25.0, row = 1,
                                               column = 1, precision = 2)
        self.addLabel(text = "Weeks", row = 2, column = 0)
        self.weeksField = self.addIntegerField(value = 8, row = 2,
                                               column = 1)
        self.addButton(text = "Show table", row = 3, column = 0,
                       columnspan = 2, command = self.showTable)
        self.outputArea = self.addTextArea(text = "", row = 4,
                                           column = 0, columnspan = 2,
                                           width = 30, height = 10)

    def showTable(self):
        total = self.startField.getNumber()
        deposit = self.depositField.getNumber()
        weeks = self.weeksField.getNumber()
        result = "%4s %12s\n" % ("Week", "Total")
        for week in range(1, weeks + 1):
            total += deposit
            result += "%4d %12.2f\n" % (week, total)
        self.outputArea.setText(result)

def main():
    SavingsTracker().mainloop()

if __name__ == "__main__":
    main()
```

</details>

#### Quick check

**What does "%8.2f" % 5 produce?**

- a) "5.00" with 4 spaces in front (8 characters total)
- b) "5" with 7 spaces in front
- c) "00000005"

<details>
<summary>Answer</summary>

**a) "5.00" with 4 spaces in front (8 characters total)**

8 is the total width, .2 means 2 decimals, f means float. So 5 becomes 5.00, padded to 8 characters.

</details>

#### Watch out for

- Calling `setText` inside the loop. Each call wipes out the last one, so you only see the final line. Build the string first, or use `appendText`.
- Forgetting `\n` at the end of each line, so everything ends up on one giant line.
- `getText()` on a text area gives you an extra `\n` at the very end. Keep that in mind if you save it to a file.

---

## Lesson 11: Pop-ups and file dialogs

_About 15 minutes_

#### The idea

<p>Three kinds of pop-up windows:</p>
<ul>
<li><b>Message box</b>: <code>self.messageBox(title = "...", message = "...")</code> shows info. You've seen this one already.</li>
<li><b>Prompter box</b>: <code>name = self.prompterBox(title = "...", promptString = "Your name:")</code> asks for one piece of text and returns what they typed.</li>
<li><b>File dialog</b>: the normal Open / Save window you see in every app. Needs <code>import tkinter.filedialog</code>.</li>
</ul>
<p><code>tkinter.filedialog.askopenfilename(parent = self, filetypes = [("Text files", "*.txt")])</code> returns the full path of the file they picked. <b>If they hit Cancel, you get back an empty value</b>, so always check <code>if fileName:</code> before opening.</p>
<p><code>filetypes</code> is a list of <code>(label, pattern)</code> pairs that limits which files show up.</p>

#### See it, then run it

```python
import tkinter.filedialog
from breezypythongui import EasyFrame

class FileInfo(EasyFrame):
    """Opens a text file and shows how many lines it has."""

    def __init__(self):
        EasyFrame.__init__(self, title = "File Info", width = 420,
                           height = 140)
        self.info = self.addLabel(text = "Pick a .txt file", row = 0,
                                  column = 0, sticky = "NSEW")
        self.addButton(text = "Open...", row = 1, column = 0,
                       command = self.pickFile)
        self.addButton(text = "Who are you?", row = 2, column = 0,
                       command = self.askName)

    def pickFile(self):
        fileTypes = [("Text files", "*.txt")]
        fileName = tkinter.filedialog.askopenfilename(parent = self,
                                                      filetypes = fileTypes)
        if fileName:                    # empty means they hit Cancel
            file = open(fileName, "r")
            lines = file.readlines()
            file.close()
            self.info["text"] = "That file has " + str(len(lines)) + " lines"

    def askName(self):
        name = self.prompterBox(title = "Hi",
                                promptString = "What's your name?")
        self.info["text"] = "Nice to meet you, " + name

def main():
    FileInfo().mainloop()

if __name__ == "__main__":
    main()
```

> Saving works the same way with asksaveasfilename. You get a file name back, then open it with "w" and write to it.

#### The save version

```python
fileName = tkinter.filedialog.asksaveasfilename(parent = self)
if fileName:
    file = open(fileName, "w")
    file.write("whatever text you want to save")
    file.close()
```

> This is a piece that goes inside a handler method, not a whole program.

#### Try it yourself

Add a button to FileInfo that opens a .txt file and shows its <b>first line</b> in a message box instead of the line count.

<details>
<summary>Hint</summary>

Same as `pickFile`, but after `readlines()` use `lines[0]`. Watch out for an empty file: check `if len(lines) > 0` first.

</details>

<details>
<summary>One way to do it (try first!)</summary>

Add the button line to `__init__` and add the new method to the class.

```python
    # In __init__:
        self.addButton(text = "First line", row = 3, column = 0,
                       command = self.showFirstLine)

    def showFirstLine(self):
        fileName = tkinter.filedialog.askopenfilename(
            parent = self, filetypes = [("Text files", "*.txt")])
        if fileName:
            file = open(fileName, "r")
            lines = file.readlines()
            file.close()
            if len(lines) > 0:
                self.messageBox(title = "First line", message = lines[0])
            else:
                self.messageBox(title = "First line",
                                message = "That file is empty.")
```

</details>

#### Quick check

**What should your code do if askopenfilename comes back empty?**

- a) Open it anyway
- b) Nothing: the user hit Cancel, so skip opening
- c) Show an error and close the program

<details>
<summary>Answer</summary>

**b) Nothing: the user hit Cancel, so skip opening**

An empty result means Cancel. Trying to open it would crash, so check if fileName: first.

</details>

#### Watch out for

- Forgetting `import tkinter.filedialog` at the top.
- Forgetting `file.close()`. On a save, your text might not actually get written.

---

## Lesson 12: Check buttons and radio buttons

_About 15 minutes_

#### The idea

<p><b>Check buttons</b> are checkboxes: pick any combination. <b>Radio buttons</b> are pick-exactly-one.</p>
<p><b>Check buttons:</b> <code>self.cheeseCB = self.addCheckbutton(text = "Extra cheese", row = 1, column = 1)</code>. Later, <code>self.cheeseCB.isChecked()</code> gives <code>True</code> or <code>False</code>.</p>
<p><b>Radio buttons</b> take three steps:</p>
<ol>
<li>Make a group: <code>self.sizeGroup = self.addRadiobuttonGroup(row = 1, column = 0, rowspan = 3)</code></li>
<li>Add buttons to the group: <code>small = self.sizeGroup.addRadiobutton(text = "Small")</code></li>
<li>Pick a default: <code>self.sizeGroup.setSelectedButton(small)</code></li>
</ol>
<p>To see which one is picked: <code>self.sizeGroup.getSelectedButton()["text"]</code> gives you the label of the chosen button, like <code>"Small"</code>.</p>

#### See it, then run it

```python
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
```

> rowspan = 3 on the group, because the three radio buttons stack down three rows.

#### Try it yourself

Add a second radio group for Pickup or Delivery (default Pickup). Delivery adds $3.00 to the price.

<details>
<summary>Hint</summary>

Same three steps: make `self.methodGroup` at row 5, add two buttons, set the default. In `order`, check `getSelectedButton()["text"]` and add 3 if it's Delivery. Move the Order button down a row.

</details>

<details>
<summary>One way to do it (try first!)</summary>

orient = "horizontal" lays the buttons out side by side. Use columnspan instead of rowspan when they're horizontal.

```python
        # In __init__ (and move the Order button to row 6):
        self.addLabel(text = "Pickup or delivery", row = 4, column = 0)
        self.methodGroup = self.addRadiobuttonGroup(row = 5, column = 0,
                                                    columnspan = 2,
                                                    orient = "horizontal")
        pickup = self.methodGroup.addRadiobutton(text = "Pickup")
        self.methodGroup.addRadiobutton(text = "Delivery")
        self.methodGroup.setSelectedButton(pickup)

    # In order(), before the messageBox:
        if self.methodGroup.getSelectedButton()["text"] == "Delivery":
            price += 3.00
```

</details>

#### Quick check

**You want users to choose one shirt size: S, M, L or XL. What do you use?**

- a) Four check buttons
- b) A radio button group with four buttons
- c) Four text fields

<details>
<summary>Answer</summary>

**b) A radio button group with four buttons**

Radio buttons are for choosing exactly one. Check buttons are for choosing any combination.

</details>

#### Watch out for

- Forgetting `setSelectedButton`, so nothing is picked at the start and `getSelectedButton()` doesn't give you a real choice.
- Writing `getSelectedButton["text"]` without the `()`. It's a method call first, then `["text"]`.
- Adding radio buttons with `self.addRadiobutton`. They go on the <b>group</b>: `self.sizeGroup.addRadiobutton`.

---

## Lesson 13: Keyboard events: pressing Enter

_About 5 minutes_

#### The idea

<p>It's nice when pressing Enter in a box does the same thing as clicking the button. You set that up with <code>bind</code>:</p>
<p><code>self.billField.bind("&lt;Return&gt;", lambda event: self.computeTip())</code></p>
<ul>
<li><code>"&lt;Return&gt;"</code> is the name for the Enter key.</li>
<li>When the key is pressed, tkinter calls your function and hands it an <b>event</b> object.</li>
<li>Your <code>computeTip</code> only takes <code>self</code>, so it can't accept that event. The <code>lambda event: ...</code> is a tiny throwaway function that accepts the event, ignores it, and calls your method.</li>
</ul>
<p>Put the <code>bind</code> line in <code>__init__</code>, right after you create the field.</p>

#### See it, then run it

```python
from breezypythongui import EasyFrame

class EnterKeyDemo(EasyFrame):
    """Press Enter in the box to shout it."""

    def __init__(self):
        EasyFrame.__init__(self, title = "Enter Key Demo")
        self.addLabel(text = "Type, then press Enter", row = 0,
                      column = 0)
        self.inputField = self.addTextField(text = "", row = 1,
                                            column = 0)
        self.inputField.bind("<Return>", lambda event: self.shout())
        self.output = self.addLabel(text = "", row = 2, column = 0)

    def shout(self):
        self.output["text"] = self.inputField.getText().upper() + "!!!"

def main():
    EnterKeyDemo().mainloop()

if __name__ == "__main__":
    main()
```

> Click in the box first so it has the cursor, then press Enter.

#### Try it yourself

Go back to your area calculator and make Enter in either box run computeArea.

<details>
<summary>Hint</summary>

Two `bind` lines, one for each field, both calling `self.computeArea()`.

</details>

<details>
<summary>One way to do it (try first!)</summary>

Put these in `__init__` after the fields are created.

```python
        self.widthField.bind("<Return>", lambda event: self.computeArea())
        self.heightField.bind("<Return>", lambda event: self.computeArea())
```

</details>

#### Quick check

**Why can't you just write bind("<Return>", self.computeTip)?**

- a) bind passes an event argument, and computeTip doesn't accept one
- b) bind only works with text fields
- c) You can, it works the same

<details>
<summary>Answer</summary>

**a) bind passes an event argument, and computeTip doesn't accept one**

The key press sends an event object. The lambda accepts it and throws it away, then calls your normal method.

</details>

#### Watch out for

- Spelling: it's `"<Return>"` with the angle brackets and a capital R.

---

## Exercise map

These match your Cengage assignments (the chapter9 folders in your Codespace). All of Chapter 9 is graded by your professor instead of the autograder, so compare your window to the screenshots in each exercise's `assets` folder. Each hint gets you started without giving the answer away.

### 9-1: Tax calculator with a GUI

Lessons: [Lesson 2](#lesson-2-your-first-window), [Lesson 3](#lesson-3-the-grid-putting-things-where-you-want), [Lesson 6](#lesson-6-input-and-output-with-entry-fields), [Lesson 5](#lesson-5-buttons-and-event-handlers)

<details>
<summary>How to start</summary>

This is the tip calculator pattern. Your `ex01/student` folder already has `taxform.py`, the terminal version, with the tax constants and formula, so reuse them. Inputs: gross income (FloatField) and dependents (IntegerField). One Compute button. A readonly output field for the total tax. Match the layout in the screenshots.

</details>

### 9-2: Bouncy ball with a GUI

Lessons: [Lesson 6](#lesson-6-input-and-output-with-entry-fields), [Lesson 5](#lesson-5-buttons-and-event-handlers)

<details>
<summary>How to start</summary>

Open your Chapter 3 bouncy program (`chapter3/ex04/student`). Its inputs become fields, and the loop that adds up the distance goes <b>inside</b> your Compute handler. The total goes into a readonly output field. The screenshots show exactly which fields they want.

</details>

### 9-3: Temperature converter

Lessons: [Lesson 3](#lesson-3-the-grid-putting-things-where-you-want), [Lesson 6](#lesson-6-input-and-output-with-entry-fields), [Lesson 5](#lesson-5-buttons-and-event-handlers), [Lesson 7](#lesson-7-instance-variables-how-the-window-remembers-stuff)

<details>
<summary>How to start</summary>

The layout is spelled out exactly: labels in row 0, FloatFields in row 1 (starting at 32.0 and 0.0), and buttons labeled `>>>>` and `<<<<` in row 2. You need <b>two</b> handlers, one per button. C = (F &minus; 32) &times; 5 / 9, and you can flip that around for the other direction.

</details>

### 9-4: Converter that responds to Enter

Lessons: [Lesson 13](#lesson-13-keyboard-events-pressing-enter)

<details>
<summary>How to start</summary>

Cengage copies your 9-3 file into `temperatureconverterwithkey.py` for you. If it's still just `# Write your code here`, paste your 9-3 code in. Then add one `bind` per field: Enter in the Fahrenheit box runs the F-to-C handler, and Enter in the Celsius box runs the C-to-F one.

</details>

### 9-5: Reverse guessing game (computer guesses)

Lessons: [Lesson 5](#lesson-5-buttons-and-event-handlers), [Lesson 7](#lesson-7-instance-variables-how-the-window-remembers-stuff)

<details>
<summary>How to start</summary>

Think about how <i>you'd</i> find a number from 1 to 100 if someone only said too small or too large: always guess the middle of what's left. Keep the lowest and highest possible values (plus the current guess and a count) as instance variables. Each button changes the range and makes a new guess. When it's over, disable Too small, Too large and Correct until New game is clicked.

</details>

### 9-6: Tax calculator with filing status

Lessons: [Lesson 12](#lesson-12-check-buttons-and-radio-buttons)

<details>
<summary>How to start</summary>

Cengage copies your 9-1 file in as the starting point (paste it in yourself if it's empty). Add a radio group with Single, Married and Divorced, and set Single as the default. In the compute handler, check `getSelectedButton()["text"]` to choose the rate (20%, 15% or 10%).

</details>

### 9-7: TidBit payment schedule

Lessons: [Lesson 6](#lesson-6-input-and-output-with-entry-fields), [Lesson 10](#lesson-10-text-areas-lots-of-lines-of-output)

<details>
<summary>How to start</summary>

The `tidbit.py` in the folder is just a placeholder, so paste your Chapter 3 TidBit program (`chapter3/ex10/student/tidbit.py`) into it for reference. Get the table working as a function that takes the rate and price and <b>returns</b> one big formatted string. That's your <b>model</b>. The GUI (your <b>view</b>) reads the two fields, calls it, and puts the string in a text area. Chapter 10 talks more about model/view.

</details>

### 9-8: Text editor

Lessons: [Lesson 6](#lesson-6-input-and-output-with-entry-fields), [Lesson 10](#lesson-10-text-areas-lots-of-lines-of-output), [Lesson 11](#lesson-11-pop-ups-and-file-dialogs)

<details>
<summary>How to start</summary>

A TextField for the filename, a TextArea for the contents (breezypythongui's already has scrollbars), and Open, Save and New buttons. Open reads the file into the text area. Save writes the text area's `getText()` to the file. New does `setText("")` on both. The screenshots show the open and save dialogs they expect.

</details>

### 9-9: Image browser

Lessons: [Lesson 4](#lesson-4-making-it-look-right-colors-fonts-images), [Lesson 11](#lesson-11-pop-ups-and-file-dialogs)

<details>
<summary>How to start</summary>

Like the FileInfo example, but with `filetypes = [("GIF files", "*.gif")]`. When a file is picked, make a `PhotoImage(file = fileName)`, keep it in `self.something`, and put it in a label's `"image"`. Your folder has `smokey.gif` (and another copy in `Subfolder`) to test with.

</details>

### Debug: Jack's chessboard (fix it)

Lessons: [Lesson 3](#lesson-3-the-grid-putting-things-where-you-want)

<details>
<summary>How to start</summary>

Cengage's version wants you to <b>fix</b> `chessboard.py`, not just explain it. Trace it on paper first: write down the color Jack's loop picks for the <b>last square of row 0</b> and the <b>first square of row 1</b>. On a real chessboard, should those match or be different? Then think about what should happen to `color` when a new row starts. The line at the end about GIF colors looks like it was copied from another exercise, so you can ignore it.

</details>

---

_Built from your Chapter 9 textbook pages and your Cengage assignment instructions. Every example program was run and tested in Python 3.12._
