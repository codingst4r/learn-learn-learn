# Chapter 10: Design with Classes

_Building your own types of objects from scratch_

> **Reading this in VS Code:** press `Ctrl+K` then `V` to open the preview next to your code (or `Ctrl+Shift+V` for a full tab). Click **Hint**, **One way to do it** and **Answer** to open them. The same guide with clickable quizzes and a progress bar is online: https://claude.ai/artifact/UTRzx65vxo8VT4eoQWERA3

## How to use this

<p>In Chapter 9 you <i>customized</i> a class someone else wrote (EasyFrame). In this chapter you build your <b>own</b> classes from nothing: a Student, a bank account, a deck of cards.</p>
<p>The examples here are game-themed (heroes, items, a game map) because classes are exactly how games keep track of stuff. If you ever wrote a Roblox script that tracked a player's health or coins, you were already thinking this way.</p>

- **One lesson at a time.** Most take 10 to 15 minutes. Busy day? One lesson still counts.
- **Run every example yourself** and change things. Break it on purpose and read the error.
- **Do the Try it before peeking** at the answer. Getting stuck for a few minutes is where the learning happens.
- Working on a graded exercise? Jump to the [exercise map](#exercise-map) to see which lessons it uses, or ask Claude Code `/lesson` with the exercise number.
- When you finish a lesson, check it off in `study/progress.md` (or let `/leftoff` do it).

## Setup

<p>Nothing to install. Every example on this page is a complete program, so you can paste it into a new <code>.py</code> file and run it with <code>python3 file.py</code>.</p>
<p>The GUI example in Lesson 11 also needs <code>breezypythongui.py</code> in the same folder. Copy it from any Chapter 9 <code>student</code> folder in your Codespace, and use <b>Open GUI</b> in the Cengage sidebar to see the window.</p>
<p><b>Shell trick:</b> run <code>python3 -i file.py</code> and Python stays open afterward with your classes loaded. Type <code>h = Hero("Test", 50)</code> and play with it live. That's the fastest way to learn this stuff.</p>

## The 4 words this whole chapter is about

<ol><li><b>Class</b>: the blueprint. Written once. <code>class Hero(object):</code></li><li><b>Object</b> (or instance): one actual thing made from the blueprint. <code>mike = Hero("Mike", 100)</code></li><li><b>Instance variables</b>: what each object <i>knows</i>. <code>self.name</code>, <code>self.health</code></li><li><b>Methods</b>: what each object can <i>do</i>. <code>mike.takeDamage(20)</code></li></ol>

> Think of a class as a character template in a game. The template says every hero has a name, health and coins. Each hero you spawn gets their own copy of those stats.

## Lessons

1. [Classes, objects and `__init__`](#lesson-1-classes-objects-and-__init__) · about 15 min
2. [`__str__` and docstrings](#lesson-2-__str__-and-docstrings) · about 10 min
3. [Accessors and mutators](#lesson-3-accessors-and-mutators) · about 10 min
4. [How to build a class from scratch (and when objects die)](#lesson-4-how-to-build-a-class-from-scratch-and-when-objects-die) · about 10 min
5. [Operator overloading: making + work on your objects](#lesson-5-operator-overloading-making--work-on-your-objects) · about 15 min
6. [Comparing objects: ==, &lt; and sorting](#lesson-6-comparing-objects---and-sorting) · about 15 min
7. [`__repr__`: nicer output in the shell and in lists](#lesson-7-__repr__-nicer-output-in-the-shell-and-in-lists) · about 5 min
8. [Class variables: one value shared by every object](#lesson-8-class-variables-one-value-shared-by-every-object) · about 10 min
9. [Objects that hold other objects](#lesson-9-objects-that-hold-other-objects) · about 15 min
10. [Saving objects to a file with pickle](#lesson-10-saving-objects-to-a-file-with-pickle) · about 15 min
11. [Model/view: keep the data separate from the screen](#lesson-11-modelview-keep-the-data-separate-from-the-screen) · about 15 min
12. [A 2D grid class and `__getitem__`](#lesson-12-a-2d-grid-class-and-__getitem__) · about 10 min
13. [Inheritance: a new class built on an old one](#lesson-13-inheritance-a-new-class-built-on-an-old-one) · about 15 min
14. [Polymorphism: same method name, different behavior](#lesson-14-polymorphism-same-method-name-different-behavior) · about 10 min
15. [Fail-safe methods: preconditions and raise](#lesson-15-fail-safe-methods-preconditions-and-raise) · about 10 min

→ [Exercise map](#exercise-map)

---

## Lesson 1: Classes, objects and `__init__`

_About 15 minutes_

#### The idea

<p>A class is a blueprint. Making an object from it looks like calling a function: <code>Hero("Mike", 100)</code>. When you do that, Python automatically runs the class's <code>__init__</code> method. That's its <b>constructor</b>, and its job is to give the new object its starting values.</p>
<ul>
<li><code>self</code> is the object being built. <code>self.name = name</code> means "this hero's name is whatever was passed in."</li>
<li>Variables that start with <code>self.</code> are <b>instance variables</b>. Each object gets its own set. Mike's health and Nova's health are separate.</li>
<li>You never pass <code>self</code> yourself. Python fills it in. That's why <code>__init__(self, name, health)</code> is called with just two things: <code>Hero("Mike", 100)</code>.</li>
</ul>
<p><code>class Hero(object):</code> means Hero's parent class is <code>object</code>, the most basic class in Python. The book always writes <code>(object)</code>. <code>class Hero:</code> means the same thing.</p>

#### See it, then run it

```python
class Hero(object):
    """A character in a game."""

    def __init__(self, name, health):
        """Runs automatically when you make a new Hero."""
        self.name = name
        self.health = health
        self.coins = 0          # every hero starts broke

mike = Hero("Mike", 100)
nova = Hero("Nova", 80)

print(mike.name, mike.health, mike.coins)   # Mike 100 0
print(nova.name, nova.health, nova.coins)   # Nova 80 0

nova.coins = 50                             # only changes Nova
print(mike.coins, nova.coins)               # 0 50
```

> Notice coins isn't passed in. `__init__` can set up instance variables with fixed starting values too.

#### Try it yourself

Write a `Song` class. Each song knows its `title`, `artist` and a `plays` count that starts at 0. Make two songs and print their info.

<details>
<summary>Hint</summary>

`def __init__(self, title, artist):` then three `self.something = ...` lines. `plays` isn't a parameter, it just starts at 0.

</details>

<details>
<summary>One way to do it (try first!)</summary>

```python
class Song(object):
    """A song in a playlist."""

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.plays = 0

song1 = Song("Lose Yourself", "Eminem")
song2 = Song("Blinding Lights", "The Weeknd")
print(song1.title, "by", song1.artist, "-", song1.plays, "plays")
print(song2.title, "by", song2.artist, "-", song2.plays, "plays")
```

</details>

#### Quick check

**`__init__` is defined as def `__init__`(self, name, health). How do you make a Hero?**

- a) Hero(self, "Mike", 100)
- b) Hero("Mike", 100)
- c) Hero.`__init__`("Mike", 100)

<details>
<summary>Answer</summary>

**b) Hero("Mike", 100)**

Python passes self for you. You only give the other arguments.

</details>

#### Watch out for

- `_init_` with one underscore on each side. Python won't see it as the constructor and you'll get `TypeError: Hero() takes no arguments`.
- Writing `name = name` instead of `self.name = name`. Without `self.`, the value disappears when `__init__` ends.
- Forgetting `self` as the first parameter of any method.

---

## Lesson 2: `__str__` and docstrings

_About 10 minutes_

#### The idea

<p>Try <code>print(mike)</code> with the last example and you get something ugly like <code>&lt;__main__.Hero object at 0x10d3...&gt;</code>. Python doesn't know how to show your object.</p>
<p>Fix it with a <code>__str__</code> method. It <b>returns a string</b> describing the object. Then <code>print(mike)</code> and <code>str(mike)</code> automatically use it. It's also your best debugging tool: print an object anytime to see what's inside it.</p>
<p><b>Docstrings</b> (the triple-quoted text right under a <code>class</code> or <code>def</code> line) describe what something does. Type <code>help(Hero)</code> in the shell and Python prints all of them. The book wants one for the module, the class and every method.</p>

#### See it, then run it

```python
class Hero(object):
    """A character in a game."""

    def __init__(self, name, health):
        """Sets up a new hero with 0 coins."""
        self.name = name
        self.health = health
        self.coins = 0

    def __str__(self):
        """Returns a string version of the hero."""
        return self.name + " | HP: " + str(self.health) + \
               " | Coins: " + str(self.coins)

mike = Hero("Mike", 100)
print(mike)          # Mike | HP: 100 | Coins: 0
text = str(mike)     # same string, saved in a variable
help(Hero)           # shows your docstrings
```

> The backslash at the end of a line lets one statement continue onto the next line.

#### Try it yourself

Add a `__str__` to your Song class so `print(song1)` shows something like `Lose Yourself by Eminem (0 plays)`.

<details>
<summary>Hint</summary>

Return a string made with `+`. `self.plays` is a number, so wrap it in `str()`.

</details>

<details>
<summary>One way to do it (try first!)</summary>

```python
class Song(object):
    """A song in a playlist."""

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.plays = 0

    def __str__(self):
        """Returns the string version of the song."""
        return self.title + " by " + self.artist + \
               " (" + str(self.plays) + " plays)"

song1 = Song("Lose Yourself", "Eminem")
print(song1)
```

</details>

#### Quick check

**What should `__str__` do?**

- a) print() the object's info
- b) return a string with the object's info
- c) change the object's instance variables

<details>
<summary>Answer</summary>

**b) return a string with the object's info**

`__str__` returns a string. print() then shows that string. If `__str__` prints instead of returning, you get TypeError: `__str__` returned non-string.

</details>

#### Watch out for

- Using `print` inside `__str__` instead of `return`.
- Adding a number to a string: `"HP: " + self.health` gives a TypeError. Use `str(self.health)`.

---

## Lesson 3: Accessors and mutators

_About 10 minutes_

#### The idea

<p>Methods are just functions that live inside a class and always get <code>self</code> first. Two main kinds:</p>
<ul>
<li><b>Accessors</b> let you <i>look</i> at an object without changing it: <code>getName()</code>, <code>getHealth()</code>. They usually <code>return</code> something.</li>
<li><b>Mutators</b> <i>change</i> the object: <code>takeDamage(20)</code>, <code>addCoins(5)</code>.</li>
</ul>
<p>Why not just do <code>mike.health = -999</code> directly? Because a mutator can enforce rules, like "health never goes below 0." The book's rule of thumb: <b>the fewer ways an object can change, the easier it is to use correctly.</b> So if nothing should ever rename a hero, don't write a <code>setName</code>.</p>
<p>A method with no <code>return</code> statement gives back <code>None</code>.</p>

#### See it, then run it

```python
class Hero(object):
    """A character in a game."""

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.coins = 0

    # Accessors: look, don't touch
    def getName(self):
        return self.name

    def getHealth(self):
        return self.health

    # Mutators: change the object, following the rules
    def takeDamage(self, amount):
        """Health drops by amount, but never below 0."""
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def addCoins(self, amount):
        self.coins += amount

    def __str__(self):
        return self.name + " | HP: " + str(self.health) + \
               " | Coins: " + str(self.coins)

mike = Hero("Mike", 100)
mike.takeDamage(30)
mike.addCoins(15)
print(mike)                 # Mike | HP: 70 | Coins: 15
mike.takeDamage(500)
print(mike.getHealth())     # 0, not -430
```

#### Try it yourself

Give your Song class a `getTitle()` accessor, a `getPlays()` accessor, and a `play()` mutator that adds 1 to plays. Play a song 3 times and print it.

<details>
<summary>Hint</summary>

`play` doesn't need any parameters besides `self`. Inside it: `self.plays += 1`.

</details>

<details>
<summary>One way to do it (try first!)</summary>

```python
class Song(object):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.plays = 0

    def getTitle(self):
        return self.title

    def getPlays(self):
        return self.plays

    def play(self):
        self.plays += 1

    def __str__(self):
        return self.title + " by " + self.artist + \
               " (" + str(self.plays) + " plays)"

song = Song("Lose Yourself", "Eminem")
for count in range(3):
    song.play()
print(song)                 # Lose Yourself by Eminem (3 plays)
print(song.getPlays())      # 3
```

</details>

#### Quick check

**Which of these is a mutator?**

- a) getHealth(self) that returns self.health
- b) heal(self, amount) that adds amount to self.health
- c) `__str__`(self) that returns a description

<details>
<summary>Answer</summary>

**b) heal(self, amount) that adds amount to self.health**

heal changes the object's state, so it's a mutator. The other two only look.

</details>

#### Watch out for

- Calling a method without parentheses: `mike.getHealth` gives you the method itself, not the number. Use `mike.getHealth()`.
- Writing `takeDamage(mike, 30)`. Methods are called on the object: `mike.takeDamage(30)`.

---

## Lesson 4: How to build a class from scratch (and when objects die)

_About 10 minutes_

#### The idea

<p>The book gives a recipe for designing a class. Here it is in normal words:</p>
<ol>
<li><b>Before coding, list two things:</b> what the object should <i>know</i> (those become instance variables) and what it should <i>do</i> (those become methods). Nouns are usually variables, verbs are usually methods.</li>
<li><b>Write a tiny test script first</b> that uses the class as if it already existed. It won't run yet, but it shows you what methods you need.</li>
<li><b>Write <code>__init__</code> and <code>__str__</code> first.</b> Then you can make an object, print it and check your setup.</li>
<li><b>Add the other methods one at a time</b>, running your test after each one. If method A uses method B, write B first.</li>
<li><b>Write docstrings as you go</b>, not at the end.</li>
</ol>
<p><b>When does an object die?</b> When nothing refers to it anymore. If <code>mike = Hero(...)</code> and later <code>mike = None</code> (and nothing else points to that hero), Python eventually cleans up its memory automatically. That's called <b>garbage collection</b>.</p>

#### See it, then run it

```python
# Step 1: plan (just comments)
# A Timer KNOWS: how many seconds are left
# A Timer can DO: tick (lose 1 second), check if it's done, reset

# Step 3: __init__ and __str__ first
class Timer(object):
    """A countdown timer."""

    def __init__(self, seconds):
        self.start = seconds
        self.left = seconds

    def __str__(self):
        return str(self.left) + " seconds left"

    # Step 4: the rest, one at a time
    def tick(self):
        """Loses one second, stopping at 0."""
        if self.left > 0:
            self.left -= 1

    def isDone(self):
        return self.left == 0

    def reset(self):
        self.left = self.start

# Step 2: the test script
t = Timer(3)
print(t)            # 3 seconds left
while not t.isDone():
    t.tick()
    print(t)
t.reset()
print(t)            # 3 seconds left
```

> The test script is at the bottom so the class is defined before it's used, but write it first in your head (or on paper).

#### Try it yourself

Plan (don't code yet) a `Lock` class for a combination lock. Write the plan as comments: what it knows, what it does, and a 4-line test script that would use it.

<details>
<summary>Hint</summary>

What does a lock need to remember? Its combination, and whether it's open. What can you do to it? Try a combination, close it, check if it's open.

</details>

<details>
<summary>One way to do it (try first!)</summary>

The plan is the important part. The code under it is just to show the plan turns straight into a class.

```python
# A Lock KNOWS: its secret combination, whether it is open
# A Lock can DO:
#   tryCombo(guess) -> opens it if guess matches, returns True/False
#   close()         -> locks it again
#   isOpen()        -> returns True if open
#   __str__         -> "Lock (open)" or "Lock (closed)"
#
# Test script:
# lock = Lock("1234")
# print(lock.tryCombo("0000"))   # False
# print(lock.tryCombo("1234"))   # True
# print(lock)                    # Lock (open)

class Lock(object):
    def __init__(self, combo):
        self.combo = combo
        self.open = False

    def tryCombo(self, guess):
        if guess == self.combo:
            self.open = True
        return self.open

    def close(self):
        self.open = False

    def isOpen(self):
        return self.open

    def __str__(self):
        if self.open:
            return "Lock (open)"
        return "Lock (closed)"

lock = Lock("1234")
print(lock.tryCombo("0000"))
print(lock.tryCombo("1234"))
print(lock)
```

</details>

#### Quick check

**When is an object eligible for garbage collection?**

- a) As soon as its method finishes
- b) When no variable or list refers to it anymore
- c) After the program has run for a while

<details>
<summary>Answer</summary>

**b) When no variable or list refers to it anymore**

An object lives as long as something can still reach it. Once nothing refers to it, Python can recycle its memory.

</details>

#### Watch out for

- Writing the whole class at once, then running it for the first time. Test after every method, so when something breaks you know which part did it.

---

## Lesson 5: Operator overloading: making + work on your objects

_About 15 minutes_

#### The idea

<p>Here's a secret: when Python sees <code>a + b</code>, it actually runs <code>a.__add__(b)</code>. So if you write an <code>__add__</code> method in your class, <code>+</code> works on your objects. That's called <b>operator overloading</b>.</p>
<ul>
<li><code>self</code> is the thing on the <b>left</b> of the operator, and the other parameter (usually named <code>other</code>) is the thing on the <b>right</b>.</li>
<li>The method should <b>return a new object</b> rather than changing <code>self</code>. When you do <code>3 + 4</code>, the 3 doesn't turn into 7.</li>
</ul>
<div class="table-wrap"><table>
<tr><th>Operator</th><th>Method name</th></tr>
<tr><td><code>+</code></td><td><code>__add__</code></td></tr>
<tr><td><code>-</code></td><td><code>__sub__</code></td></tr>
<tr><td><code>*</code></td><td><code>__mul__</code></td></tr>
<tr><td><code>/</code></td><td><code>__truediv__</code></td></tr>
<tr><td><code>%</code></td><td><code>__mod__</code></td></tr>
</table></div>
<p><b>Heads up:</b> the table in your book lists <code>__div__</code> for <code>/</code>. That's from old Python 2. In Python 3, <code>/</code> calls <code>__truediv__</code>. I tested it: a class with only <code>__div__</code> gives a TypeError when you use <code>/</code>.</p>

#### See it, then run it

```python
class Vector(object):
    """A position or movement in a 2D game."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """self + other: returns a NEW vector."""
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

position = Vector(10, 5)
move = Vector(3, -2)
newPosition = position + move     # really position.__add__(move)
print(newPosition)                # (13, 3)
print(position)                   # (10, 5), unchanged
```

> Your book does the same thing with a Rational (fraction) class: 1/2 + 1/6 makes a new Rational, 2/3.

#### Try it yourself

Add `__sub__` so `a - b` works, and `__mul__` so a vector times a <b>number</b> scales it: `Vector(2, 3) * 4` gives `(8, 12)`.

<details>
<summary>Hint</summary>

`__sub__` looks just like `__add__` with minus signs. In `__mul__`, the other thing is a plain number, so use `self.x * other`, not `other.x`.

</details>

<details>
<summary>One way to do it (try first!)</summary>

```python
class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, number):
        return Vector(self.x * number, self.y * number)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

print(Vector(5, 5) - Vector(2, 1))   # (3, 4)
print(Vector(2, 3) * 4)              # (8, 12)
```

</details>

#### Quick check

**In a + b, which one is self inside `__add__`?**

- a) a
- b) b
- c) Neither, self is the class

