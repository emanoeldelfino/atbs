# My Answers to the Practice Questions

## 1 - Python Basics
1. \* is an operator (multiplication)
   'hello' is a value (string)
   -88.8 is value (float, decimal)
   \- is an operator (subtraction or negative)
   / is an operator (division or concatenation for Path objects from pathlib)
   \+ is an operator (sum or concatenation)
   5 is a value (integer)
   In short +, -, * and / are operators and ‘hello’, 5 and -88.8 are values.
2. spam with no single quotes is a variable while 'spam' is a string.
3. The three most basic data types are integers, floating-point numbers and strings.
4. An expression is made up of values and operators and they can all evaluate (reduce) down to a single value. This means you can them in the same places values are used.
5. An expression is a combination of values and operators and can evaluate down to a single value, so it means if you can use a value somewhere you can also use an expression.
6. Bacon variable is 20. bacon + 1 doesn’t take any effect on the bacon variable, so it remains with the value 20.
7. They both evaluate to ‘spamspamspam’. The first does a concatenation while the last replicates (multiplies) the string ‘spam’ three times evaluating to a single string.
8. eggs is valid, while 100 is invalid because variables can’t start with numbers and its naming needs to follow a set of rules, otherwise they’re invalid like 100 in this case, if it were \_100 it would be valid, as variable names accept to begin with underscores.
9. **int()**, **float()** and __str()__ functions will evaluate to integer, floating-point numbers and string versions of the value passed to them.
10. It causes a TypeError because it’s not possible to concatenate a string to a integer, so we can turn the integer 99 into a string:
‘I have eaten ‘ + str(99) + ‘ burritos.’

## 2 - Flow Control
1. Capitalized **True** and __False__, so the first letters are capital while the rest of the word is in lowercase.
2. **and**, **or** and **not**.
3. True and True is True.
   True and False is False.
   False and True is False.
   False and False is False.
   True or True is True.
   True or False is True.
   False or True is True.
   False or False is False.
   not True is False.
   not False is True.
4. False
   False
   True
   False
   False
   True
5. ==, !=, <, >, <= and >=.
6. The equal operator is == is the equal to operator and it compares two values evaluating to a Boolean, while the = is the assignment operator which stores a value in a variable.
7. A condition is much like an expression evaluating to a Boolean value, True or False, but more specific in the context of flow control statements.
8. The blocks are everything inside the if statements:
```
1
print('eggs')
if spam > 5:
	# code	
else:
	# code	
print('spam')

2
	print('bacon')

3
	print('ham')
```
9. Code:
```
if spam == 1:
	print('Hello')
elif spam == 2:
	print('Howdy')
else:
	print('Greetings!')
```
10. Ctrl+C or Ctrl+Z.
11. break will stop the function, moving to the next line after the function call, and continue will skip the current iteration, moving the loop to its start.
12. range(10), range(0, 10) and range(0, 10, 1) evaluate to the same values because of the defaults of range, it has start 0 and step 1 as default. If only one value is given to range it is the last value and 0 is start and 1 default, if two values are given they’re taken as start and last value and step 1 is defined as default.
OBS: The last value is not included, range takes up to its last value but no including it.
13. Code: 
```
for i in range(1, 11):
	print(i)

i = 1
while i <= 10:
	print(i)
	i = i + 1
```
14. The syntax to call it after its import is _module\_name.function()_, so **spam.bacon()**.

## 3 - Functions
1. Functions avoid repetitiveness of code making them more clear and concise, helping in the maintainability and debugging.
2. When the function is called.
3. The **def** keyword creates a function through statement
   **def** *function_name(parameters)*:
4. A function is simply the **def** statement and the body of the function indented right after the **def** statement. A function call moves the program to the function body, executing what is inside the function until hitting the function’s return value.
5. There’s one global scope, whereas local scopes are tied to the amount of defined functions and inner functions, in short, every defined function has its own local scope.
6. The function returns and destroys the local scope, so all the variables inside it are forgotten in the outer scope or global scope.
7. A return value is what a function evaluates to. Return values can be tied to expressions and used as regular values.
8. The default return value for functions without a return statement is None.
9. The **global** keyword followed by the name of the variable forces it to point to the global variable.
10. The data type of **None** which also is the only value of this data type is the **NoneType**.
11. It imports the module named this way or returns a **ModuleNotFoundError** if that doesn’t exist in the same path that the script is being executed.
12. The function can be called through _module_name.function()_, so **spam.bacon()**.
13. You can use **try except** clauses for treating possible exceptions (errors).
14. The **try** clause wrappers the code that can lead to errors, while the except clause is the treatment or response to that error.

