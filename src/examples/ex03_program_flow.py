# CONTROLLING PROGRAM FLOW
# Run this file on its own. Enter valid integers when prompted.
# These are small top-level lecture demonstrations. In assignment solutions,
# move calculations into functions and keep input/output separate, as required.


# 1. IF / ELIF / ELSE: CHOOSE ONE BRANCH
print("=== Decisions ===")
number = int(input("Enter an integer (negative, zero or positive): "))

# A colon starts each block; indentation determines which statements belong
# to it. Use four spaces per indentation level, and do not mix tabs and spaces.
# Python uses indentation here instead of C/C++ braces.
if number > 0:
    print("The number is positive.")
elif number == 0:  # elif means 'else if'. Use == for equality, not =.
    print("The number is zero.")
else:
    print("The number is negative.")

# Conditions are checked in order. Only the first matching branch is run.
# This statement is outside all three branches, so it runs in every case.
print("Finished checking the sign.")

# This is a SEPARATE decision, so it runs regardless of the branch above.
if number % 2 == 0:
    print("The number is even.")  # Zero and negative even integers work too.
else:
    print("The number is odd.")

# Use and, or and not to combine or negate Boolean conditions.
# Hover over the line below in PyCharm and check what the 'simplified chain comparison' looks like
if number >= 1 and number <= 10:
    print("The number is in the interval [1, 10].")
if number < -10 or number > 10:
    print("The number is outside the interval [-10, 10].")
is_zero = number == 0
print("The number is not zero:", not is_zero)

# 2. FOR: VISIT EACH ITEM IN A SEQUENCE (remember sequences from lists and tuples?)
print("\n=== Iterating over a list ===")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)
# A Python for loop takes successive items; an index is not always necessary.


# 3. RANGE: GENERATE INTEGER SEQUENCES FOR LOOPS
print("\n=== for with range() ===")
# range(stop): starts at 0, advances by 1, and EXCLUDES stop.
# range() produces a range object, not a list.
print("range(5):")
for index in range(5):
    print(index)  # 0, 1, 2, 3, 4

# range(start, stop): includes start, excludes stop.
print("range(2, 7):")
for number in range(2, 7):
    print(number)  # 2, 3, 4, 5, 6

# range(start, stop, step): step controls the increment; it cannot be zero.
print("range(0, 11, 2):")
for number in range(0, 11, 2):
    print(number)  # 0, 2, 4, 6, 8, 10

print("Countdown with range(5, 0, -1):")
for counter in range(5, 0, -1):
    print(counter)  # 5, 4, 3, 2, 1; stop is still excluded.
# PREDICT: how many times would the body run for range(5, 0) or range(0)?


# 4. AN ACCUMULATOR: BUILD A RESULT STEP BY STEP
print("\n=== Computing a total ===")
scores = [7, 10, 8]
total = 0  # Initialise ONCE, before entering the loop.
for score in scores:
    # simplified, C-style syntax would also work: total += score
    total = total + score
    print("After adding", score, "the total is", total)
print("Final total:", total)
# Trace total: 0 -> 7 -> 17 -> 25. With an empty list, it would remain 0.
# Putting total = 0 inside the loop would incorrectly reset it every time.
# Python also has sum(scores); here we write the loop to understand the steps.


# 5. WHILE: REPEAT WHILE A CONDITION IS TRUE
print("\n=== while countdown ===")
counter = 5
while counter > 0:
    print("Counter:", counter)
    counter -= 1  # For this integer, equivalent to counter = counter - 1.
print("After the loop, counter is", counter)
# The condition is tested BEFORE each iteration. Starting at 0 would skip
# the body. Removing the decrement would make this loop run forever.


# 6. BREAK: LEAVE THE INNERMOST LOOP IMMEDIATELY
print("\n=== Reading until a stop value ===")
# A sentinel is a special input meaning 'stop'. Here it is 0, and it is NOT
# included in the total or count. Negative integers are valid data too.
total = 0
count = 0
while True:
    number = int(input("Enter an integer to add (0 to finish): "))
    if number == 0:
        break
    total += number  # Equivalent here to total = total + number.
    count += 1

print("Numbers entered:", count)
print("Their total:", total)
if count > 0:
    print("Their average:", total / count)
else:
    print("No numbers were entered, so there is no average.")
# Checking count prevents division by zero when the first input is 0.


# 7. CONTINUE: SKIP THE REST OF THE CURRENT ITERATION
print("\n=== Skipping negative values ===")
measurements = [3, -1, 0, -2, 5]
for measurement in measurements:
    if measurement < 0:
        continue
    print("Non-negative measurement:", measurement)
# Unlike break, continue does not end the loop. Output: 3, 0, 5.
# Here an if measurement >= 0 would also work; continue is shown explicitly.

# TRY IT:
# 1. Run the first section with -3, 0 and 4. Predict both sign and parity.
# 2. Sum the integers from 1 through n using range(). What happens for n = 0?
# 3. In the sentinel loop, also count how many entered numbers are positive.
# 4. Replace continue with break above and predict how the output changes.