<details>
<summary>Answer</summary>

**a) a**

a + b becomes a.`__add__`(b). The left operand is self, the right one is the other parameter.

</details>

#### Watch out for

- Changing `self` inside `__add__` and returning it. Then `a + b` secretly changes `a`. Build and return a new object instead.
- Forgetting to `return`. Then `a + b` gives `None`.

---

## Lesson 6: Comparing objects: ==, &lt; and sorting

_About 15 minutes_

#### The idea

<p>Comparisons work the same way as arithmetic. Each operator runs a method:</p>
<div class="table-wrap"><table>
<tr><th>Operator</th><th>Method</th><th>Operator</th><th>Method</th></tr>
<tr><td><code>==</code></td><td><code>__eq__</code></td><td><code>!=</code></td><td><code>__ne__</code></td></tr>
<tr><td><code>&lt;</code></td><td><code>__lt__</code></td><td><code>&lt;=</code></td><td><code>__le__</code></td></tr>
<tr><td><code>&gt;</code></td><td><code>__gt__</code></td><td><code>&gt;=</code></td><td><code>__ge__</code></td></tr>
</table></div>
<p><b>Why <code>__eq__</code> matters:</b> without it, <code>==</code> only says True if both sides are the <i>exact same object</i>. Two different heroes with identical stats would be "not equal." Usually that's not what you want.</p>
<p>The book's <code>__eq__</code> pattern has three steps: (1) same object? True. (2) different types? False. (3) otherwise, compare the instance variables you care about.</p>
<p><b>Free bonus:</b> if you define <code>__eq__</code>, <code>__lt__</code> and <code>__ge__</code>, Python can figure out <code>!=</code>, <code>&gt;</code> and <code>&lt;=</code> by flipping them around. And once <code>__lt__</code> exists, <code>sort()</code> can sort a list of your objects.</p>

