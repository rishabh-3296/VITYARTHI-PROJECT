# 🧮 Tkinter Calculator GUI

This project is a **simple GUI-based Calculator** built using **Python** and the **Tkinter** library.  
It mimics the layout and style of a modern smartphone calculator.

---

## 📋 Features

- GUI built with **Tkinter**
- Display label showing current input / result
- Buttons for:
  - Digits: `0–9`
  - Decimal point: `.`
  - Basic operations: `+`, `-`, `×`, `÷`
  - Percentage: `%`
  - Toggle sign: `+/-`
  - All Clear: `AC`
  - Equals: `=`
- Styled buttons with different colors based on their function

> Note: A button for `√` (square root) exists in the UI layout, but its functionality is **not yet implemented in the logic**.

---

## 🧠 Concepts Used in This Code

This code demonstrates the following Python & Tkinter concepts:

### 🪟 1. Tkinter Window Setup
- Creating the main window using `tkinter.Tk()`
- Setting:
  - Title with `window.title("Calculator")`
  - Non-resizable window with `window.resizable(False, False)`

### 🧱 2. Frames & Layout
- Using `tkinter.Frame` to group and manage widgets
- Using the **grid layout** with `widget.grid(row=..., column=...)` to place:
  - The display label
  - All calculator buttons

### 🏷️ 3. Label Widget
- `tkinter.Label` used as the calculator **display**
- Properties used:
  - `text` (for showing current number/expression)
  - `font` (Arial, size 45)
  - `background` and `foreground`
  - `anchor="e"` to right-align the text
  - `columnspan` to stretch label across multiple columns

### 🔘 4. Button Widget
- `tkinter.Button` used for all calculator keys
- Dynamic creation of buttons using nested loops from `button_values` list
- Each button:
  - Gets its **text** from the layout list
  - Uses `command=lambda value=value: button_clicked(value)`  
    to call the `button_clicked()` function with the correct value

### 🎨 5. Styling & Colors
- Hexadecimal color codes:
  - `color_light_gray = "#D4D4D2"`
  - `color_dark_gray = "#505050"`
  - `color_black = "#1C1C1C"`
  - `color_orange = "#FF9500"`
  - `color_white = "white"`
- Conditional styling:
  - Top row buttons (`AC`, `+/-`, `%`) → light gray
  - Right-side operators (`÷`, `×`, `-`, `+`, `=`) → orange
  - Number buttons → dark gray

### 🧮 6. Calculator Logic & Global Variables
- Global variables:
  - `A` → first operand
  - `B` → second operand
  - `operator` → current arithmetic operator
- Helper functions:
  - `clear_all()` → resets `A`, `B`, and `operator`
  - `remove_zero_decimal(num)` → removes `.0` for whole numbers (e.g., `5.0 → "5"`)
- `button_clicked(value)`:
  - Handles:
    - Digit and decimal input
    - Operator selection (`+`, `-`, `×`, `÷`)
    - Evaluation when `=` is pressed
    - Percentage and sign change
    - Clearing the display and state (`AC`)

---

## 🧾 Code Structure Overview

```text
- Define button layout and symbols
- Define colors
- Create main window and frame
- Create display label
- Dynamically create and style all buttons
- Initialize global variables A, B, operator
- Define helper functions:
  - clear_all()
  - remove_zero_decimal()
  - button_clicked()
- Start Tkinter event loop with window.mainloop()