## 4 - Lists
1. Empty list value, the same as list(), it is simply a list with no items.
2. spam[2] = ‘hello’
3. spam[3] which evaluates to ‘d’.
4. It evaluates to the last item of the list which is ‘d’.
5. It does a slice until the element in index 2, not including index 2 element, so it evaluates to [‘a’, ‘b’].
6. It looks for ‘cat’ value inside the bacon list and returns the index of the first element it finds in the list with that value which is 1.
7. [3.14, ‘cat’, 11, ‘cat’, True, 99].
8. [3.14, 11, ‘cat’, True].
9. Lists can be concatenated and replicated like strings. The **+** operator add lists and ___*___ with a number replicates the list the specified number of times.
10. **Append** adds an element to the end of the list, whereas **insert** adds an element to a specified index passed as argument to it without overwriting any values in the list.
11. You can use _list_.**remove**(value) for removing the first value found in the list, if it is not found it’s going to throw an error and **del** keyword when you know the index of the value you want to remove like **del** _list_[index] which also throws an error (IndexError exception) if the list has not the passed index.
12. Both are indexed sequence data types. You can do indexing, slicing and iterate over them with for loops, and concatenate and replicate the same way. You can get the length of both with the **len** method and use the **in** and **not in** operators as well. You can consider a string much like a list of single text characters.
13. Lists are mutable data types so you change them, while tuples are immutable data types, so you cannot change it the same way you do with a list.
14. (42,) or tuple([42]).
15. Using the data type functions **tuple**(_list_) and **list**(_tuple_), respectively.
16. They contain a reference to the list's value, so any changes to the list’s value also changes it.
17. **copy.copy()** makes a shallow copy of a list which means it only copies the outer list, **copy.deepcopy()** makes a deep copy of the list which copies the inner lists as well.

## 5- Dictionaries and Structuring Data

1. dict() or {}.
2. dict([(‘foo’, 42)]) or {‘foo’: 42}.
3. A list has defined indexes that start from 0 and increase in 1 by each new item, whereas in a dictionary the indexes, which are called keys, are defined in the code and can be any immutable data types such as integers, floats, strings. Mutable data types like dictionaries, lists can’t be defined as keys in a dictionary.
4. You get an **KeyError** Exception.
5. **‘cat’ in spam** is shorter for **‘cat’ in spam.keys()**, both look for keys with **‘cat’** value in in the **spam** dictionary keys, if it finds it it returns True, otherwise it returns False.
6. **‘cat’ in spam** will look for keys with the **‘cat’** value in the dictionary **spam**, while **‘cat’ in spam.values()** will look for values with the **‘cat’** value in it.
7. spam.setdefault(‘color’, ‘black’).
8. import pprint; pprint.pprint(dict). It’s going to show each key, value pair per line and sorted.

## 6 - Manipulating Strings
1. Escape characters are special characters which are escaped using the ‘\’ character which would be impossible to represent or use without it.
2. **\n** represents a new line, while **\t** represents a tab.
3. You can put a \ backslash in a string escaping it with another backslash, so you have \\ double backslash.
4. Because it’s wrapped by double quotes which are different from single quotes, the other way around is also possible, wrapping a string in a single quote and using a double quote inside it like **‘He said “wow, that is amazing!”, and I left.’**.
5. You can use triple single quotes or triple double quotes which will interpret the stuff inside them literally, so any space you give inside it will convert to a **\n**.
6. ‘e’; ‘Hello’; ‘Hello’; ‘lo, world!’.
7. ‘HELLO’; True; ‘hello’.
8. [‘Remember,’, ‘remember,’, ‘the’, ‘fifth’, ‘of’, ‘November.’]; ‘There-can-be-only-one.’.
9. _str_.**center(**\<int>, [‘char‘]**), _str_.**rjust(**int, char**)**, _str_.**ljust(**int, char**)**.
10. _str_.**strip(**[‘char’]**)** Trims space at the beginning and end of string with default char being space. **lstrip** trims at the beggining, on the left edge of a string, whereas **rstrip** trims at the end, on the right edge of a string.

## 7 - Regular Expressions
1. **compile** through re.**compile**.
2. For not getting conflicts between scape characters of Python and Regular Expressions.
3. It searches inside the string that is passed for the first value that it matches, if there are no matches it returns an AttributeError Exception.
4. We can use the **group** function for that.
5. Group 0: Every digit from 0 to 9, including hyphens; 
   Group 1: First 3 digits from 0 to 9;
   Group 2: Every remaining digits from 0 to 9, after the first hyphen, including the second hyphen.