#### See it, then run it

```python
class Score(object):
    """A name and points on a leaderboard."""

    def __init__(self, name, points):
        self.name = name
        self.points = points

    def __eq__(self, other):
        if self is other:                  # exact same object?
            return True
        elif type(self) != type(other):    # not even a Score?
            return False
        else:
            return self.points == other.points

    def __lt__(self, other):
        return self.points < other.points

    def __ge__(self, other):
        return self.points >= other.points

    def __str__(self):
        return self.name + ": " + str(self.points)

a = Score("Mike", 900)
b = Score("Nova", 1200)
print(a < b, a >= b, a == b)          # True False False
print(a == Score("Zed", 900))         # True (same points)
print(a > b, a != b)                  # False True  (free bonus)

board = [b, Score("Zed", 300), a]
board.sort()                          # uses your __lt__
for entry in board:
    print(entry)                      # Zed: 300, Mike: 900, Nova: 1200
```

#### Try it yourself

Give your Song class `__eq__`, `__lt__` and `__ge__` that compare by <b>plays</b>. Make three songs, play them different numbers of times, put them in a list, `sort()` it and print each one.

<details>
<summary>Hint</summary>

Copy the three methods from Score and change `points` to `plays`. Then play each song a different number of times with a loop before sorting.

</details>

