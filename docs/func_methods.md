
# 🧰 Common Python Functions and Methods for Cybersecurity, Engineering, and DevOps

This guide serves as a practical reference for Python's most common functions and methods, especially useful when working in **security automation**, **DevOps scripting**, and **general system engineering**. Each section links directly to use-case scripts in this folder.

### File Handling
- **Syntax**: `open()`, `with open()`, `read()`, `write()`
    - **Usage**:
        - `open()`: Opens a file for reading, writing, or appending.
        - `with open()`: Ensures proper resource management by automatically closing the file.
        - `read()`: Reads the content of a file.
        - `write()`: Writes data to a file.



### String Manipulation
- **Syntax**: `.upper()`, `.lower()`, `.replace()`, `.split()`, `.join()`
    - **Usage**:
        - `.upper()`: Converts a string to uppercase.
        - `.lower()`: Converts a string to lowercase.
        - `.replace()`: Replaces occurrences of a substring with another substring.
        - `.split()`: Splits a string into a list based on a delimiter.
        - `.join()`: Joins elements of a list into a single string with a specified delimiter.



### Iteration & Comprehensions
- **Syntax**: `for`, `while`, `[expression for item in iterable]`
    - **Usage**:
        - `for`: Iterates over items in a sequence (e.g., list, tuple).
        - `while`: Repeats a block of code while a condition is true.
        - `[expression for item in iterable]`: Creates a new list by applying an expression to each item in an iterable.



### Built-ins & Data Structures
- **Syntax**: `len()`, `sorted()`, `dict()`, `list()`, `set()`, `tuple()`
    - **Usage**:
        - `len()`: Returns the length of an object (e.g., list, string).
        - `sorted()`: Returns a sorted version of an iterable.
        - `dict()`: Creates a dictionary.
        - `list()`: Creates a list.
        - `set()`: Creates a set (unique elements).
        - `tuple()`: Creates a tuple (immutable sequence).



### Regex Basics
- **Syntax**: `re.search()`, `re.match()`, `re.findall()`, `re.sub()`
    - **Usage**:
        - `re.search()`: Searches for a pattern anywhere in a string.
        - `re.match()`: Matches a pattern at the beginning of a string.
        - `re.findall()`: Finds all occurrences of a pattern in a string.
        - `re.sub()`: Replaces occurrences of a pattern with a specified string.



### Error Handling & Debugging
- **Syntax**: `try`, `except`, `finally`, `raise`
    - **Usage**:
        - `try`: Defines a block of code to test for exceptions.
        - `except`: Handles exceptions that occur in the `try` block.
        - `finally`: Executes code regardless of whether an exception occurred.
        - `raise`: Manually raises an exception.



## 🧠 Tip for Learners

These functions are **building blocks** used in everything from:
- parsing logs,
- handling configuration files,
- interacting with OS environments,
- scanning networks,
- or automating security scripts.





# 🧰 Common Python Functions and Methods for Cybersecurity, Engineering, and DevOps

This guide serves as a practical reference for Python's most common functions and methods, especially useful when working in **security automation**, **DevOps scripting**, and **general system engineering**. Each section links directly to use-case scripts in this folder.

---

## 📂 File Handling
**Common Methods:** `open()`, `with open()`, `.read()`, `.write()`, `.readlines()`

| Function | Purpose |
|----------|---------|
| `open()` | Opens a file in various modes (`r`, `w`, `a`, `rb`, etc.) |
| `with open()` | Automatically closes file, even on error |
| `.read()` | Reads the entire file as a string |
| `.readlines()` | Reads the file line by line into a list |
| `.write()` | Writes a string to the file |

🔗 See: [`file_handling.py`](file_handling.py)

---

## 🔤 String Manipulation
**Common Methods:** `.upper()`, `.lower()`, `.replace()`, `.split()`, `.join()`

| Method | Description |
|--------|-------------|
| `.upper()` / `.lower()` | Changes case |
| `.replace()` | Replace substrings |
| `.split(delimiter)` | Splits a string into a list |
| `.join(list)` | Joins elements with a delimiter |
| `.strip()` | Trims whitespace or characters |

🔗 See: [`string_operations.py`](string_operations.py)

---

## 🔁 Iteration & Comprehensions

**Syntax:** `for`, `while`, `[x for x in iterable]`, `enumerate()`, `zip()`

| Construct | Use Case |
|----------|----------|
| `for item in iterable:` | Loop through items |
| `while condition:` | Loop as long as condition is True |
| `enumerate()` | Loop with index and value |
| `zip()` | Loop through multiple iterables in parallel |
| `[x for x in iterable]` | Create new list (list comprehension) |

🔗 See: [`iteration_examples.py`](iteration_examples.py)

---

## 🧮 Built-ins & Data Structures

**Common Built-ins:** `len()`, `sorted()`, `dict()`, `set()`, `list()`, `tuple()`, `sum()`, `min()`, `max()`

| Function | Description |
|----------|-------------|
| `len()` | Get number of elements |
| `sorted()` | Return a sorted version of iterable |
| `dict()`, `list()`, `set()`, `tuple()` | Create new data structures |
| `sum()`, `min()`, `max()` | Aggregate functions for numeric data |

🔗 See: [`builtin_helpers.py`](builtin_helpers.py)

---

## 📦 Collections Module

**Common Tools:** `Counter`, `defaultdict`, `deque`, `namedtuple`

| Tool | Use Case |
|------|----------|
| `Counter()` | Count elements in iterable |
| `defaultdict()` | Auto-create default values in a dict |
| `deque()` | Double-ended queue for fast append/popleft |
| `namedtuple()` | Lightweight, immutable object-like structures |

🔗 See: [`collections_examples.py`](collections_examples.py)

---

## 🔍 Regex Basics

**Key Functions from `re` Module:** `search()`, `match()`, `findall()`, `sub()`, `compile()`

| Function | Use Case |
|----------|----------|
| `re.search()` | Find a match anywhere |
| `re.match()` | Match only at the beginning |
| `re.findall()` | Return all matches in a list |
| `re.sub()` | Replace pattern with new text |
| `re.compile()` | Precompile pattern for reuse (better performance) |

🔗 See: [`regex_examples.py`](regex_examples.py)

---

## 🧪 Error Handling & Debugging

**Syntax:** `try`, `except`, `finally`, `raise`, `assert`

| Statement | Description |
|-----------|-------------|
| `try` / `except` | Catch and handle exceptions |
| `finally` | Code that always runs, even after error |
| `raise` | Manually raise an exception |
| `assert` | Sanity checks, often used in testing |

🔗 See: [`error_handling.py`](error_handling.py)

---

## 🧠 Tip for Learners

These functions are **building blocks** used in everything from:
- parsing logs,
- handling configuration files,
- interacting with OS environments,
- scanning networks,
- or automating security scripts.

Make sure to **experiment with the example `.py` scripts** and expand this document as you grow.

---

