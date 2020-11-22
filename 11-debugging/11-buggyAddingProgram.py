# You can run your program in bult-in debugger from code editors and IDEs.
# PyCharm, VSCode and Mu Editor are some examples that have debuggers.

# When you execute Mu's debugger you have some options:
# -> Stop (Stop the debugger)
# -> Continue (The program executes normally until it terminates or reaches a breakpoint)
# -> Step over (Executes next line of code, if it is a function it'll "step over" the function
# code)
# -> Step in (Executes next line of code and pauses again, if next line is a function call,
# the debugger will "step into" that function going to the 1st line inside it.
# If you use it in a line with a built-in function of Python it should skip it, like
# print, though in my case it didn't skip the input function from Python.
# -> Step out (Executes line of code until returns from current function, useful for
# skipping a function code if you're inside it)

print('Enter the first number to add: ')
first = input()
print('Enter the second number to add: ')
second = input()
print('Enter the third number to add: ')
third = input()
print('The sum is ' + first + second + third)