<details>
<summary>One way to do it (try first!)</summary>

```python
class Song(object):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.plays = 0

    def play(self):
        self.plays += 1

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.plays == other.plays

    def __lt__(self, other):
        return self.plays < other.plays

    def __ge__(self, other):
        return self.plays >= other.plays

    def __str__(self):
        return self.title + " (" + str(self.plays) + " plays)"

a = Song("Song A", "X")
b = Song("Song B", "Y")
c = Song("Song C", "Z")
for count in range(5):
    a.play()
b.play()
for count in range(3):
    c.play()
songs = [a, b, c]
songs.sort()
for song in songs:
    print(song)        # Song B (1), Song C (3), Song A (5)
```

</details>

#### Quick check

**You didn't write `__eq__`. Two Score objects both have 500 points. What does a == b give?**

- a) True, they have the same points
- b) False, because without `__eq__` Python only checks if they're the exact same object
- c) An error

<details>
<summary>Answer</summary>

**b) False, because without `__eq__` Python only checks if they're the exact same object**

The default `__eq__` uses object identity (is). Two separate objects are never == unless you write your own `__eq__`.

</details>

#### Watch out for

- Forgetting the type check in `__eq__`. Then `myScore == "hello"` crashes with AttributeError, because a string has no `.points`.
- `sort()` sorts the list in place and returns `None`. Write `board.sort()`, not `board = board.sort()`.

---

## Lesson 7: `__repr__`: nicer output in the shell and in lists

_About 5 minutes_

#### The idea

<p>Even with <code>__str__</code>, two things still show the ugly <code>&lt;__main__.Hero object at ...&gt;</code> text:</p>
<ul>
<li>Typing just the variable name in the IDLE shell (no <code>print</code>).</li>
<li><b>Printing a list of your objects.</b> <code>print([a, b])</code> uses each object's <code>__repr__</code>, not <code>__str__</code>.</li>
</ul>
<p>The book's simple fix: add a <code>__repr__</code> that just returns <code>str(self)</code>.</p>

#### See it, then run it

```python
class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):
        """Lets lists and the shell use the nice string too."""
        return str(self)

path = [Vector(0, 0), Vector(1, 2), Vector(3, 3)]
print(path)        # [(0, 0), (1, 2), (3, 3)]
# Without __repr__ you'd see three <__main__.Vector object at ...> blobs
```

#### Try it yourself

Add `__repr__` to your Song class, then print a whole list of songs in one line.

<details>
<summary>Hint</summary>

Same two lines as above: `def __repr__(self):` and `return str(self)`.

</details>

<details>
<summary>One way to do it (try first!)</summary>

```python
class Song(object):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __str__(self):
        return self.title + " by " + self.artist

    def __repr__(self):
        return str(self)

playlist = [Song("A", "X"), Song("B", "Y")]
print(playlist)    # [A by X, B by Y]
```

</details>

#### Quick check

**print(myList) shows ugly &lt;...object at 0x...&gt; text even though your class has `__str__`. Why?**

- a) Lists show their items using `__repr__`, and you didn't write one
- b) `__str__` only works on numbers
- c) You need to call print twice

<details>
<summary>Answer</summary>

**a) Lists show their items using `__repr__`, and you didn't write one**

A list's string uses repr() on each item. Adding `__repr__` that returns str(self) fixes it.

</details>

---

## Lesson 8: Class variables: one value shared by every object

_About 10 minutes_

#### The idea

<p>Some values are the same for <b>every</b> object of a class, like the max health for every hero or the interest rate for every savings account. Storing a copy in every object would be wasteful, so use a <b>class variable</b>.</p>
<ul>
<li>Put it <b>inside the class but outside every method</b>, usually right under the class line.</li>
<li>Name it in ALL CAPS, since it usually acts like a constant.</li>
<li>Use it with the class name in front: <code>Hero.MAX_HEALTH</code>. Plain <code>MAX_HEALTH</code> gives a NameError.</li>
</ul>
<p>Your book's SavingsAccount does this with <code>RATE</code>, and its Card class uses class variables for the list of all suits and ranks.</p>

#### See it, then run it

```python
class Hero(object):
    """A hero whose health is capped."""

    MAX_HEALTH = 100            # class variable: shared by ALL heroes

    def __init__(self, name):
        self.name = name                    # instance variable: per hero
        self.health = Hero.MAX_HEALTH

    def takeDamage(self, amount):
        self.health = max(0, self.health - amount)

    def heal(self, amount):
        self.health += amount
        if self.health > Hero.MAX_HEALTH:
            self.health = Hero.MAX_HEALTH

    def __str__(self):
        return self.name + " " + str(self.health) + "/" + str(Hero.MAX_HEALTH)

mike = Hero("Mike")
mike.takeDamage(40)
mike.heal(100)
print(mike)                  # Mike 100/100
print(Hero.MAX_HEALTH)       # 100: you can use it from outside too
```

> max(0, x) returns whichever is bigger, so health never goes below 0. Same idea as the if statement in Lesson 3.

#### Try it yourself

Add a class variable `MAX_PLAYS = 1000` to Song. Make `play()` stop adding once a song hits MAX\_PLAYS.

<details>
<summary>Hint</summary>

Inside `play`: `if self.plays < Song.MAX_PLAYS:` then add 1.

</details>

<details>
<summary>One way to do it (try first!)</summary>

```python
class Song(object):
    MAX_PLAYS = 1000

    def __init__(self, title):
        self.title = title
        self.plays = 0

    def play(self):
        if self.plays < Song.MAX_PLAYS:
            self.plays += 1

song = Song("Loop")
for count in range(1500):
    song.play()
print(song.plays)        # 1000
```

</details>

#### Quick check

**Each savings account has its own balance, but they all use the same interest rate. Which should be a class variable?**

- a) The balance
- b) The interest rate
- c) Both

<details>
<summary>Answer</summary>

**b) The interest rate**

The rate is shared by every account, so it's a class variable. The balance is different for each account, so it's an instance variable.

</details>

#### Watch out for

- Writing `MAX_HEALTH` alone inside a method. It has to be `Hero.MAX_HEALTH`.
- Using a class variable for something that's different per object, like a name or a balance.

---

## Lesson 9: Objects that hold other objects

_About 15 minutes_

#### The idea

