# Spaceport Control: Clear for Landing?
The university has opened a spaceport. Unfortunately, its landing-control software was written by an intern who has just left for Mars. Your job is to build a small replacement before the next spaceship arrives.

Every arriving spaceship transmits a non-negative integer **landing code**. The spaceport uses a deliberately simple, fictional rule to decide what happens next:

1. Calculate the **checksum**, defined as the sum of the code's decimal digits.
2. Calculate the remainder when the checksum is divided by 3.
3. Use that remainder to decide the spaceship's landing status.

| Remainder | Status | Message |
| --- | --- | --- |
| 0 | `CLEARED` | Welcome! You may land. |
| 1 | `MANUAL CHECK` | Please wait while we find someone responsible. |
| 2 | `HOLD` | Stay in orbit. The coffee machine is blocking the runway. |

For example, code `2026` has checksum `10`, so its status is `MANUAL CHECK`.

Build the application in the stages below. **Each completed stage must leave a runnable program.** A single Python file, `spaceport.py`, is sufficient. Here, modular means dividing responsibilities between functions; multiple source files are not required.

### Stage 1 — The control tower is online
Ask the operator for their name and one landing code. Greet the operator and display the received code with a meaningful label.
At this stage, the program may simply report that inspection is not yet available, then end normally.

Example:

```text
Operator name: Ada
Welcome to Spaceport Control, Ada!
Landing code (non-negative integer): 2026
Received landing code: 2026
Inspection is not yet available.
```

### Stage 2 — Inspect one landing code

Write a function that receives a non-negative integer and returns the sum of its digits. Use integer arithmetic and a loop: extract a digit using `% 10` and remove it using `// 10`.

Then write a separate function that receives the checksum and returns the appropriate status string. Use `if`, `elif`, and `else`.

The program must now read one code and display its code, checksum, status, and corresponding message. It must still work without a menu or flight log.

Before implementing a calculation function, write its specification: what the parameters mean, what inputs are valid, and what the function returns. Neither calculation function may call `input()` or `print()`.

### Stage 3 — Create an inspection report

Represent one completed inspection using a dictionary with these three keys:

```python
{"code": 2026, "checksum": 10, "status": "MANUAL CHECK"}
```

Write a function that receives a landing code, calls the calculation functions, and returns a new report dictionary. Write a separate function that displays a report and the appropriate message.

The program still processes just one spaceship. Its observable behaviour can remain the same as in Stage 2; the report now groups related values and makes later features easier to add.

### Stage 4 — Keep the control tower open

After greeting the operator once, repeatedly display a menu:

```text
1. Inspect a landing code
0. Close the control tower
```

Option `1` reads a code and displays its report. Option `0` prints a farewell and ends the program. Any other menu choice displays `Unknown option.` and returns to the menu.

Keep menu choices as strings. There is no reason to convert a choice to an integer simply to compare it with `"1"` or `"0"`.

### Stage 5 — Add the flight log

Store every completed report in a list, in inspection order. Add one menu option:

```text
2. Show the flight log
```

Use a `for` loop to display the reports, reusing the report-display function. Show `No spaceships inspected yet.` when the log is empty. Display the total number of inspections using `len()`.

Inspecting the same code twice produces two log entries: these are separate arrivals. Viewing the log must not add or change any entries. The log lasts only until the program exits.

### Input assumptions and implementation rules

- For this introductory version, assume landing-code input contains one or more ASCII decimal digits (`0`–`9`), with no sign. Handling malformed numeric input is an extension.
- Code `0` is valid and has checksum `0`. Leading zeros have no significance: entering `0007` is equivalent to entering `7`.
- Use descriptive names, normal indentation, and short comments where they explain an intention or decision.
- Keep all application data local to functions. Do not use global or module-level data variables.
- Pass information through parameters and return values. Give each function one responsibility.
- Separate calculations and report construction from console input/output.
- Use only built-in Python facilities. No packages, classes, files, network access, or graphical interface are needed.
- Add menu entries only when their features work. An unfinished extension must not break the completed program.

### Examples to check together

| Landing code | Checksum | Status | Why this example matters |
| --- | ---: | --- | --- |
| `2026` | 10 | `MANUAL CHECK` | Typical multi-digit input |
| `120` | 3 | `CLEARED` | Contains a zero |
| `14` | 5 | `HOLD` | Covers the third status |
| `0` | 0 | `CLEARED` | The digit-processing loop may run zero times |
| `999` | 27 | `CLEARED` | Repeated digits |
| `7` | 7 | `MANUAL CHECK` | Single-digit input |

Also check that exiting immediately works, an unknown menu choice does not end the program, and the flight log behaves correctly both before and after an inspection.

### Optional missions

These are extensions beyond the core session, not prerequisites for a working program.

1. **Traffic summary:** count how many reports have each status and return the counts in a dictionary. Print the result separately.
2. **Suspicious transmission:** count how many times each digit occurs in a code, including the case of code `0`.
3. **Safer console:** reject malformed landing-code input and ask again. Keep input validation outside the calculation functions.
