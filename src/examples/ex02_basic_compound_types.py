# LISTS, TUPLES AND DICTIONARIES
# Run this file on its own. It does not require keyboard input.
# These examples use the indexing and slicing ideas introduced with strings.


# 1. LISTS: AN ORDERED, CHANGEABLE SEQUENCE
print("=== Lists ===")
# Ordered means items have positions; each item has a predecessor (except the first one) and a successor (except the last
# one); having positions does not mean lists are sorted by default.
# Lists allow duplicates. Here we deliberately include 'banana' twice.
fruits = ["apple", "banana", "cherry", "banana"]  # the [] syntax allows you to define a list easily
print("Original list:", fruits)
print("Number of items:", len(fruits))
print("First item:", fruits[0])
print("Last item:", fruits[-1])
# Positive indices here are 0, 1, 2 and 3. fruits[4] would raise IndexError.
# NB! fruits[-1] is not an error, but returns the last fruit in the list

# A list is mutable: its contents can change after it has been created.
fruits.append("orange")  # Add one item at the end.
print("After append:", fruits)
fruits[1] = "blueberry"  # Replace the item at index 1 (the second item).
print("After replacement:", fruits)
fruits.insert(1, "pear")  # Insert before index 1; later items shift right.
print("After insertion:", fruits)

removed_fruit = fruits.pop()  # Remove AND return the last item.
print("Removed:", removed_fruit)
print("After pop:", fruits)
# append() changes the list and returns None (default for functions that do not return anything)
# Do not write fruits = fruits.append("orange"): fruits would become None.

# A slice has the form [start:stop:step]. The stop position is excluded.
# Omitting start/stop uses the beginning/end for the positive steps below.
print("First two items [0:2]:", fruits[0:2])
print("From index 2 onwards [2:]:", fruits[2:])
print("Every second item [::2]:", fruits[::2])
print("Last two items [-2:]:", fruits[-2:])
print("Is 'apple' present?", "apple" in fruits)
print("Is 'mango' absent?", "mango" not in fruits)

# 2. LIST ASSIGNMENT IS A SHALLOW COPY OF THE LIST
print("\n=== Sharing a list versus copying it ===")
scores = [7, 8, 9]
same_scores = scores  # A second name for the SAME list.
copied_scores = scores[:]  # A NEW list containing the same items.

# PREDICT: which of the three printed lists will contain 10?
same_scores[0] = 10
print("Original list:", scores)
print("Second name:", same_scores)
print("Separate copy:", copied_scores)

# 3. TUPLES: A SEQUENCE WHOSE ITEMS CANNOT BE REPLACED
print("\n=== Tuples ===")
position = (10, 20)
print("Position:", position)
print("First coordinate:", position[0])
print("Last coordinate:", position[-1])  # Indexing returns one item: 20.
print("Last coordinate as a tuple:", position[-1:])  # Slicing returns (20,).

# Tuple unpacking assigns each item to a corresponding name.
# The number of names must match the number of items in this example.
x, y = position
print("x =", x, "and y =", y)

# position[0] = 99  # TypeError: tuple items cannot be reassigned.
# Reassigning the NAME is allowed: it makes the name refer to another tuple.
position = (99, 20)
print("New position:", position)

empty_tuple = ()  # () is the syntactically convenient way to define a tuple
one_item_tuple = (10,)  # The comma matters: (10) is just the integer 10.
print("Empty tuple:", empty_tuple)
print("One-item tuple:", one_item_tuple, type(one_item_tuple))
# Like lists, tuples allow duplicates. Both can hold items of different types.
# A tuple can contain a mutable object, such as a list: the tuple fixes its
# item references, but does not prevent that contained list from changing.


# 4. DICTIONARIES: LOOK UP VALUES BY KEY
print("\n=== Dictionaries ===")
student = {
    "name": "Alice",
    "year": 1,
    "group": "911"
}
print("Original dictionary:", student)
print("Student's name:", student["name"])
# Unlike list indexing, this lookup uses a key, not a position.
# student[0] would look for the KEY 0; it would not select the first item.

student["year"] = 2  # Existing key: replace its value.
student["email"] = "alice@example.com"  # New key: add a key-value pair.
print("After update and addition:", student)
print("Number of key-value pairs:", len(student))

# in checks dictionary KEYS, not values.
print("Is there an 'email' key?", "email" in student)
print("Is there an 'Alice' key?", "Alice" in student)
# student["phone"] would raise KeyError because that key does not exist.
print("Phone:", student.get("phone", "not provided"))
# get() returns the supplied default when the key is absent; it adds no key.

del student["email"]
print("After deleting 'email':", student)

# list() collects the keys, values or key-value pairs into a list for display.
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items (pairs represented as tuples):", list(student.items()))

# Keys are unique: assigning to an existing key replaces its value.
# Keys must be hashable. Strings and integers work; lists do not.