<p>Real programs have classes that <b>work together</b>. A Bank holds SavingsAccounts. A Deck holds Cards. Here, an Inventory holds Items.</p>
<p>The container class keeps the other objects in an instance variable that's a <b>list</b> or a <b>dictionary</b>:</p>
<ul>
<li><b>List</b> when order matters (a deck of cards: top card, shuffle).</li>
<li><b>Dictionary</b> when you look things up by a key (the book's Bank finds accounts by name and PIN).</li>
</ul>
<p>Two tricks from the book's Bank and Deck classes:</p>
<ul>
<li>When something isn't found, <b>return <code>None</code></b>. The caller can check <code>if result:</code> or <code>if result == None:</code>.</li>
<li>Write <code>__len__</code> and then <code>len(myInventory)</code> works, just like <code>__str__</code> makes <code>str()</code> work.</li>
</ul>

#### See it, then run it

```python
class Item(object):
    """Something a hero can carry."""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name + " ($" + str(self.price) + ")"


class Inventory(object):
    """Holds Items, looked up by name."""

    def __init__(self):
        self.items = {}                  # name -> Item

    def add(self, item):
        self.items[item.name] = item

    def get(self, name):
        """Returns the Item, or None if it isn't here."""
        if name in self.items:
            return self.items[name]
        return None

    def remove(self, name):
        """Removes and returns the Item, or None."""
        if name in self.items:
            return self.items.pop(name)
        return None

    def totalValue(self):
        total = 0
        for item in self.items.values():
            total += item.price
        return total

    def __len__(self):
        return len(self.items)

    def __str__(self):
        result = ""
        for item in self.items.values():
            result += str(item) + "\n"
        return result

bag = Inventory()
bag.add(Item("Sword", 50))
bag.add(Item("Potion", 10))
bag.add(Item("Shield", 40))
print(bag)                     # all three items, one per line
print(len(bag))                # 3
print(bag.get("Potion"))       # Potion ($10)
print(bag.get("Laser"))        # None
bag.remove("Sword")
print(bag.totalValue())        # 50
```

> Look at how Inventory never does anything item-specific itself. It asks each Item for its price or its string. Each class handles its own data.

#### Try it yourself

Write a `Playlist` class that holds Songs in a <b>list</b>. Give it `add(song)`, `__len__`, `totalPlays()` and `__str__` (one song per line).

<details>
<summary>Hint</summary>

`self.songs = []` in `__init__`. `add` uses `append`. `totalPlays` loops through `self.songs` adding up `song.plays`.

</details>

<details>
<summary>One way to do it (try first!)</summary>

```python
class Song(object):
    def __init__(self, title):
        self.title = title
        self.plays = 0

    def play(self):
        self.plays += 1

    def __str__(self):
        return self.title + " (" + str(self.plays) + ")"


class Playlist(object):
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)

    def totalPlays(self):
        total = 0
        for song in self.songs:
            total += song.plays
        return total

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        result = ""
        for song in self.songs:
            result += str(song) + "\n"
        return result

mix = Playlist()
a = Song("A")
b = Song("B")
mix.add(a)
mix.add(b)
a.play()
a.play()
b.play()
print(mix)
print(len(mix), mix.totalPlays())    # 2 3
```

</details>

#### Quick check

**Your Bank's get(name, pin) can't find the account. What should it return?**

- a) An empty string
- b) None
- c) It should crash

<details>
<summary>Answer</summary>

**b) None**

None is Python's way of saying "nothing here." The code that called get can check for it.

</details>

#### Watch out for

- Building the string in `__str__` and forgetting `\n`, so all the items run together on one line.
- Printing inside `__str__` instead of building and returning one string.

---

## Lesson 10: Saving objects to a file with pickle

_About 15 minutes_

#### The idea

<p>Turning objects into text and back by hand is a pain. Python's <code>pickle</code> module saves whole objects to a file and loads them back, instance variables and all. (Pickling cucumbers preserves them. Get it?)</p>
<ul>
<li>Open the file with <code>"wb"</code> to save or <code>"rb"</code> to load. The b means binary, because pickle files aren't plain text.</li>
<li><code>pickle.dump(obj, fileObj)</code> saves one object.</li>
<li><code>pickle.load(fileObj)</code> loads the next object. When there's nothing left, it raises an <code>EOFError</code> (End Of File).</li>
</ul>
<p>Since you can't tell ahead of time how many objects are in the file, keep loading in a <code>while True</code> loop and let <code>try</code>/<code>except EOFError</code> catch the end. That's the same try/except from Chapter 9, used for something other than bad input.</p>

#### See it, then run it

```python
import pickle

class Item(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name + " ($" + str(self.price) + ")"

def saveItems(items, fileName):
    """Pickles each item into the file."""
    fileObj = open(fileName, "wb")
    for item in items:
        pickle.dump(item, fileObj)
    fileObj.close()

def loadItems(fileName):
    """Loads items until the file runs out."""
    items = []
    fileObj = open(fileName, "rb")
    while True:
        try:
            item = pickle.load(fileObj)
            items.append(item)
        except EOFError:          # no more objects in the file
            fileObj.close()
            break
    return items

saveItems([Item("Sword", 50), Item("Potion", 10)], "bag.dat")
for item in loadItems("bag.dat"):
    print(item)                   # Sword ($50), then Potion ($10)
```

> The class (Item) has to be defined in the program that loads the file. Pickle saves the data, not the class code.

#### Try it yourself

Make a list of 3 Song objects with different play counts, save them with pickle, load them back into a new list, and print them to prove the play counts survived.

<details>
<summary>Hint</summary>

Reuse `saveItems` and `loadItems` as they are, since they don't care what kind of objects they get. Just swap in your Song class.

</details>

<details>
<summary>One way to do it (try first!)</summary>

```python
import pickle

class Song(object):
    def __init__(self, title, plays):
        self.title = title
        self.plays = plays

    def __str__(self):
        return self.title + " (" + str(self.plays) + " plays)"

def saveAll(objects, fileName):
    fileObj = open(fileName, "wb")
    for obj in objects:
        pickle.dump(obj, fileObj)
    fileObj.close()

def loadAll(fileName):
    result = []
    fileObj = open(fileName, "rb")
    while True:
        try:
            result.append(pickle.load(fileObj))
        except EOFError:
            fileObj.close()
            break
    return result

saveAll([Song("A", 3), Song("B", 10), Song("C", 0)], "songs.dat")
for song in loadAll("songs.dat"):
    print(song)
```

</details>

#### Quick check

**Why does the loading loop need try/except EOFError?**

- a) Because pickle.load raises EOFError when there are no more objects, and that's how you know to stop
- b) Because pickle files are always broken
- c) To catch typos in your class

<details>
<summary>Answer</summary>

**a) Because pickle.load raises EOFError when there are no more objects, and that's how you know to stop**

There's no way to check "is there another object?" first, so you load until it fails with EOFError, then close the file and break.

</details>

#### Watch out for

- Opening with `"w"` or `"r"` instead of `"wb"` / `"rb"`. Pickle needs binary mode.
- Forgetting `break` in the except, so the loop never ends.

---

## Lesson 11: Model/view: keep the data separate from the screen

_About 15 minutes_

#### The idea

<p>The book's ATM case study splits the program into two sets of classes:</p>
<ul>
<li><b>Model</b>: the data and the rules. Bank and SavingsAccount. No <code>input()</code>, no <code>print()</code>, no widgets.</li>
<li><b>View</b>: talks to the human. The ATM window. It reads inputs, asks the model to do the work, and shows the results.</li>
</ul>
<p>Why bother? Because you can swap the view without touching the model. The same Bank could run behind a terminal program, a GUI or a website. And when there's a bug in the math, you know it's in the model, not buried in button code.</p>
<p>The connection: the view keeps a reference to the model in an instance variable, like <code>self.bank = bank</code>. Every button handler goes "get input, call a model method, show what it returns."</p>

#### See it, then run it