6. We can use the backslash \ to make an escape, allowing it to be interpreted as matching values inside the regular expression. 
7. If the regular expression has no groups, in other words, parentheses, the **findall** method will return a list, otherwise, it’ll return a list of tuples. Each tuple is equal to one group of the regular expression.
8. It means **or**, so we can create matches that can be one **or** another value.
9. The question mark makes the preceding group optional, so it can have 0 or 1 matches. It also can be used after curly brackets **{}** that are used to establish a range of the preceding group, in other words, the amount of times it can be matched. **{3,5}** means a range from 3 to 5, default matches the maximum of values, with a **?** after **{}**, so **{3,5}?** It’ll match the minimum amount of values.
   These are called **greedy** and **non-greedy** matching. For default it’s **greedy**, so it’ll match as many values as it can, with **?** it’ll be **non-greedy**, matching as few as it can.
   This also applies to **\***_ and **\+**, both create ranges as well, the first one matches zero or more of the preceding group while the second one matches one or more of the preceding group. So *? +? are non-greedy matching, instead of the default greedy matching.
10. __*__ matches zero or more of the preceding group, while + matches one or more of the preceding group.
11. {3} matches exactly 3 of the preceding group, while {3,5} matches a range from 3 to 5, matching as many values as it can if it repeats sequentially, unless a ? is placed after it.
12. \d matches digits which are the numbers from 0 to 9;
    \w matches words composed for letters, numbers and underscore;
    \s matches spaces.
13. In uppercase it’s negation 
    \D don’t match any digit from 0 to 9;
    \W don’t match words composed for letters, numbers and underscores;
    \S don’t match spaces. 
It’s used for not matching, then excluding not desired values.
14. **\*** matches any value as the dot is a wildcard character in regular expressions. It matches everything, except for new lines \n. ? also makes it non-greedy as explained before.
15. [0-9a-z].
16. Using re.IGNORECASE argument, or in short re.I. 
17. It matches any values as said, except for line breaks \n. Using re.DOTALL argument we can also get new lines characters \n, then we can match any possible values.
18. 'X drummers, X pipers, five rings, X hens'.
19. It allows us to write the raw string between multiple lines with comments. It’s useful for bigger and more complex regular expressions that don’t fit in a single line and are also more convoluted, then making comments a need.
20. numRegex = re.compile(r'^(\d{1,3}(,\d{3})+)$|^\d{1,3}$')
21. watanabeRegex = re.compile(r'[A-Z][a-zA-Z]+\sWatanabe')
22. sentenceRegex = re.compile('(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs).', re.I) 
\# or re.IGNORECASE

## 8 - Input Validation
1. No, it doesn’t. We can install it through PIP with the command pip3 install pyinputplus.
2. We use as pyip to create an alias for pyinputplus, so we can easily use its functions while coding, as it is a bit big name, and we are also kind lazy.
3. inputInt() will only accept integer numbers returning it, while inputFloat() will accept both integers and float numbers returning float numbers. If it’s passed an integer, let’s say 2 to inputFloat(), it’ll return 2.0.
4. We can use inputInt() with the arguments min=0 and lessThan=100. There are other options like min=0;max=99, greaterThan=-1;lessThan=100 and greaterThan=-1;max=99.
5. Both receive raw strings which are regular expressions patterns, allowRegexes receives regular expressions patterns/values that we want to match, besides the values that are already matched with the function itself, and blockRegexes receives regular expression patterns/values that we don’t want to match.
6. It’ll throw a pyinputplus exception, pyinputplus.RetryLimitException.
7. That’s simply the default value that’ll be returned by the function if an exception occurs on it.

