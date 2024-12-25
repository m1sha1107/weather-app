# Tkinter Calculator

## Description
This project is a GUI-based calculator built using Python's Tkinter library. The calculator supports basic arithmetic operations including addition, subtraction, multiplication, division, and modulus. Users can interact with the buttons to input numbers and perform calculations.

---

## Features
1. **Basic Arithmetic Operations**:
   - Addition (+)
   - Subtraction (-)
   - Multiplication (*)
   - Division (/)
   - Modulus (%)
2. **Clear Functionality**:
   - A button to reset the input field and start fresh.
3. **Backspace Functionality**:
   - A button to delete the last character in the input field.
4. **Dynamic Input Handling**:
   - Concatenates input dynamically as buttons are clicked.
5. **Error Handling**:
   - Prevents division by zero and displays an appropriate error message.

---

## Requirements
- Python 3.x
- Tkinter library (pre-installed with Python)

---

## How to Run
1. Ensure Python is installed on your system.
2. Save the script as `calculator.py`.
3. Open a terminal or command prompt in the directory containing the script.
4. Run the script using:
   ```
   python calculator.py
   ```
5. The calculator window will appear. Use the buttons to perform calculations.

---

## Code Structure
### Key Functions
- **clicked(n):**
  Handles button clicks and updates the input field dynamically.

- **equals():**
  - Identifies the operation based on the input string.
  - Performs the appropriate calculation (addition, subtraction, multiplication, division, or modulus).
  - Handles division by zero errors.

- **clear():**
  Clears the input field and resets all flags.

- **delete():**
  Deletes the last character in the input field.

### Button Mapping
- Buttons for digits `0-9`.
- Buttons for operations: `+`, `-`, `*`, `/`, `%`.
- Buttons for clear (`Clear`) and backspace (`Backspace`).
- Equals (`=`) button to evaluate expressions.

---

## Example Usage
1. To add two numbers:
   - Click `5` → `+` → `3` → `=`
   - The result `8` will be displayed.

2. To calculate modulus:
   - Click `9` → `%` → `4` → `=`
   - The result `1` will be displayed.

3. To handle errors:
   - Division by zero (e.g., `5` → `/` → `0` → `=`) will display `Error`.

---

## Future Enhancements
- Add support for parentheses to handle complex expressions.
- Implement memory functions like M+, M-, MR.
- Add a scientific mode for advanced calculations.


