# Introduction to Python data structures: Lists, Tuples, and Dictionaries
print("Python Data Structures: Lists, Tuples, and Dictionaries\n")

# --- Lists ---
print("Lists:")
# Lists are ordered, mutable (can be changed), and allow duplicates.
fruits = ["apple", "banana", "cherry", "banana"]

print("Original list of fruits:", fruits)

# Adding an item to a list
fruits.append("orange")
print("After append:", fruits)

# Changing an item (mutable)
fruits[1] = "blueberry"
print("After changing the element on index 1:", fruits)

# Slicing lists
print("First two fruits (slicing [0:2]):", fruits[0:2]) # notice the slicing operator indices
print("Every second fruit (slicing [::2]):", fruits[::2]) # notice that not all indices are mandatory
print()

# --- Tuples ---
print("Tuples:")
# Tuples are ordered, immutable (cannot be changed), and allow duplicates.
coordinates = (10, 20, 30, 20)
print("Tuple of coordinates:", coordinates)

# Accessing elements is allowed
print("First coordinate:", coordinates[0])

# Tuples are immutable, so this would cause an error:
# coordinates[0] = 99

# Slicing tuples
# Slicing has the same rules for all supported data types, making it easy to use
print("First two coordinates (slicing [0:2]):", coordinates[0:2])
print("Last coordinate (slicing [-1:]):", coordinates[-1:])
print()

# --- Dictionaries ---
print("Dictionaries:")
# Dictionaries are collections of key-value pairs.
# Keys must be unique and immutable (like strings, numbers, tuples).
person = {
    "name": "Alice",
    "age": 30,
    "job": "Engineer"
}

print("Original dictionary:", person)

# Accessing values
print("Person's name:", person["name"])

# Changing values
person["age"] = 31
print("After updating age:", person)

# Adding a new key-value pair
person["city"] = "Paris"
print("After adding city:", person)

# Keys vs Values
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))
print("Items (key-value pairs):", list(person.items()))

print("\n=== Summary ===")
print("Lists -> Ordered, mutable, allow duplicates.")
print("Tuples -> Ordered, immutable, allow duplicates.")
print("Dictionaries -> Unordered (in Python 3.7+ they preserve insertion order), key-value pairs, keys must be unique.")