```python
import random

class CoinGame(object):
    """MODEL: the data and the rules. No input, print or widgets."""

    def __init__(self):
        self.heads = 0
        self.tails = 0

    def flip(self):
        """Flips once, updates the counts, returns the result."""
        result = random.choice(["Heads", "Tails"])
        if result == "Heads":
            self.heads += 1
        else:
            self.tails += 1
        return result

    def __str__(self):
        return "Heads: " + str(self.heads) + "  Tails: " + str(self.tails)


def playInTerminal():
    """VIEW #1: a terminal view of the same model."""
    game = CoinGame()
    for count in range(5):
        print(game.flip())
    print(game)

playInTerminal()
```

> Now here's a totally different view using the exact same CoinGame class, with zero changes to it.

#### View #2: a GUI for the same model

```python
import random
from breezypythongui import EasyFrame

class CoinGame(object):
    """MODEL (same as above)."""
    def __init__(self):
        self.heads = 0
        self.tails = 0

    def flip(self):
        result = random.choice(["Heads", "Tails"])
        if result == "Heads":
            self.heads += 1
        else:
            self.tails += 1
        return result

    def __str__(self):
        return "Heads: " + str(self.heads) + "  Tails: " + str(self.tails)


class CoinGameGUI(EasyFrame):
    """VIEW: shows the model in a window."""

    def __init__(self, game):
        EasyFrame.__init__(self, title = "Coin Flip", width = 260,
                           height = 120)
        self.game = game                  # the view holds the model
        self.result = self.addLabel(text = "Press Flip", row = 0,
                                    column = 0, sticky = "NSEW")
        self.totals = self.addLabel(text = str(game), row = 1,
                                    column = 0, sticky = "NSEW")
        self.addButton(text = "Flip", row = 2, column = 0,
                       command = self.flip)

    def flip(self):
        self.result["text"] = self.game.flip()     # ask the model
        self.totals["text"] = str(self.game)       # show what it says

def main():
    CoinGameGUI(CoinGame()).mainloop()

if __name__ == "__main__":
    main()
```

> main() makes the model first, then hands it to the view. That's exactly how the book's ATM main() hands a Bank to the ATM window.

#### Try it yourself

Write a model class `Dice` with a `roll()` method that returns a random number from 1 to 6 and keeps a list of every roll. Add a `getAverage()` method. Then write a terminal view function that rolls 10 times and prints each roll and the average.

<details>
<summary>Hint</summary>

`random.randint(1, 6)`. Keep `self.rolls = []` and append each roll. The view function is the only place that uses `print`.

</details>

<details>
<summary>One way to do it (try first!)</summary>

```python
import random

class Dice(object):
    """MODEL"""
    def __init__(self):
        self.rolls = []

    def roll(self):
        value = random.randint(1, 6)
        self.rolls.append(value)
        return value

    def getAverage(self):
        if len(self.rolls) == 0:
            return 0
        return sum(self.rolls) / len(self.rolls)

def terminalView():
    """VIEW"""
    dice = Dice()
    for count in range(10):
        print("Rolled", dice.roll())
    print("Average: %.2f" % dice.getAverage())

terminalView()
```

</details>

#### Quick check

**In a model/view program, where does the code that decides if a withdrawal is allowed go?**

- a) In the view, in the button's event handler
- b) In the model, in the account's withdraw method
- c) In main()

<details>
<summary>Answer</summary>

**b) In the model, in the account's withdraw method**

Rules about the data belong to the model. The view just calls withdraw and shows whatever message comes back.

</details>

#### Watch out for

- Putting `print()` or `input()` inside a model class. If the model prints, you can't reuse it in a GUI.

---

## Lesson 12: A 2D grid class and `__getitem__`

_About 10 minutes_

#### The idea

<p>A grid is rows and columns, like pixels in an image or squares on a game map. The book builds a <code>Grid</code> class whose data is a <b>list of lists</b>: one list per row.</p>
<p>The cool part: write a <code>__getitem__</code> method and square brackets work on your object. <code>grid[2]</code> runs <code>grid.__getitem__(2)</code>, which returns row 2 (a normal list). Then the second <code>[5]</code> is just normal list indexing. So <code>grid[2][5]</code> works for reading <b>and</b> for setting: <code>grid[2][5] = "@"</code>.</p>

#### See it, then run it

```python
class GameMap(object):
    """A 2D map, stored as a list of rows."""

    def __init__(self, rows, columns, fillValue = "."):
        self.data = []
        for row in range(rows):
            rowList = []
            for column in range(columns):
                rowList.append(fillValue)
            self.data.append(rowList)

    def getHeight(self):
        return len(self.data)

    def getWidth(self):
        return len(self.data[0])

    def __getitem__(self, row):
        """Makes map[row][column] work."""
        return self.data[row]

    def find(self, value):
        """Returns (row, column) of value, or None."""
        for row in range(self.getHeight()):
            for column in range(self.getWidth()):
                if self[row][column] == value:
                    return (row, column)
        return None

    def __str__(self):
        result = ""
        for row in self.data:
            result += " ".join(row) + "\n"
        return result

world = GameMap(4, 8)
world[1][2] = "@"           # the player
world[3][7] = "$"           # treasure
print(world)
print(world.find("$"))      # (3, 7)
print(world.find("X"))      # None
```

> " ".join(row) glues the items of a list together with a space between each one.

#### Try it yourself

Add a method `count(value)` that returns how many squares hold `value`. Put three `"$"` on the map and print `world.count("$")`.

<details>
<summary>Hint</summary>

Same nested loops as `find`, but instead of returning on the first match, add 1 to a counter. Return the counter after both loops.

</details>

<details>
<summary>One way to do it (try first!)</summary>

Add the method inside the GameMap class.

```python
    def count(self, value):
        total = 0
        for row in range(self.getHeight()):
            for column in range(self.getWidth()):
                if self[row][column] == value:
                    total += 1
        return total

# Test:
# world[0][0] = "$"; world[2][5] = "$"; world[3][7] = "$"
# print(world.count("$"))     # 3
```

</details>

#### Quick check

**What does world[1] return in the GameMap class?**

- a) The single square at row 1, column 1
- b) The whole row 1, as a list
- c) An error, because GameMap isn't a list

<details>
<summary>Answer</summary>

**b) The whole row 1, as a list**

`__getitem__`(1) returns self.data[1], which is the list for row 1. The second [ ] then picks a column from that list.

</details>

#### Watch out for

- Building every row from the same list (`[rowList] * rows`). Then changing one row changes all of them. Make a fresh list for each row like the example does.

---

## Lesson 13: Inheritance: a new class built on an old one

_About 15 minutes_

#### The idea

<p>You did this in Chapter 9 with EasyFrame. Now with your own classes: <code>class Boss(Hero):</code> means a Boss <b>is a kind of</b> Hero. It gets every Hero method for free, and you add or change only what's different.</p>
<p>Three moves to know:</p>
<ol>
<li><b>Call the parent's constructor first:</b> <code>Hero.__init__(self, name, health)</code>. Each class sets up its own instance variables. Then add the new ones (<code>self.armor = armor</code>).</li>
<li><b>Override</b> a method by defining one with the same name in the subclass. Boss's <code>takeDamage</code> replaces Hero's for bosses only.</li>
<li><b>Reuse the parent's version</b> inside your override: <code>Hero.takeDamage(self, reduced)</code>. Note the class name, the dot, and <code>self</code> passed in by hand.</li>
</ol>
<p>The book's RestrictedSavingsAccount does exactly this. It's a SavingsAccount, but its withdraw checks a counter first, then calls <code>SavingsAccount.withdraw(self, amount)</code> to do the real work.</p>

