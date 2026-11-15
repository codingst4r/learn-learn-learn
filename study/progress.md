# My progress

> Claude Code reads this at the start of every session and updates it when you run `/leftoff`. You can edit it yourself too. Keep it short.

## Where I left off

- 2026-11-14: Finished Lesson 8 (area calculator now pops up a message on bad input). Ran the Lesson 9 panels example. Started the Lesson 9 try-it in `lessons/lesson9_try.py`: the third panel and its label are in, and `submit` is half written.
- next: finish `submit` so it counts how many of the two fields are blank and shows it in the bottom label.

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
- [ ] 9. Panels: grids inside your grid
- [ ] 10. Text areas: lots of lines of output
- [ ] 11. Pop-ups and file dialogs
- [ ] 12. Check buttons and radio buttons
- [ ] 13. Keyboard events: pressing Enter

### Chapter 9 exercises
- [x] 9-1 Tax calculator with a GUI
- [x] 9-2 Bouncy ball with a GUI
- [x] 9-3 Temperature converter
- [ ] 9-4 Converter that responds to Enter
- [ ] 9-5 Reverse guessing game (computer guesses)
- [ ] 9-6 Tax calculator with filing status
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

## Session log (newest first, keep the last 5)

- 2026-11-14: Finished Lesson 8 (broke the tip calculator on purpose to find `ValueError`, added try/except to the area calculator). Did Lesson 9 panels: each panel is one cell of the window with its own grid, and it stretches to fill its cell. Homework 9-1 to 9-3 all passed.
- 2026-11-13: Short one. Typed the Lesson 8 example. Set up autopep8 as my Python formatter (Shift+Alt+F), keeping the book's spaces around `=`.
- 2026-11-11: Fixed git sync (switched to schannel). Finished Lesson 7: worked out what `self` really is, built a score keeper with a 2-second warning using `self.after`. Fixed the Lesson 6 readonly leftover.
- 2026-11-09 (later): Finished Lessons 5 and 6. Coin flip with an extra Reset button, plus a rectangle area calculator. Saw that typing 3.5 in an IntegerField causes a ValueError (Lesson 8 handles that).
- 2026-11-09: Finished Lesson 4 and its try-it. Added Smokey (an image) and a terminal launcher menu to `lesson4.py`, and worked out what each sticky setting does.
- 2026-11-06: Finished Chapter 9 Lessons 1 to 3, including the Seat 1 to 12 try-it. Ran the Lesson 4 example. Moved practice files into `lessons/`.
