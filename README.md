# 🐍 Python 3.10+ Mini-Piscine: Module 03 (Data Quest)

This directory contains production-grade solutions for **Module 03: Mastering Python Collections**. The primary objective of this module is to transition from basic sequential arrays to advanced, memory-efficient data structures (Lists, Tuples, Sets, and Dictionaries) while writing resilient, fully type-hinted code in a simulated gaming environment.

---

## 🛠️ Strict Engineering Standards

All scripts contained within this project strictly adhere to the following enterprise-level constraints mandated by the evaluation guidelines:
1. **Coding Standard:** 100% compliance with `flake8` syntax and style checking (strict 79-character line limit / E501).
2. **Static Type Analysis:** Zero warnings under `mypy` strict type-checking across all functions and methods.
3. **Robustness:** Complete elimination of runtime crashes through proactive exception management (`try-except` blocks).
4. **I/O Constraints:** Zero File I/O operations allowed; all data processing occurs entirely in-memory or via `sys.argv`.

---

## 📂 Repository Structure & Project Summary

### 🎮 ex0: Command Quest (`ex0/ft_command_quest.py`)
* **Core Concept:** Low-level command-line argument manipulation via `sys.argv`.
* **Technical Highlights:** Implements slicing-free pointer operations to extract raw execution paths and isolate target arguments without causing unnecessary heap memory allocations.

### 📊 ex1: Score Cruncher (`ex1/ft_score_analytics.py`)
* **Core Concept:** Algorithmic data filtering and mathematical computing using `list`.
* **Technical Highlights:** Employs the EAFP (Easier to Ask for Forgiveness than Permission) approach via `try-except ValueError` blocks to cleanly split valid numeric game scores from human-input errors. Calculates mathematical variance and bounds in O(N) linear time.

### 📐 ex2: Position Tracker (`ex2/ft_coordinate_system.py`)
* **Core Concept:** Handling immutable data frames via `tuple`.
* **Technical Highlights:** Utilizes read-only 3-element float tuples to lock spatial variables (X, Y, Z), leveraging tuple unpacking features for clean mathematical processing using the Euclidean distance formula.

### 🏆 ex3: Achievement Hunter (`ex3/ft_achievement_tracker.py`)
* **Core Concept:** Set operations and relationship analysis via `set`.
* **Technical Highlights:** Harnesses underlying hash-tables to perform rapid unique matrix processing (`union`, `intersection`, `difference`) across multiple players' tracking profiles in O(1) average lookup complexity. Addresses the E501 linting constraint via implicit line continuation within brackets.

### 🎒 ex4: Inventory Master (`ex4/ft_inventory_system.py`)
* **Core Concept:** Fast lookup mapping via `dict` structures.
* **Technical Highlights:** Parses custom key-value pairs formatted as string arguments (`item:quantity`) into an active tracking structure. Implements an inline lambda expression (`key=lambda k: inventory[k]`) to guarantee structural int evaluation for min/max functions, completely bypassing type-inference bugs inside static checkers.

### 🧙‍♂️ ex5: Stream Wizard (`ex5/ft_data_stream.py`)
* **Core Concept:** Memory-isolated asynchronous streaming pipelines via `typing.Generator` and `yield`.
* **Technical Highlights:** Replaces standard buffer caching with state-preserving generator execution pipelines. Achieves a fixed O(1) spatial footprint by evaluating individual structural changes lazily. Showcases mutable pointer manipulation through the synchronized subtraction of references from an active array wrapper.

---

## 🧠 Core Defense Concepts & Architecture Q&A

### Q1: Why prioritize implicit line continuation over explicit backslashes (`\`) for PEP 8 compliance?
Explicit backslashes (`\`) create brittle code states; accidental trailing spaces immediately trigger invalid syntax exceptions. Utilizing open block boundaries (such as inside round or square brackets) signals the PVM to safely process logical code segments across lines without adding unsafe escape characters.

### Q2: What explains the memory advantage of `yield` over standard arrays?
Standard list compositions allocate large contiguous memory buffers upfront to house all elements simultaneously. In contrast, `yield` structures return custom generator objects that freeze runtime states, local scopes, and execution pointers on the stack. The function runs only when actively polled via a `next()` trigger, evaluating a single isolated object before returning to a paused state.

### Q3: How do lists and tuples behave differently during parameter passing?
In Python, lists are mutable wrappers passed by reference; altering the structure inside a nested routine directly modifies the underlying memory block in the parent scope. Conversely, tuples act as read-only constants; their structural dimensions and indices are sealed at creation, preventing unauthorized modification during runtime operations.
