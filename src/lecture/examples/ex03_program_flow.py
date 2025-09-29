# Control Flow in Python 3 example

print("=== IF / ELIF / ELSE ===")
number = int(input("Enter an integer: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

print("\n=== FOR LOOP with range() ===")
print("Counting from 0 to 4 using range(5):")
for i in range(5):
    print("i =", i)

print("\nCounting from 2 to 6 using range(2, 7):")
for i in range(2, 7):
    print("i =", i)

print("\nCounting even numbers between 0 and 10 using range(0, 11, 2):")
for i in range(0, 11, 2):
    print("i =", i)

print("\n=== WHILE LOOP ===")
print("We will count down from 5 until 1.")

counter = 5
while counter > 0:
    print("Counter =", counter)
    counter -= 1  # decrease the counter by 1