## 9 - Reading and Writing Files
1. A relative path is relative to the current working directory and never starts with the root folder / on Linux and macOS and C:\ on Windows. 
2. It starts with the root directory/folder which is / on Linux, macOS and C:\ on Windows.
3. It evaluates to the home directory of the Windows system which is related to the user of the machine, in this case it is C:/Users/Al (C:/Users/<user>). / concatenates Path objects, it’s like + operator from Python.
4. It throws a TypeError exception because / is an invalid operator for strings, it works with path objects, but not with strings.
5. os.getcwd() returns the current working directory of the system and os.chdir(path) changes the current working directory to the argument path which can be a relative or absolute path.
6. . is the current working directory in short and .. is the parent directory of current working directory in short.
7. In C:\bacon\eggs\spam.txt C:\bacon\eggs is the dirname and spam.txt is the basename.
8. ‘r’ Read mode which is the default, you can use file.read() to get all the contents from the file or file.readlines() to get each line separated into a list. 
‘w’ Write mode that creates files when they don’t exist and writes contents to that, and also overwrites files when they already exist with file.write(‘string\n’) because it has file.seek(0) which get the cursor to the beginning of the file, hence overwriting it. It is recommended to add line breaks at  the end of each string that is written to the file, because it doesn’t add lines by itself. 
‘a’ Append mode which is append mode that adds to the contents of files with file.seek(last_num) putting the cursor at the end of the file and also creates that if it doesn’t exist, so it doesn't overwrite files as write mode.
9. It becomes empty as soon as it’s opened in write mode because file.seek is set to 0, then it overwrites existing files.
10. read() returns all content of the file in a single large string and readlines() returns a list containing each line of the content of the file.
11. A dictionary as it saves files by using keys with shelf_file[key] = content. And then you can access this data using the same shelf_file[key] as soon as the content is written to that key. You can also use other common methods of dictionaries like keys(), values() and items() (Note that you need to pass the return value of these methods to a list, converting them from shelf file types to Python file types, so it gets visible). If you want you can also delete a specific key added to that shelf file by using del shelf_file[key].

## 10 - Organizing Files
1. shutil.copy() will only copy a single file, while shutil.copytree() will copy an entire folder with all its contents like files and folders.
2. shutil.move() where you’ll pass the first argument as the file, and the second as the same path of the file with a different name. It is also used for moving files as stated by the name of the function.
3. Shutil modules will permanently delete the files/folders, they’re less secure for these kinds of actions, while send2trash as stated by the name will send the files/folders to the trash or recycle bin, so the latter is more secure to not make some mistake deleting an important file.
4. zipfile.ZipFile(file, mode) is equivalent to the open() function. Mode can be either read, write, or append.

## 11 - Debugging
1. assert spam >= 10 | assert spam > 9
2. assert eggs.lower() != bacon.lower()
3. assert False | assert 2 == 1 | assert ‘abc’ == ‘a’
4. import logging and logging.basicConfig(level=logging.DEBUG, format=’ %(asctime)s - %(levelname)s - %(message)s’)
5. import logging and logging.basicConfig(filename=’log.txt’,level=logging.DEBUG, format=’%(asctime)s - %(levelname)s - %(message)s’)
6. DEBUG, INFO, WARNING, ERROR, CRITICAL.
7. logging.disable(logging.CRITICAL).
8. Because it’s possible to disable logging messages and they have more functionalities as well.
9. Step Over executes the next line of code, if it finds a function it’s going to “step over” the code in the function. It’s going to execute the code’s function at full speed and pause as soon as the function call returns, on the other hand Step In will execute the function codes, so the debugger “step into” it, jumping to the first line of code of that function. Step Out executes lines of code at full speed until it returns from the current function. This is useful if you Step In a function and now want to back out. Click it and to “step out” of the current function call.
10. The debugger will stop until the code ends or hits a breakpoint.
11. A breakpoint is a point where the code stops when you hit the Continue button. You shouldn’t use it in if statements inside for loops, but instead inside if statements, so it won’t execute every time the loops iterate.
12. Just click the line number, so a red dot will appear, clicking again will remove the breakpoint.

## 12 - Web Scraping
1. webbrowser is for opening the browser in a specific URL, requests if for downloading files and pages from web, bs4 is for parsing HTML (so you get what you want from the page) and selenium is for opening and control the browser.
2. requests.get() function returns a Response object. You can use text attribute to get the content as a string value.
3. Response.raise_for_status() will check if the download worked, if it doesn't work it raises an Exception, otherwise it does nothing.
4. Response.status_code (attribute) shows the HTTP status code.
5. Through open in write binary mode, so you iterate over chunks of the file to save it:
```
import requests

res = requests.get('https://url')
file = open('filename.extension', 'wb')
for chunk in res.iter_content(chunk_size=100000):
	file.write(chunk)	
```
6. Ctrl + Shift + I or Ctrl + Shift + J (Console) or F12.
7. Just right click the page element and click Inspect.
8. '#main'
9. '.highlight'
10. 'div div'
11. 'button[value="favorite"]'
12. spam.getText()
13. linkElem.attrs
14. Selenium module is import with from selenium import webdriver.
15. find_element_\** will only return the first occurence of the given element as a WebElement object, while find_elements\** will return all occurences of given element as a list of WebElement objects.
16. click() and send_keys('keys') methods simulate mouse clicks and keyboard keys, respectively.
17. Calling submit() method on any elements within a form submits the form.
18. Through forward(), back() and refresh() Webdriver object methods it is possible to simulate the browser buttons with the same name.


