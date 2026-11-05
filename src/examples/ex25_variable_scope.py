"""
Variable scope: predict, run, explain.
Adapted from http://www.python-course.eu/global_vs_local_variables.php

Uncomment ONE section below and run the file in a fresh Python process.
Comment it out again before trying another section. All sections are initially
commented so that names from one example cannot accidentally affect another.
Before running, predict the output or the line that raises an exception.

Assignment to a name normally makes it local to the whole function.
Changing an object through a name is different from assigning to that name
"""

#############################
"""
1. Reading a global name
Does reading a name require a local assignment?
Expected: Hello
The function reads a module-level name: this is a hidden dependency.
"""

# def show_message():
#     print(message)
#
# message = "Hello"
# show_message()

#############################
"""
2. Local assignment and shadowing
Does assigning to message inside the function change the global message?
Expected: Local, then Global (on separate lines).
The two names have separate bindings.
"""

# def show_message():
#     message = "Local"
#     print(message)
#
# message = "Global"
# show_message()
# print(message)

#############################
"""
3. Reading a local name before assigning to it
Does the first print fall back to the global message?
Expected: UnboundLocalError at print(message) inside the function.
The later assignment makes message local throughout the function.
No output is printed before the exception.
"""

# def show_message():
#     print(message)
#     message = "Local"
#
# message = "Global"
# show_message()

#############################
"""
4. Indentation does not necessarily introduce a scope
Can we use result after the if statement? Can we use it outside the function?
Expected: 10, then 10. An ordinary if/for/while suite has no separate scope.
If the condition were False, result would never be assigned and the return
would raise UnboundLocalError. Visibility does not guarantee an assigned value.
"""

# def calculate():
#     if True:
#         result = 10
#     print(result)
#     return result
#
# answer = calculate()
# print(answer)

#############################
"""
5. A local name is not visible to the caller
Expected: Local, followed by NameError at the final print (NB! Error might be displayed before the Local
string, due to the way output streams are merged by PyCharm) 
A returned object can outlive a call, but a function's local names do not
become names in the caller.
"""

# def show_message():
#     message = "Local"
#     print(message)
#
# show_message()
# print(message)

#############################
"""
6. Explicitly rebinding a global name
Expected: Before, then After.
This demonstrates global; it is NOT the design to use in the assignments.

WARNING: The function changes state that its parameter list does not reveal.
"""

# def change_message():
#     global message
#     message = "After"
#
# message = "Before"
# print(message)
# change_message()
# print(message)

#############################
"""
7. Refactoring a hidden dependency into an explicit interface
Expected: Before, Before!, Before!
add_exclamation returns a value; the caller chooses whether to rebind message.
It does not print, change a global binding, or modify its argument.
Questions: Can you test it without console input? Can you reuse it for another
message? What would assert add_exclamation("Hi") == "Hi!" check?
Optional: inspect the text binding in the debugger or with locals().
"""

# def add_exclamation(text):
#     return text + "!"
#
# message = "Before"
# result = add_exclamation(message)
# print(message)
# print(result)
# message = result
# print(message)
