# My progress

> Claude Code reads this at the start of every session and updates it when you run `/leftoff`. You can edit it yourself too. Keep it short.

## Where I left off

- 2026-11-17: Finished Lesson 12 (pizza order with a Pickup/Delivery group). Homework 9-4, 9-5 and 9-6 all passed. Started Lesson 10: ran the times table example and learned format codes like `%6.1f`. The Lesson 10 try-it is started in `lessons/lesson10_try.py` but not checked yet.
- next: finish the Lesson 10 try-it and `/check` it. Then Lesson 11, then homework 9-7.
- **On the desktop:** delete the old `lessons/lesson12.py` and `lessons/lesson12_try.py` there *before* running `/start`, or the pull will fail.

## Done

### Chapter 9 lessons (study/chapter9.md)
- [x] 1. Terminal vs. GUI: who's in charge?
- [x] 2. Your first window
- [x] 3. The grid: putting things where you want
- [x] 4. Making it look right: colors, fonts, images
- [x] 5. Buttons and event handlers
- [x] 6. Input and output with entry fields
- [x] 7. Instance variables: how the window remembers stuff
- [x] 8. Bad input? Don't crash, pop up a message
- [x] 9. Panels: grids inside your grid
- [ ] 10. Text areas: lots of lines of output
- [ ] 11. Pop-ups and file dialogs
- [x] 12. Check buttons and radio buttons
- [x] 13. Keyboard events: pressing Enter

### Chapter 9 exercises
- [x] 9-1 Tax calculator with a GUI
- [x] 9-2 Bouncy ball with a GUI
- [x] 9-3 Temperature converter
- [x] 9-4 Converter that responds to Enter
- [x] 9-5 Reverse guessing game (computer guesses)
- [x] 9-6 Tax calculator with filing status
- [ ] 9-7 TidBit payment schedule
- [ ] 9-8 Text editor
- [ ] 9-9 Image browser
- [ ] Debug Jack's chessboard (fix it)

### Chapter 10 lessons (study/chapter10.md)
- [ ] 1. Classes, objects and `__init__`
- [ ] 2. `__str__` and docstrings
- [ ] 3. Accessors and mutators
- [ ] 4. How to build a class from scratch (and when objects die)
- [ ] 5. Operator overloading: making + work on your objects
- [ ] 6. Comparing objects: ==, &lt; and sorting
- [ ] 7. `__repr__`: nicer output in the shell and in lists
- [ ] 8. Class variables: one value shared by every object
- [ ] 9. Objects that hold other objects
- [ ] 10. Saving objects to a file with pickle
- [ ] 11. Model/view: keep the data separate from the screen
- [ ] 12. A 2D grid class and `__getitem__`
- [ ] 13. Inheritance: a new class built on an old one
- [ ] 14. Polymorphism: same method name, different behavior
- [ ] 15. Fail-safe methods: preconditions and raise

### Chapter 10 exercises
- [ ] 10-1 Compare Student objects
- [ ] 10-2 Shuffle and sort students
- [ ] 10-3 Bank `__str__` sorted by name
- [ ] 10-4 ATM: lock out after 3 failures
- [ ] 10-5 Doctor program, model/view
- [ ] 10-6 Craps Player, one roll at a time
- [ ] 10-7 Craps game GUI
- [ ] 10-8 Cards that face up or down
- [ ] 10-9 Cards GUI
- [ ] 10-10 Shapes with Turtle
- [ ] Debug Jack's ZeroDivisionError (fix it)

## Hard stuff (review these)

- Nested loops with a grid: which loop is rows and which is columns. The inner loop changes with every item, so it sets the direction things fill in.
- Why images need `self.picture`: the window keeps widgets alive, but you have to keep pictures alive yourself.
- What `self` is: one object built from the class (an *instance*), not the method you're in and not the class itself. Two windows = two `self`s, each with its own `clicks`. Plain variables (no `self.`) disappear when the method ends.
- In a GUI, don't use `time.sleep` (it freezes the window). Use `self.after(ms, self.method)`.
- Variables that only get set inside `except` (or an `if`) might not exist later. Give them a starting value (like `= False`) at the top. Also: a method with no `return` gives back `None`.

## Session log (newest first, keep the last 5)

- 2026-11-17: Lesson 12 done (saw why a default radio button matters: with none set, `getSelectedButton()` raises ValueError). 9-4 to 9-6 passed. Learned format codes in Lesson 10: `%` slot, width, `.decimals`, type, and `-` to flip alignment.
- 2026-11-16: Finished Lesson 13 try-it with custom error pop-ups (two `try`s, flags that hold the message, `getValue()` for what was typed, box height from message length). Refactored so it's DRY.
- 2026-11-15: Finished Lesson 9 (blank-field counter, starts at 2). Learned class vs object for methods: `self.clear()` is really `SignUpForm.clear(self)`, and `print(e)` uses the error's `__str__`. Started Lesson 13.
- 2026-11-14: Finished Lesson 8 (broke the tip calculator on purpose to find `ValueError`, added try/except to the area calculator). Did Lesson 9 panels: each panel is one cell of the window with its own grid, and it stretches to fill its cell. Homework 9-1 to 9-3 all passed.
- 2026-11-13: Short one. Typed the Lesson 8 example. Set up autopep8 as my Python formatter (Shift+Alt+F), keeping the book's spaces around `=`.