#### See it, then run it

```python
class Hero(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def takeDamage(self, amount):
        self.health = max(0, self.health - amount)

    def isAlive(self):
        return self.health > 0

    def __str__(self):
        return self.name + " HP " + str(self.health)


class Boss(Hero):
    """A Hero with armor that blocks some damage."""

    def __init__(self, name, health, armor):
        Hero.__init__(self, name, health)   # parent sets up its stuff
        self.armor = armor                  # then add the new stuff

    def takeDamage(self, amount):           # override
        reduced = max(0, amount - self.armor)
        Hero.takeDamage(self, reduced)      # reuse the parent's version

    def __str__(self):                      # override + reuse
        return Hero.__str__(self) + " (armor " + str(self.armor) + ")"

mike = Hero("Mike", 100)
dragon = Boss("Dragon", 300, 15)
mike.takeDamage(20)
dragon.takeDamage(20)       # only 5 gets through the armor
print(mike)                 # Mike HP 80
print(dragon)               # Dragon HP 295 (armor 15)
print(dragon.isAlive())     # True: inherited, never written in Boss
```

#### Try it yourself

Make a `Healer(Hero)` subclass. It has an extra instance variable `mana` (starts at 50) and a new method `heal(other)` that gives the other hero 20 health and costs 10 mana. If mana is under 10, it does nothing.

<details>
<summary>Hint</summary>

In `Healer.__init__`, call `Hero.__init__(self, name, health)` first, then `self.mana = 50`. In `heal`, check mana first, then change `other.health` and `self.mana`.

</details>

<details>
<summary>One way to do it (try first!)</summary>

```python
class Hero(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def __str__(self):
        return self.name + " HP " + str(self.health)


class Healer(Hero):
    def __init__(self, name, health):
        Hero.__init__(self, name, health)
        self.mana = 50

    def heal(self, other):
        if self.mana >= 10:
            other.health += 20
            self.mana -= 10

    def __str__(self):
        return Hero.__str__(self) + " mana " + str(self.mana)

tank = Hero("Tank", 40)
medic = Healer("Medic", 60)
medic.heal(tank)
print(tank)      # Tank HP 60
print(medic)     # Medic HP 60 mana 40
```

</details>

#### Quick check

**Inside Boss.`__init__`, how do you run Hero's constructor?**

- a) Hero.`__init__`(name, health)
- b) Hero.`__init__`(self, name, health)
- c) `__init__`(self, name, health)

<details>
<summary>Answer</summary>

**b) Hero.`__init__`(self, name, health)**

When you call a parent's method through the class name, you have to pass self yourself.

</details>

#### Watch out for

- Skipping `Hero.__init__(self, ...)`. The subclass never gets `self.name` or `self.health`, and you'll hit AttributeError later.
- Forgetting `self` in the parent call: `Hero.takeDamage(reduced)` fails.

---

## Lesson 14: Polymorphism: same method name, different behavior

_About 10 minutes_

#### The idea

<p>Polymorphism sounds scary but it just means "many forms": different classes have methods with the <b>same name</b> that each do their own version of the job.</p>
<p>The payoff: you can loop over a list of mixed objects and call the same method on each one without checking what type it is. Each object does the right thing. <code>__str__</code> is the classic example. Every class has one, and <code>print</code> doesn't care which kind of object it gets.</p>
<p>Your book's examples: <code>withdraw</code> in SavingsAccount vs. RestrictedSavingsAccount, and <code>hit</code> in the blackjack Player vs. Dealer. Same name, different behavior.</p>

#### See it, then run it

```python
class Enemy(object):
    def __init__(self, name):
        self.name = name

    def attack(self):
        return self.name + " pokes you for 5"


class Archer(Enemy):
    def attack(self):                    # same name...
        return self.name + " shoots an arrow for 12"


class Mage(Enemy):
    def attack(self):                    # ...different behavior
        return self.name + " casts fireball for 20"


wave = [Enemy("Slime"), Archer("Robin"), Mage("Merlin"), Enemy("Rat")]
for enemy in wave:
    print(enemy.attack())    # each one runs its OWN attack()
```

> The loop never checks if an enemy is an Archer or a Mage. It just calls attack(), and the object handles the rest. That's polymorphism.

#### Try it yourself

Add a `Ghost(Enemy)` whose attack returns `"... misses (it's a ghost)"` and add one to the wave. Don't change the loop at all.

<details>
<summary>Hint</summary>

A new class with just an `attack` method. Then add `Ghost("Boo")` to the list.

</details>

<details>
<summary>One way to do it (try first!)</summary>

Add this below the other classes. The loop stays exactly the same.

```python
class Ghost(Enemy):
    def attack(self):
        return self.name + " misses (it's a ghost)"

wave = [Enemy("Slime"), Archer("Robin"), Mage("Merlin"), Ghost("Boo")]
for enemy in wave:
    print(enemy.attack())
```

</details>

#### Quick check

**What makes a method polymorphic?**

- a) It has the same name in different classes but a different body in each
- b) It takes a different number of parameters each time
- c) It's defined in the object class

<details>
<summary>Answer</summary>

**a) It has the same name in different classes but a different body in each**

Same header, different definitions in different classes. Callers use one name, and each object does its own version.

</details>

#### Watch out for

- Spelling the method slightly differently in one subclass (`Attack` vs `attack`). Then the parent's version runs instead and you won't know why.

---

## Lesson 15: Fail-safe methods: preconditions and raise

_About 10 minutes_

#### The idea

<p>Sometimes a method only makes sense for certain inputs. Damage can't be negative. A score position has to exist. Those rules are called <b>preconditions</b>. Write them in the docstring so users know.</p>
<p>Then <b>check</b> them at the top of the method. If one is broken, stop with a clear message using <code>raise</code>:</p>
<p><code>raise RuntimeError("damage can't be negative")</code></p>
<p>That's way more helpful than letting the code fail later with some confusing error, or worse, quietly doing something wrong (like a hero <i>gaining</i> health from negative damage).</p>

#### See it, then run it

```python
class Hero(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def takeDamage(self, amount):
        """Lowers health by amount.
        Precondition: amount >= 0"""
        if amount < 0:
            raise RuntimeError("damage can't be negative, got " +
                               str(amount))
        self.health = max(0, self.health - amount)

mike = Hero("Mike", 100)
mike.takeDamage(30)
print(mike.health)          # 70
mike.takeDamage(-50)        # RuntimeError: damage can't be negative, got -50
```

> This one is supposed to end with an error. That's the point: the bad call gets caught right away with a clear message.

#### Try it yourself

Give the Inventory's `add(item)` a precondition: the item's price must be 0 or more. Raise a RuntimeError with a clear message if not.

<details>
<summary>Hint</summary>

First line of `add`: `if item.price < 0:` then `raise RuntimeError(...)`.

</details>

<details>
<summary>One way to do it (try first!)</summary>

Replace add in the Inventory class from Lesson 9.

```python
    def add(self, item):
        """Adds item.
        Precondition: item.price >= 0"""
        if item.price < 0:
            raise RuntimeError("price must be >= 0, got " +
                               str(item.price))
        self.items[item.name] = item
```

</details>

#### Quick check

**Why raise an error instead of just ignoring a bad argument?**

- a) It makes the program run faster
- b) It stops the problem right where it happens, with a clear message, instead of causing weird bugs later
- c) Python requires it

<details>
<summary>Answer</summary>

**b) It stops the problem right where it happens, with a clear message, instead of causing weird bugs later**

A clear error at the source is much easier to fix than a wrong value that causes trouble somewhere else.

</details>

#### Watch out for

- Checking the precondition <i>after</i> already changing the object. Check first, then change.

---

## Exercise map

These match your Cengage assignments (the chapter10 folders in your Codespace). Cengage uses a few different method names than the textbook, so always go by the Cengage instructions. Exercises 10-1, 10-3, 10-5, 10-6, 10-8 and the debug one are autograded task by task, and the rest are graded by your professor.

### 10-1: Compare Student objects

Lessons: [Lesson 6](#lesson-6-comparing-objects---and-sorting)

<details>
<summary>How to start</summary>

Three graded tasks, one per method: `__eq__`, `__lt__` and `__ge__` in Student, each comparing `self.name` with `other.name`. Use the three-step `__eq__` pattern from Lesson 6. Then write a `main()` that makes a few students and prints the comparisons. The instructions show the exact output format, so check yours against it.

</details>

### 10-2: Shuffle and sort students

Lessons: [Lesson 6](#lesson-6-comparing-objects---and-sorting), [Lesson 7](#lesson-7-__repr__-nicer-output-in-the-shell-and-in-lists)

<details>
<summary>How to start</summary>

Cengage tries to copy your 10-1 `student.py` in, but its copy points at the wrong folder, so the file may come up blank. If it does, paste in your finished 10-1 `student.py`. Then make a list of Students, `random.shuffle` it, print each student, `sort()` the list (your `__lt__` does the work), print `Sorted list of students:`, and print each one again with `print(student)`.

</details>

### 10-3: Bank `__str__` sorted by name

Lessons: [Lesson 6](#lesson-6-comparing-objects---and-sorting), [Lesson 9](#lesson-9-objects-that-hold-other-objects)

<details>
<summary>How to start</summary>

Look at the starter `savingsaccount.py` first. It already has `__eq__` and `__lt__` comparing names, so accounts already know how to sort. The real work is in `Bank.__str__`: the accounts live in a dictionary, so get them into a list you can sort, then build the string the same way the original method does.

</details>

### 10-4: ATM: lock out after 3 failures

Lessons: [Lesson 1](#lesson-1-classes-objects-and-__init__), [Lesson 11](#lesson-11-modelview-keep-the-data-separate-from-the-screen)

<details>
<summary>How to start</summary>

Add a counter instance variable in the ATM's `__init__`. In `login`, when the name and PIN don't match, add 1. When it hits 3, pop up a `self.messageBox(...)` saying the police will be called and set `self.loginButton["state"]` to `"disabled"` (Chapter 9, Lessons 5 and 8). It's three <i>in a row</i>, so reset the counter when someone logs in successfully.

</details>

### 10-5: Doctor program, model/view

Lessons: [Lesson 11](#lesson-11-modelview-keep-the-data-separate-from-the-screen)

<details>
<summary>How to start</summary>

The tasks check for a `Doctor` class with three methods named exactly `greeting` (returns `Hello, how can I help you today?`), `farewell` (returns `Have a nice day!`) and `reply(sentence)`. Those methods <b>return</b> strings and never print. Reuse your Chapter 5 doctor code for `reply`. A `main` function does all the `input` and `print`, and stops when the user types quit.

</details>

### 10-6: Craps Player, one roll at a time

Lessons: [Lesson 1](#lesson-1-classes-objects-and-__init__), [Lesson 3](#lesson-3-accessors-and-mutators), [Lesson 4](#lesson-4-how-to-build-a-class-from-scratch-and-when-objects-die)

<details>
<summary>How to start</summary>

Use Cengage's exact names. The methods are `rollDice`, `getNumberOfRolls`, `isWinner` and `isLoser`, and the instance variables are `roll`, `rollsCount`, `atStartup`, `winner` and `loser`. Plan first (Lesson 4): write down each variable's starting value. `rollDice` rolls once, updates the state using the craps rules, and returns the two die values as a tuple. The starter's `getNumberOfRolls` uses the old rolls list, so update it. Then fix `playOneGame` and `playManyGames` to use the new methods.

</details>

### 10-7: Craps game GUI

Lessons: [Lesson 11](#lesson-11-modelview-keep-the-data-separate-from-the-screen)

<details>
<summary>How to start</summary>

Cengage copies your 10-6 `craps.py` in, and its Player is your <b>model</b>. The book's DiceDemo window is your starting <b>view</b>. The Roll button calls `rollDice()`, then updates the dice images and the text area. When `isWinner()` or `isLoser()` is True, show the result and disable Roll until New game makes a fresh Player.

</details>

### 10-8: Cards that face up or down

Lessons: [Lesson 1](#lesson-1-classes-objects-and-__init__), [Lesson 3](#lesson-3-accessors-and-mutators)

<details>
<summary>How to start</summary>

Two tasks. Add `self.faceup = False` in Card's `__init__`, and add a `turn` method that flips it (`not` is your friend). Then update `main` so each line prints the card <i>and</i> its faceup value, like `Ace of Spades False`, and the shuffled deck turns each card before printing it. Heads up: the starter's `Deck.__str__` has a bug (`self.result`), but main doesn't use it.

</details>

### 10-9: Cards GUI

Lessons: [Lesson 11](#lesson-11-modelview-keep-the-data-separate-from-the-screen), [Lesson 9](#lesson-9-objects-that-hold-other-objects)

<details>
<summary>How to start</summary>

Cengage copies your 10-8 `cards.py` in. Deck and Card are the model, and the window is the view (like DiceDemo). Write the helper method they ask for: it takes a Card and returns its image, which is `b.gif` if the card is face down, otherwise the file named from rank and suit letter, like `13s.gif`, in the DECK folder. Turn each card as you deal it, and keep the PhotoImage on `self` (Chapter 9, Lesson 4).

</details>

### 10-10: Shapes with Turtle

Lessons: [Lesson 13](#lesson-13-inheritance-a-new-class-built-on-an-old-one), [Lesson 14](#lesson-14-polymorphism-same-method-name-different-behavior)

<details>
<summary>How to start</summary>

Shape is the parent. It holds the Turtle and the color, set up in its `__init__`. Line, Circle and Rectangle each call `Shape.__init__(self, ...)` first, add their own data, and define their own `draw`. In testshapes.py, put a bunch of shapes in a list and call `draw()` on each one. That's polymorphism. Cengage also requires `turtle.setup()` with the window starting at (0, 0) and `turtle.done()` as the very last line.

</details>

### Debug: Jack's ZeroDivisionError (fix it)

Lessons: [Lesson 15](#lesson-15-fail-safe-methods-preconditions-and-raise)

<details>
<summary>How to start</summary>

Cengage wants you to <b>fix</b> `student.py` so it doesn't crash. Look at the line in the traceback: `sum(self.scores) / len(self.scores)`. What is `len(self.scores)` for `Student("Jack", 0)`? What should the average be when there are no scores at all? Make `getAverageScore` handle that case before it divides.

</details>

---

_Built from your Chapter 10 textbook pages and your Cengage assignment instructions. Every example program was run and tested in Python 3.12._
