FAQS = [
    {"q": "What is Python?",
     "a": "Python is a high-level, easy-to-read programming language used for web development, data science, AI, automation, and much more. It is known for its simple, English-like syntax."},

    {"q": "How do I install Python?",
     "a": "Go to https://www.python.org/downloads/, download the installer for your OS, run it, and tick 'Add Python to PATH'. Verify by typing  python --version  in your terminal."},

    {"q": "What is pip?",
     "a": "pip is Python's package manager. Use it to install libraries: e.g.  pip install flask  installs Flask. It comes bundled with Python 3.4+."},

    {"q": "What is a virtual environment?",
     "a": "A virtual environment is an isolated Python installation for a single project. Create one with  python -m venv venv , then activate it: on Windows run  venv\\Scripts\\activate , on Mac/Linux run  source venv/bin/activate ."},

    {"q": "What is the difference between a list and a tuple?",
     "a": "A list [1,2,3] is mutable — you can change it after creation. A tuple (1,2,3) is immutable — it cannot be changed. Tuples are faster and used for fixed data."},

    {"q": "What is a dictionary in Python?",
     "a": "A dictionary stores key-value pairs: {'name': 'Ali', 'age': 25}. Keys must be unique. Access values with  d['name'] . Dictionaries are ordered (Python 3.7+) and very fast for lookups."},

    {"q": "How do I read a file in Python?",
     "a": "Use the built-in open() with a 'with' block:\n\n  with open('file.txt', 'r') as f:\n      content = f.read()\n\nThe file closes automatically after the block."},

    {"q": "What is a lambda function?",
     "a": "A lambda is a short anonymous function: square = lambda x: x**2. Useful with map(), filter(), and sorted(), but for anything complex use a regular def function."},

    {"q": "What is object-oriented programming?",
     "a": "OOP organises code into classes (blueprints) and objects (instances). Key ideas: encapsulation (bundling data + methods), inheritance (child classes reuse parent code), and polymorphism (same interface, different behaviour)."},

    {"q": "What is machine learning?",
     "a": "Machine learning lets computers learn patterns from data to make predictions — without being explicitly programmed. Popular Python libraries: scikit-learn, TensorFlow, PyTorch."},

    {"q": "What is an API?",
     "a": "An API (Application Programming Interface) lets two programs talk to each other. Web APIs use HTTP requests to send/receive data (usually JSON). Example: a weather app calling a weather API to get forecasts."},

    {"q": "What is Git?",
     "a": "Git is a version control system that tracks code changes and lets teams collaborate. Key commands: git init, git add, git commit, git push, git pull. GitHub and GitLab host Git repositories online."},

    {"q": "What is a for loop?",
     "a": "A for loop repeats code for each item in a sequence:\n\n  for i in range(5):\n      print(i)\n\nThis prints 0, 1, 2, 3, 4."},

    {"q": "How do I handle exceptions in Python?",
     "a": "Use try/except:\n\n  try:\n      x = 10 / 0\n  except ZeroDivisionError:\n      print('Cannot divide by zero')\n\nAdd  finally:  to run cleanup code regardless of errors."},

    {"q": "What is a DataFrame?",
     "a": "A DataFrame is a table-like data structure from the pandas library — like an Excel sheet in Python. Create one with  pd.DataFrame({'col': [1,2,3]}) . It is the core tool for data analysis in Python."},

    {"q": "What is Flask?",
     "a": "Flask is a lightweight Python web framework for building websites and REST APIs. Install with  pip install flask . It is minimal, flexible, and great for beginners and small-to-medium projects."},

    {"q": "What is the difference between == and is?",
     "a": "'==' checks if two values are equal. 'is' checks if two variables point to the exact same object in memory. Example: [1,2] == [1,2] is True, but [1,2] is [1,2] is False."},

    {"q": "What is recursion?",
     "a": "Recursion is when a function calls itself. Every recursive function needs a base case to stop. Classic example: factorial(n) = n * factorial(n-1), with factorial(0) = 1 as the base case."},

    {"q": "What are Python decorators?",
     "a": "Decorators wrap a function to extend its behaviour without modifying it, using @ syntax. Common examples: @staticmethod, @property, @app.route('/') in Flask. You can also write your own."},

    {"q": "How do I exit Python?",
     "a": "In the interactive shell type exit() or quit() and press Enter. Shortcuts: Ctrl+D on Mac/Linux, Ctrl+Z then Enter on Windows."},

    {"q": "What is the difference between Python 2 and Python 3?",
     "a": "Python 2 is obsolete (end-of-life since 2020). Python 3 is the current version with better Unicode support, cleaner syntax, and active development. Always use Python 3."},

    {"q": "How do I install a package?",
     "a": "Use pip:  pip install package-name . For example  pip install requests . Inside a virtual environment the package is installed only for that project."},

    {"q": "What is a class in Python?",
     "a": "A class is a blueprint for creating objects. Example:\n\n  class Dog:\n      def __init__(self, name):\n          self.name = name\n      def bark(self):\n          return 'Woof!'\n\n  d = Dog('Rex')\n  print(d.bark())"},

    {"q": "What is NumPy?",
     "a": "NumPy is a Python library for fast numerical computing. It provides the ndarray (n-dimensional array) and hundreds of math functions. It is the foundation of pandas, scikit-learn, and most scientific Python tools."},

    {"q": "How do I reverse a list?",
     "a": "Three ways:\n  1. my_list.reverse()       # in-place\n  2. reversed(my_list)       # returns an iterator\n  3. my_list[::-1]           # returns a new reversed list (most Pythonic)"},

    # ── Python — Core Language ──────────────────────────────────
    {"q": "What are Python data types?",
     "a": "Python's built-in data types include: int, float, complex (numbers), str (text), bool (True/False), list, tuple, range (sequences), dict (mapping), set, frozenset (sets), bytes, bytearray, and NoneType. Use type(x) to check any variable's type."},

    {"q": "What is the difference between append and extend in Python?",
     "a": "list.append(x) adds x as a single element at the end — appending a list adds it as one nested item. list.extend(iterable) unpacks the iterable and adds each item individually. Example: [1,2].append([3,4]) → [1,2,[3,4]]; [1,2].extend([3,4]) → [1,2,3,4]."},

    {"q": "What is list comprehension in Python?",
     "a": "List comprehension is a concise way to create lists: [expression for item in iterable if condition]. Example: squares = [x**2 for x in range(10) if x % 2 == 0] creates [0,4,16,36,64]. It is faster and more readable than an equivalent for-loop with append."},

    {"q": "What is a generator in Python?",
     "a": "A generator is a function that uses 'yield' instead of 'return' to produce values one at a time, on demand. It saves memory because it does not build the entire sequence in memory. Example: def count_up(n): yield from range(n). Use next() or a for-loop to consume it."},

    {"q": "What is the difference between range and xrange?",
     "a": "In Python 3, range() is already a lazy object (like Python 2's xrange). Python 2's range() returned a full list; xrange() returned an iterator. In Python 3, xrange no longer exists — just use range()."},

    {"q": "What are *args and **kwargs?",
     "a": "*args lets a function accept any number of positional arguments as a tuple. **kwargs lets it accept any number of keyword arguments as a dict. Example: def f(*args, **kwargs): print(args, kwargs). Call as f(1,2, name='Ali') → args=(1,2), kwargs={'name':'Ali'}."},

    {"q": "What is the global keyword in Python?",
     "a": "The global keyword lets a function read and write a variable defined in the module (global) scope. Without it, assigning inside a function creates a new local variable. Example: global count; count += 1. Use sparingly — global state makes code harder to test."},

    {"q": "What is the nonlocal keyword?",
     "a": "nonlocal lets an inner (nested) function modify a variable in the enclosing function's scope — one level up, but not global. Example: def outer(): x=0; def inner(): nonlocal x; x+=1. Without nonlocal, x inside inner would be treated as a new local."},

    {"q": "What is a Python module?",
     "a": "A module is any .py file containing Python code (functions, classes, variables). Import it with 'import module_name'. Python also has built-in modules (os, sys, math) and third-party ones installed via pip. Use 'from module import name' to import specific items."},

    {"q": "What is a Python package?",
     "a": "A package is a directory containing an __init__.py file and one or more modules. It lets you organise related modules into a namespace. Example: import numpy as np — numpy is a package. You can create your own by making a folder with __init__.py inside."},

    {"q": "What is __init__.py?",
     "a": "__init__.py makes a directory a Python package. It can be empty or contain initialization code that runs when the package is imported. Without it (in Python < 3.3), Python won't treat the directory as a package."},

    {"q": "What is the difference between is and == in Python?",
     "a": "'==' checks value equality — whether two objects contain the same data. 'is' checks identity — whether two variables point to the exact same object in memory. Example: a=[1,2]; b=[1,2]; a==b is True, a is b is False. Always use == for value comparisons."},

    {"q": "What is Python's GIL?",
     "a": "The Global Interpreter Lock (GIL) is a mutex in CPython that prevents multiple threads from executing Python bytecode simultaneously. It simplifies memory management but limits CPU-bound parallelism. Use multiprocessing or async for concurrency; threading works fine for I/O-bound tasks."},

    {"q": "What is a context manager in Python?",
     "a": "A context manager controls setup and teardown around a block of code using the 'with' statement. It must implement __enter__ and __exit__ methods. The most common use is file handling: 'with open(\"f.txt\") as f:' — the file closes automatically even if an exception occurs."},

    {"q": "What is the difference between deepcopy and copy?",
     "a": "copy.copy() creates a shallow copy — the new object references the same nested objects. copy.deepcopy() creates a fully independent copy, recursively duplicating all nested objects. Use deepcopy when you need changes to the copy to not affect the original."},

    {"q": "What are Python magic methods?",
     "a": "Magic (dunder) methods have double underscores: __init__, __str__, __repr__, __len__, __add__, etc. They let you define how objects behave with Python's built-in operations. Example: defining __add__ lets your class use the + operator. __str__ controls what print() shows."},

    {"q": "What is __str__ vs __repr__?",
     "a": "__str__ returns a human-readable string for end users (used by print() and str()). __repr__ returns an unambiguous developer-friendly string (used by repr() and in the REPL). A good __repr__ should ideally let you recreate the object: repr(datetime(2024,1,1)) → 'datetime.datetime(2024, 1, 1, 0, 0)'."},

    {"q": "What is multiple inheritance in Python?",
     "a": "A class can inherit from more than one parent: class C(A, B). Python uses the C3 linearization algorithm (MRO — Method Resolution Order) to determine which parent's method is called. Use super() to cooperatively call parent methods. Check the MRO with ClassName.__mro__."},

    {"q": "What is a property in Python?",
     "a": "The @property decorator lets you define a method that is accessed like an attribute (no parentheses). Pair it with @name.setter and @name.deleter for controlled get/set/delete. Useful for adding validation without breaking the API: obj.age = -1 can raise ValueError via the setter."},

    {"q": "What is the difference between staticmethod and classmethod?",
     "a": "@staticmethod is a regular function inside a class — no implicit first argument, no access to class or instance. @classmethod receives the class itself as the first argument (cls) and can access/modify class state. classmethods are often used as alternative constructors."},

    {"q": "What is monkey patching?",
     "a": "Monkey patching is dynamically replacing or adding attributes/methods to a class or module at runtime. Example: import json; json.loads = my_custom_loads. Useful in testing (mocking) but dangerous in production — it makes code hard to understand and debug."},

    {"q": "What is memoization?",
     "a": "Memoization caches the result of expensive function calls so repeated calls with the same arguments return instantly. Python provides functools.lru_cache for this: @functools.lru_cache(maxsize=None). It's especially powerful for recursive functions like Fibonacci."},

    {"q": "What is the walrus operator?",
     "a": "The walrus operator := (assignment expression, Python 3.8+) assigns a value inside an expression. Example: if (n := len(data)) > 10: print(f'Too long: {n}'). It avoids computing the same value twice and is useful in while loops: while chunk := f.read(8192): process(chunk)."},

    {"q": "What is type hinting in Python?",
     "a": "Type hints annotate variables and function signatures with expected types: def greet(name: str) -> str: return f'Hi {name}'. They don't enforce types at runtime but help IDEs, linters (mypy), and other developers. Use 'from __future__ import annotations' or the typing module for complex types."},

    {"q": "What is the difference between a set and a frozenset?",
     "a": "A set is a mutable, unordered collection of unique items: {1,2,3}. A frozenset is the immutable version: frozenset({1,2,3}). Because frozensets are hashable, they can be used as dictionary keys or elements of another set — regular sets cannot."},

    {"q": "What is unpacking in Python?",
     "a": "Unpacking assigns iterable elements to variables in one line: a, b, c = [1,2,3]. Extended unpacking: first, *rest = [1,2,3,4] → first=1, rest=[2,3,4]. You can unpack in function calls with * for lists and ** for dicts: func(*args, **kwargs)."},

    # ── Python — OOP ─────────────────────────────────────────────
    {"q": "What is encapsulation?",
     "a": "Encapsulation bundles data and the methods that operate on it inside a class, and restricts direct access to some components. In Python, prefix with _ for 'protected' (convention only) or __ for name-mangled 'private' attributes. Use properties/methods to expose controlled access."},

    {"q": "What is inheritance?",
     "a": "Inheritance lets a child class acquire attributes and methods from a parent class. Use super() to call the parent's methods. Example: class Dog(Animal): def speak(self): return 'Woof'. Dog inherits all of Animal's methods and can override or extend them."},

    {"q": "What is polymorphism?",
     "a": "Polymorphism lets different classes be used interchangeably through a shared interface. Example: both Dog and Cat implement speak(), so you can loop over a list of animals and call animal.speak() without knowing the specific type — each responds differently."},

    {"q": "What is abstraction?",
     "a": "Abstraction hides implementation details and exposes only a clean interface. In Python, use the abc module: from abc import ABC, abstractmethod. A class inheriting ABC with @abstractmethod methods cannot be instantiated directly — only concrete subclasses that implement all abstract methods can be."},

    {"q": "What is method overriding?",
     "a": "Method overriding is when a child class provides its own implementation of a method already defined in the parent. The child's version is called instead of the parent's. Use super().method() inside the override if you still want to run the parent's version as well."},

    # ── Python — Error Handling ──────────────────────────────────
    {"q": "What is the difference between Exception and BaseException?",
     "a": "BaseException is the root of all exceptions including SystemExit, KeyboardInterrupt, and GeneratorExit. Exception is a subclass of BaseException and is the base for all non-system-exiting exceptions. Always catch Exception (or specific subclasses) in application code — never catch bare BaseException unless you re-raise it."},

    {"q": "How do I create a custom exception?",
     "a": "Subclass Exception (or a more specific exception): class ValidationError(ValueError): pass. Add a custom __init__ if you need extra data: def __init__(self, field, msg): self.field=field; super().__init__(msg). Raise with: raise ValidationError('email', 'Invalid format')."},

    {"q": "What is the else clause in try/except?",
     "a": "The else block runs only if no exception was raised in the try block. It is better practice than putting success code at the end of the try block, because it won't accidentally catch exceptions raised by your success code. Structure: try / except / else / finally."},

    {"q": "What does raise from do?",
     "a": "'raise NewError(...) from original_error' chains exceptions, preserving the original traceback context. This is useful when you catch one exception and raise a different one: except KeyError as e: raise ValueError('Missing key') from e. Use 'raise ... from None' to suppress the original context."},

    # ── Python — Functional Programming ─────────────────────────
    {"q": "What is map() in Python?",
     "a": "map(function, iterable) applies a function to every item in an iterable and returns a lazy iterator. Example: list(map(str, [1,2,3])) → ['1','2','3']. In modern Python, list comprehensions are often preferred for readability, but map() is useful with existing functions."},

    {"q": "What is filter() in Python?",
     "a": "filter(function, iterable) returns an iterator of items for which the function returns True. Example: list(filter(lambda x: x>0, [-1,2,-3,4])) → [2,4]. Like map(), list comprehension with a condition is often more readable: [x for x in items if x>0]."},

    {"q": "What is reduce() in Python?",
     "a": "functools.reduce(function, iterable) applies a two-argument function cumulatively to reduce the iterable to a single value. Example: reduce(lambda a,b: a+b, [1,2,3,4]) → 10. It was a built-in in Python 2; in Python 3 it moved to functools. sum(), max(), min() cover the most common cases."},

    {"q": "What is a closure in Python?",
     "a": "A closure is a function that remembers variables from its enclosing scope even after that scope has finished. Example: def make_adder(n): return lambda x: x+n. add5=make_adder(5); add5(3) → 8. The inner function 'closes over' n. Closures are the basis for decorators."},

    {"q": "What is functools.partial?",
     "a": "functools.partial creates a new function with some arguments of an existing function pre-filled. Example: from functools import partial; double = partial(pow, exp=2); double(5) → 25. Useful for adapting functions to interfaces that require fewer arguments."},

    # ── Python — Async / Concurrency ────────────────────────────
    {"q": "What is async/await in Python?",
     "a": "async/await enables asynchronous programming using coroutines. An 'async def' function returns a coroutine. 'await' suspends execution until the awaited coroutine completes — without blocking other tasks. Run with asyncio.run(main()). Ideal for I/O-bound tasks like HTTP requests or database queries."},

    {"q": "What is the difference between threading and multiprocessing?",
     "a": "Threading runs multiple threads in the same process sharing memory, but the GIL limits true parallelism for CPU-bound work. Multiprocessing spawns separate processes each with their own Python interpreter and memory — true parallelism for CPU-bound tasks. Use threading for I/O-bound, multiprocessing for CPU-bound work."},

    {"q": "What is asyncio?",
     "a": "asyncio is Python's built-in library for writing concurrent code with async/await. It runs an event loop that manages coroutines. Key functions: asyncio.run(), asyncio.gather() (run multiple coroutines concurrently), asyncio.sleep(), asyncio.create_task(). Libraries like aiohttp and httpx build on asyncio."},

    {"q": "What is a thread-safe operation?",
     "a": "An operation is thread-safe if it produces correct results when called from multiple threads simultaneously. In Python, simple attribute reads/writes and list.append() are thread-safe due to the GIL. For compound operations use threading.Lock(): with lock: counter += 1."},

    # ── Python — Standard Library ────────────────────────────────
    {"q": "What does the os module do?",
     "a": "The os module provides operating-system interfaces: file/directory operations (os.listdir, os.mkdir, os.remove), environment variables (os.environ), path manipulation (os.path.join, os.path.exists), process info (os.getpid), and running shell commands (os.system). Use pathlib for modern path handling."},

    {"q": "What is pathlib in Python?",
     "a": "pathlib.Path is an object-oriented, cross-platform path library (Python 3.4+). It replaces os.path string manipulation: Path('data') / 'file.txt' builds paths, p.read_text() reads files, p.glob('*.csv') finds files, p.exists() checks existence. Much more readable than os.path."},

    {"q": "What is the sys module?",
     "a": "sys provides access to interpreter internals: sys.argv (command-line arguments), sys.path (module search paths), sys.exit() (exit the program), sys.stdin/stdout/stderr (standard streams), sys.version (Python version string), sys.platform (OS identifier)."},

    {"q": "What is the collections module?",
     "a": "collections provides specialised container types: Counter (counts hashable objects), defaultdict (dict with a default value factory), OrderedDict (insertion-ordered dict, mostly redundant in Python 3.7+), deque (fast append/pop from both ends), namedtuple (tuple with named fields)."},

    {"q": "What is itertools?",
     "a": "itertools provides efficient iterators for looping: chain() (flatten iterables), product() (cartesian product), permutations(), combinations(), groupby() (group consecutive items), islice() (slice an iterator), cycle() (repeat infinitely), count() (infinite counter). All are memory-efficient lazy iterators."},

    {"q": "What is the datetime module?",
     "a": "datetime provides date/time types: datetime.date (date only), datetime.time (time only), datetime.datetime (date+time), datetime.timedelta (duration). Key operations: datetime.now(), date.today(), strftime() (format to string), strptime() (parse from string), timedelta arithmetic."},

    {"q": "What is the json module?",
     "a": "json converts between Python objects and JSON strings. json.dumps(obj) serialises to a JSON string; json.loads(s) parses a JSON string to a Python object. json.dump(obj, file) writes to a file; json.load(file) reads from a file. Use indent= for pretty-printing."},

    {"q": "What is the re module?",
     "a": "re provides regular expression operations. Key functions: re.search() (find first match anywhere), re.match() (match at string start), re.findall() (list all matches), re.sub() (replace matches), re.compile() (pre-compile a pattern for reuse). Use raw strings r'\\d+' to avoid double-escaping backslashes."},

    {"q": "What is the math module?",
     "a": "math provides mathematical functions: math.sqrt(), math.floor(), math.ceil(), math.log(), math.sin(), math.cos(), math.pi, math.e, math.factorial(), math.gcd(), math.inf. For complex numbers use cmath. For arrays of numbers, numpy is much faster."},

    {"q": "What is the random module?",
     "a": "random provides pseudo-random number generation: random.random() (0.0–1.0), random.randint(a,b), random.choice(seq), random.shuffle(list), random.sample(pop, k). For cryptographic randomness use the secrets module instead."},

    {"q": "What is pickle in Python?",
     "a": "pickle serialises Python objects to binary format and deserialises them back. pickle.dumps(obj) → bytes; pickle.loads(bytes) → object. pickle.dump(obj, file) / pickle.load(file) for files. Warning: never unpickle data from untrusted sources — it can execute arbitrary code."},

    {"q": "What is the logging module?",
     "a": "logging is Python's standard logging framework. Levels (lowest to highest): DEBUG, INFO, WARNING, ERROR, CRITICAL. Basic setup: logging.basicConfig(level=logging.INFO). Use a module-level logger: logger = logging.getLogger(__name__). Prefer logging over print() in production code."},

    {"q": "What is argparse?",
     "a": "argparse parses command-line arguments. Create a parser, add arguments with add_argument(), then call parse_args(). Example: parser.add_argument('--name', type=str, default='World'). It automatically generates --help text and validates input types."},

    {"q": "What is the csv module?",
     "a": "csv reads and writes CSV files. csv.reader(file) iterates rows as lists; csv.DictReader(file) iterates rows as dicts using the header row as keys. csv.writer(file) writes rows; csv.DictWriter writes dicts. For large data, pandas.read_csv() is much more powerful."},

    # ── Data Structures & Algorithms ────────────────────────────
    {"q": "What is a stack?",
     "a": "A stack is a LIFO (Last-In, First-Out) data structure. Push adds to the top; pop removes from the top. In Python, use a list: stack=[]; stack.append(x) to push; stack.pop() to pop. Or use collections.deque for thread-safe operations. Common uses: undo history, function call stack, expression parsing."},

    {"q": "What is a queue?",
     "a": "A queue is a FIFO (First-In, First-Out) data structure. Enqueue adds to the back; dequeue removes from the front. Use collections.deque: dq.append(x) to enqueue; dq.popleft() to dequeue. For thread-safe queues use queue.Queue from the standard library."},

    {"q": "What is a linked list?",
     "a": "A linked list is a sequence of nodes, each containing data and a pointer to the next node. Unlike arrays, insertions/deletions are O(1) if you have a reference to the node, but access by index is O(n). Python doesn't have a built-in linked list — collections.deque is backed by a doubly-linked list."},

    {"q": "What is a binary tree?",
     "a": "A binary tree is a hierarchical structure where each node has at most two children (left and right). A binary search tree (BST) keeps left < node < right, enabling O(log n) search. Common traversals: in-order (sorted output), pre-order, post-order. Python has no built-in BST; use the sortedcontainers library."},

    {"q": "What is a hash table?",
     "a": "A hash table stores key-value pairs and uses a hash function to map keys to array indices, enabling O(1) average-case get/set/delete. Python's dict is a highly optimised hash table. Collisions are resolved internally. Hash tables underpin dicts, sets, and many caching systems."},

    {"q": "What is Big O notation?",
     "a": "Big O notation describes how an algorithm's time or space requirements grow as input size n increases. Common complexities: O(1) constant, O(log n) logarithmic, O(n) linear, O(n log n) linearithmic, O(n²) quadratic, O(2ⁿ) exponential. It describes worst-case growth, ignoring constants."},

    {"q": "What is binary search?",
     "a": "Binary search finds a target in a sorted array in O(log n) by repeatedly halving the search space. Compare target to the midpoint; if less, search the left half; if greater, search the right half. Python provides bisect.bisect_left() for binary search on sorted lists."},

    {"q": "What is a sorting algorithm?",
     "a": "Sorting algorithms arrange data in order. Key ones: Bubble sort O(n²), Selection sort O(n²), Insertion sort O(n²) but fast for nearly-sorted data, Merge sort O(n log n) stable, Quick sort O(n log n) average but O(n²) worst case, Timsort O(n log n) — Python's built-in sort uses Timsort."},

    {"q": "What is recursion vs iteration?",
     "a": "Recursion solves a problem by having a function call itself with a smaller input until a base case is reached. Iteration uses loops. Recursion can be cleaner for tree/graph problems but risks stack overflow for deep calls. Python's default recursion limit is 1000 (sys.setrecursionlimit). Many recursive solutions can be converted to iteration with an explicit stack."},

    {"q": "What is dynamic programming?",
     "a": "Dynamic programming (DP) solves problems by breaking them into overlapping subproblems and storing results to avoid recomputation (memoization or tabulation). Classic examples: Fibonacci, Knapsack, Longest Common Subsequence, Coin Change. The key insight: optimal solution = combination of optimal sub-solutions."},

    {"q": "What is a graph?",
     "a": "A graph is a set of nodes (vertices) connected by edges. Directed graphs have one-way edges; undirected have two-way. Weighted graphs assign costs to edges. Common algorithms: BFS (shortest path in unweighted graphs), DFS (cycle detection, topological sort), Dijkstra (weighted shortest path). Represent with adjacency lists or matrices."},

    {"q": "What is BFS?",
     "a": "Breadth-First Search (BFS) explores a graph level by level using a queue. It finds the shortest path in unweighted graphs. Start from a source, visit all neighbours, then their neighbours, and so on. Time: O(V+E). Use collections.deque for the queue. Also used for level-order tree traversal."},

    {"q": "What is DFS?",
     "a": "Depth-First Search (DFS) explores as far as possible along each branch before backtracking, using a stack (or recursion). Used for cycle detection, topological sort, connected components, and maze solving. Time: O(V+E). Recursive DFS is elegant but can hit Python's recursion limit for large graphs."},

    # ── Web Development ──────────────────────────────────────────
    {"q": "What is REST?",
     "a": "REST (Representational State Transfer) is an architectural style for APIs. It uses standard HTTP methods: GET (read), POST (create), PUT/PATCH (update), DELETE (remove). Resources are identified by URLs. Responses are typically JSON. REST APIs are stateless — each request contains all needed information."},

    {"q": "What is HTTP?",
     "a": "HTTP (HyperText Transfer Protocol) is the protocol web browsers and servers use to communicate. A client sends a request (method, URL, headers, optional body); the server sends a response (status code, headers, body). HTTPS adds TLS encryption. HTTP/2 and HTTP/3 add multiplexing and performance improvements."},

    {"q": "What are HTTP status codes?",
     "a": "HTTP status codes indicate the result of a request. 1xx: informational. 2xx: success (200 OK, 201 Created, 204 No Content). 3xx: redirection (301 Moved Permanently, 302 Found). 4xx: client error (400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found). 5xx: server error (500 Internal Server Error, 503 Service Unavailable)."},

    {"q": "What is Django?",
     "a": "Django is a full-featured Python web framework following the 'batteries included' philosophy. It provides ORM, admin interface, authentication, URL routing, template engine, form handling, and security features out of the box. Best for larger, content-heavy applications. Install: pip install django."},

    {"q": "What is the difference between Flask and Django?",
     "a": "Flask is minimal and flexible — you choose your own libraries for the database, auth, etc. Django is full-featured and opinionated — it includes everything. Flask is great for APIs and small-to-medium apps; Django shines for large content-driven sites. Both are production-ready and widely used."},

    {"q": "What is FastAPI?",
     "a": "FastAPI is a modern, high-performance Python web framework for building APIs with automatic data validation (via Pydantic) and auto-generated interactive docs (Swagger UI). It uses async/await natively and is one of the fastest Python frameworks. Install: pip install fastapi uvicorn."},

    {"q": "What is a web server?",
     "a": "A web server handles HTTP requests from clients and returns responses — typically HTML, JSON, or files. Popular ones: Nginx and Apache (serve static files, act as reverse proxies), Gunicorn and uWSGI (run Python WSGI apps), Uvicorn (run Python ASGI/async apps). Flask and Django's built-in servers are for development only."},

    {"q": "What is CORS?",
     "a": "CORS (Cross-Origin Resource Sharing) is a browser security mechanism that blocks web pages from making requests to a different domain unless the server explicitly allows it via response headers (Access-Control-Allow-Origin). In Flask: use flask-cors. In Django: use django-cors-headers."},

    {"q": "What is a JSON Web Token (JWT)?",
     "a": "A JWT is a compact, URL-safe token for transmitting claims between parties. Structure: header.payload.signature (base64 encoded, dot-separated). The server signs the token; the client sends it in the Authorization header (Bearer token). The server verifies the signature without a database lookup. Use PyJWT in Python."},

    {"q": "What is middleware?",
     "a": "Middleware is code that sits between a web request and the view/handler, processing the request before it reaches the view and/or the response before it goes back to the client. Common uses: authentication, logging, rate limiting, CORS headers, request timing. Flask uses decorators; Django has a MIDDLEWARE list."},

    {"q": "What is a RESTful API?",
     "a": "A RESTful API follows REST principles: stateless client-server communication, resources identified by URLs, standard HTTP methods for CRUD, uniform interface. Example: GET /users returns all users, POST /users creates one, GET /users/42 returns user 42, PUT /users/42 updates it, DELETE /users/42 removes it."},

    {"q": "What is GraphQL?",
     "a": "GraphQL is a query language for APIs (alternative to REST) developed by Facebook. Clients specify exactly the data they need in a single query, avoiding over-fetching and under-fetching. A single /graphql endpoint handles all operations: queries (read), mutations (write), subscriptions (real-time). Python library: Strawberry or Graphene."},

    {"q": "What is a webhook?",
     "a": "A webhook is an HTTP callback — when an event happens in system A, it sends an HTTP POST to a URL in system B with event data. Unlike polling (system B repeatedly asks system A for updates), webhooks are event-driven and more efficient. Example: GitHub sends a webhook to your server on every push."},

    # ── Databases ────────────────────────────────────────────────
    {"q": "What is SQL?",
     "a": "SQL (Structured Query Language) is the standard language for relational databases. Core commands: SELECT (query data), INSERT (add rows), UPDATE (modify rows), DELETE (remove rows), CREATE TABLE, ALTER TABLE, DROP TABLE. Also: WHERE (filter), JOIN (combine tables), GROUP BY, ORDER BY, LIMIT."},

    {"q": "What is the difference between SQL and NoSQL?",
     "a": "SQL databases (PostgreSQL, MySQL, SQLite) store structured data in tables with a fixed schema, enforce ACID properties, and use SQL to query. NoSQL databases (MongoDB, Redis, Cassandra) store unstructured/semi-structured data, offer flexible schemas, and scale horizontally more easily. Choice depends on data shape and consistency needs."},

    {"q": "What is an ORM?",
     "a": "An ORM (Object-Relational Mapper) lets you interact with a database using Python objects instead of raw SQL. Example (SQLAlchemy): user = User(name='Ali'); db.session.add(user); db.session.commit(). Django has its own built-in ORM. ORMs increase productivity but can generate inefficient queries — monitor with SQL logging."},

    {"q": "What is SQLite?",
     "a": "SQLite is a lightweight, file-based relational database built into Python's standard library (import sqlite3). No separate server needed — the database is a single .db file. Great for development, small apps, embedded systems, and testing. Not suitable for high-concurrency production workloads."},

    {"q": "What is PostgreSQL?",
     "a": "PostgreSQL (Postgres) is a powerful, open-source relational database known for standards compliance, extensibility, and advanced features: JSONB, full-text search, window functions, CTEs, PostGIS (geospatial). It is the most popular database for Python web applications in production. Connect with psycopg2 or asyncpg."},

    {"q": "What is Redis?",
     "a": "Redis is an in-memory key-value store used for caching, session storage, message queuing (pub/sub), rate limiting, and leaderboards. Data is kept in RAM for microsecond latency. Supports strings, lists, sets, sorted sets, hashes. Python library: redis-py. Often used alongside a primary relational database."},

    {"q": "What is a database index?",
     "a": "An index is a data structure (usually a B-tree) that speeds up data retrieval at the cost of extra storage and slower writes. Without an index, a query scans every row (O(n)). With an index on a column, lookups are O(log n). Always index columns used in WHERE, JOIN, and ORDER BY clauses. Avoid over-indexing."},

    {"q": "What is a database transaction?",
     "a": "A transaction is a sequence of database operations treated as a single unit. It either fully succeeds (commit) or fully rolls back (rollback) on failure. Transactions follow ACID properties: Atomicity, Consistency, Isolation, Durability. In Python: with db.begin(): ... or use context managers in SQLAlchemy/psycopg2."},

    {"q": "What is database normalization?",
     "a": "Normalization organises a database to reduce redundancy and improve data integrity by splitting data into related tables. Normal forms: 1NF (atomic values, no repeating groups), 2NF (no partial dependencies on composite key), 3NF (no transitive dependencies). Denormalisation trades redundancy for query performance."},

    {"q": "What is a JOIN in SQL?",
     "a": "JOIN combines rows from two tables based on a related column. Types: INNER JOIN (only matching rows), LEFT JOIN (all left rows + matching right), RIGHT JOIN (all right rows + matching left), FULL OUTER JOIN (all rows from both). Example: SELECT * FROM orders JOIN users ON orders.user_id = users.id."},

    {"q": "What is MongoDB?",
     "a": "MongoDB is a document-oriented NoSQL database that stores data as BSON (Binary JSON) documents grouped in collections. Flexible schema — documents in the same collection can have different fields. Great for hierarchical/nested data. Python library: pymongo or motor (async). Part of the MERN stack."},

    # ── Version Control / Git ────────────────────────────────────
    {"q": "What is a Git branch?",
     "a": "A branch is an independent line of development. Create one with git branch feature-x or git checkout -b feature-x. Branches let you work on features/bug-fixes without affecting main. Merge with git merge feature-x or use a Pull Request. Delete with git branch -d feature-x after merging."},

    {"q": "What is the difference between git merge and git rebase?",
     "a": "git merge integrates changes from one branch into another, preserving the full history and creating a merge commit. git rebase moves or replays your commits on top of another branch, creating a linear history. Rebase rewrites commits — never rebase shared/public branches. Use merge for integration, rebase for cleanup."},

    {"q": "What is git stash?",
     "a": "git stash temporarily shelves uncommitted changes so you can switch branches with a clean working directory. git stash saves changes; git stash pop restores them. git stash list shows all stashes; git stash drop removes one. Useful when you need to quickly switch context without making a commit."},

    {"q": "What is a pull request?",
     "a": "A pull request (PR) — called a merge request in GitLab — is a proposal to merge code from one branch into another. It is the central point for code review: teammates comment on specific lines, request changes, and approve before merging. PRs document why a change was made."},

    {"q": "What is git cherry-pick?",
     "a": "git cherry-pick <commit-hash> applies the changes of a specific commit onto the current branch. Useful for picking a bug fix from one branch and applying it to another without merging the entire branch. Can be used with a range: git cherry-pick A..B."},

    {"q": "What is .gitignore?",
     "a": ".gitignore is a file listing patterns of files/directories Git should not track: __pycache__/, *.pyc, .env, venv/, node_modules/, *.log. Each line is a pattern. Use gitignore.io to generate one for your stack. Committed files are not affected — use git rm --cached to stop tracking them."},

    {"q": "What is git revert vs git reset?",
     "a": "git revert <commit> creates a new commit that undoes a previous commit — safe for shared branches because it preserves history. git reset moves the branch pointer back and can discard commits (--soft keeps changes staged, --mixed keeps them unstaged, --hard discards them entirely). Never hard-reset shared branches."},

    # ── Software Engineering Principles ──────────────────────────
    {"q": "What are SOLID principles?",
     "a": "SOLID is five OOP design principles: S — Single Responsibility (one reason to change), O — Open/Closed (open for extension, closed for modification), L — Liskov Substitution (subtypes must be substitutable for base types), I — Interface Segregation (specific interfaces over general ones), D — Dependency Inversion (depend on abstractions, not concretions)."},

    {"q": "What is DRY?",
     "a": "DRY (Don't Repeat Yourself) means every piece of knowledge should have a single, authoritative representation in the codebase. Duplicated code means bugs must be fixed in multiple places. Refactor duplicate logic into functions, classes, or modules. The opposite is WET (Write Everything Twice)."},

    {"q": "What is KISS?",
     "a": "KISS (Keep It Simple, Stupid) means prefer the simplest solution that works. Complexity is the enemy of reliability and maintainability. Avoid premature optimisation, over-engineering, and unnecessary abstraction. Simple code is easier to read, test, and debug."},

    {"q": "What is YAGNI?",
     "a": "YAGNI (You Aren't Gonna Need It) means don't build features until they are actually needed. It is a core XP (Extreme Programming) principle. Building speculative features wastes time, adds complexity, and often results in the wrong abstraction. Add things when required, not when imagined."},

    {"q": "What is separation of concerns?",
     "a": "Separation of concerns (SoC) is the idea that different parts of a program should handle different responsibilities with minimal overlap. Example: in MVC, the Model handles data, the View handles display, and the Controller handles logic. SoC improves modularity, testability, and maintainability."},

    {"q": "What is coupling and cohesion?",
     "a": "Coupling measures how dependent modules are on each other — low coupling is desirable (modules are independent). Cohesion measures how closely related the responsibilities of a module are — high cohesion is desirable (a module does one thing well). Good design = high cohesion + low coupling."},

    {"q": "What is technical debt?",
     "a": "Technical debt is the implied cost of shortcuts taken in code — quick fixes, lack of tests, poor design — that must eventually be 'repaid' through refactoring. Like financial debt, it accrues interest: the longer it's left, the harder it becomes to change the code. Track it and dedicate time to paying it down."},

    {"q": "What is refactoring?",
     "a": "Refactoring is restructuring existing code — improving its internal structure without changing its external behaviour. Examples: rename variables, extract a function, simplify a conditional, remove duplication. Tests are essential so you know behaviour is preserved. Refactor in small steps."},

    {"q": "What is code review?",
     "a": "Code review is the practice of one or more developers examining another's code before it is merged. Goals: catch bugs early, share knowledge, enforce standards, improve design. Best practices: review small PRs, be respectful, focus on the code not the person, automate style issues with linters."},

    # ── Testing ──────────────────────────────────────────────────
    {"q": "What is unit testing?",
     "a": "Unit testing tests individual functions or classes in isolation to verify each works correctly. In Python, use unittest (built-in) or pytest (recommended). A good unit test is fast, isolated (no network/DB), repeatable, and tests one thing. Aim for high coverage but quality matters more than percentage."},

    {"q": "What is pytest?",
     "a": "pytest is Python's most popular testing framework. Write test functions starting with test_, run with 'pytest'. Features: auto-discovery, powerful fixtures (dependency injection for setup/teardown), parametrize (run a test with multiple inputs), plugins (coverage, mock, asyncio). Install: pip install pytest."},

    {"q": "What is mocking in testing?",
     "a": "Mocking replaces a real dependency (database, API, file system) with a fake one so tests are fast, isolated, and deterministic. Python provides unittest.mock. Example: from unittest.mock import patch; with patch('requests.get') as mock_get: mock_get.return_value.json.return_value = {...}. Also use pytest-mock."},

    {"q": "What is TDD?",
     "a": "Test-Driven Development (TDD) is a workflow: write a failing test first, write the minimum code to make it pass, then refactor. The cycle is Red → Green → Refactor. Benefits: forces clear requirements, improves design, gives instant regression protection. Popularised by Kent Beck."},

    {"q": "What is the difference between unit, integration, and end-to-end tests?",
     "a": "Unit tests test a single function in isolation (fast, lots of them). Integration tests verify that multiple units work together correctly (e.g., service + database). End-to-end (E2E) tests simulate a real user interacting with the full system (slowest, fewest). The Testing Pyramid recommends many unit, some integration, few E2E."},

    {"q": "What is code coverage?",
     "a": "Code coverage measures the percentage of code lines (or branches) executed by tests. Use pytest-cov: pytest --cov=my_package. 100% coverage doesn't guarantee bug-free code — focus on meaningful tests. Coverage helps identify untested code paths. Aim for high coverage in critical business logic."},

    # ── DevOps / Deployment ──────────────────────────────────────
    {"q": "What is Docker?",
     "a": "Docker packages applications and their dependencies into containers — lightweight, isolated environments that run consistently everywhere. Key concepts: Dockerfile (build instructions), image (immutable snapshot), container (running instance), docker-compose (multi-container apps). Solves 'works on my machine' problems."},

    {"q": "What is a Dockerfile?",
     "a": "A Dockerfile is a text file with instructions to build a Docker image. Key instructions: FROM (base image), WORKDIR (working directory), COPY/ADD (copy files), RUN (execute commands during build), EXPOSE (document port), CMD/ENTRYPOINT (default command when container starts). Build with: docker build -t my-app ."},

    {"q": "What is CI/CD?",
     "a": "CI (Continuous Integration) automatically builds and tests code on every commit, catching bugs early. CD (Continuous Delivery/Deployment) automatically deploys passing builds to staging or production. Tools: GitHub Actions, GitLab CI, Jenkins, CircleCI. A CI/CD pipeline typically: lint → test → build → deploy."},

    {"q": "What is Kubernetes?",
     "a": "Kubernetes (K8s) is an open-source container orchestration system. It automates deploying, scaling, and managing containerised applications. Key concepts: Pod (one or more containers), Deployment (desired state), Service (networking), Ingress (external access), ConfigMap/Secret (configuration). Managed offerings: GKE, EKS, AKS."},

    {"q": "What is an environment variable?",
     "a": "Environment variables are key-value pairs set in the OS that applications can read at runtime. Used to pass configuration (database URLs, API keys, debug mode) without hardcoding it. In Python: os.environ['DATABASE_URL'] or os.getenv('DATABASE_URL', 'default'). Use .env files with python-dotenv in development."},

    {"q": "What is a .env file?",
     "a": "A .env file stores environment variables for local development: DATABASE_URL=postgres://... API_KEY=secret. Load it with python-dotenv: from dotenv import load_dotenv; load_dotenv(). Never commit .env to version control — add it to .gitignore. Use secrets managers (AWS Secrets Manager, Vault) in production."},

    {"q": "What is SSH?",
     "a": "SSH (Secure Shell) is a cryptographic protocol for secure remote access to servers. Connect with: ssh user@host. Use SSH keys instead of passwords: ssh-keygen creates a key pair; copy the public key to the server's ~/.ssh/authorized_keys. SSH tunnelling forwards local ports to remote hosts securely."},

    {"q": "What is a load balancer?",
     "a": "A load balancer distributes incoming traffic across multiple servers to prevent any single server from being overwhelmed. Types: Round-robin (equal distribution), Least-connections (to the server with fewest active connections), IP-hash (same client always to the same server). Tools: Nginx, HAProxy, AWS ELB."},

    {"q": "What is caching?",
     "a": "Caching stores the result of expensive operations (DB queries, API calls, computations) for fast reuse. Levels: in-process (Python dict, functools.lru_cache), distributed (Redis, Memcached), HTTP (browser cache, CDN). Cache invalidation — knowing when to expire cached data — is one of the hardest problems in CS."},

    # ── Security ─────────────────────────────────────────────────
    {"q": "What is SQL injection?",
     "a": "SQL injection is an attack where malicious SQL is inserted into a query via user input. Example: entering ' OR 1=1 -- in a login form. Prevention: always use parameterised queries / prepared statements — never format user input directly into SQL strings. ORMs handle this automatically."},

    {"q": "What is XSS?",
     "a": "Cross-Site Scripting (XSS) injects malicious scripts into web pages viewed by other users. A stored XSS attack saves the script in the database; reflected XSS includes it in the URL. Prevention: escape user-generated HTML output, use Content Security Policy (CSP) headers, use frameworks that auto-escape templates."},

    {"q": "What is CSRF?",
     "a": "Cross-Site Request Forgery (CSRF) tricks a logged-in user into unknowingly submitting a malicious request to a site they trust. Prevention: CSRF tokens (a secret value in each form that is verified server-side). Django includes CSRF protection by default. Also use SameSite cookie attribute."},

    {"q": "What is hashing vs encryption?",
     "a": "Hashing is one-way — you cannot reverse it (MD5, SHA-256, bcrypt). Use it for passwords: store the hash, not the plain text. Verify by hashing the input and comparing. Encryption is two-way — data can be decrypted with a key (AES, RSA). Use it for data that needs to be retrieved. Never encrypt passwords — hash them."},

    {"q": "What is HTTPS?",
     "a": "HTTPS is HTTP encrypted with TLS (Transport Layer Security). It ensures that data sent between the browser and server is encrypted and cannot be intercepted (MITM attacks). A server needs an SSL/TLS certificate (free from Let's Encrypt). Always use HTTPS in production; modern browsers warn on HTTP sites."},

    {"q": "What is rate limiting?",
     "a": "Rate limiting restricts how many requests a client can make in a given time window to prevent abuse, brute-force attacks, and DoS. Example: 100 requests per minute per IP. Implement with Redis (store request counts) or use libraries like flask-limiter. APIs expose rate limit info in response headers."},

    {"q": "What is the principle of least privilege?",
     "a": "The principle of least privilege (PoLP) means every user, process, and system should have only the minimum permissions necessary to perform its function. Apply it to database users (read-only where possible), file permissions, IAM roles in cloud, and API scopes. Limits the blast radius of a security breach."},

    # ── Data Science & ML ────────────────────────────────────────
    {"q": "What is pandas?",
     "a": "pandas is Python's core data manipulation library. It provides DataFrame (2D table) and Series (1D array) with powerful operations: filtering, groupby, merge/join, pivot tables, time series, missing data handling. Essential for data cleaning and exploration. Install: pip install pandas."},

    {"q": "What is NumPy?",
     "a": "NumPy provides fast n-dimensional arrays and mathematical functions. Operations are vectorised (C-speed, no Python loops needed). Core type: numpy.ndarray. Essential for scientific computing, ML, and image processing. pandas, scikit-learn, and TensorFlow all use NumPy arrays internally."},

    {"q": "What is Matplotlib?",
     "a": "Matplotlib is Python's foundational plotting library. Create line plots, bar charts, scatter plots, histograms, heatmaps, and more. Most common interface: matplotlib.pyplot (plt). For richer, interactive plots consider Seaborn (built on Matplotlib), Plotly, or Altair."},

    {"q": "What is scikit-learn?",
     "a": "scikit-learn is Python's standard ML library for classical machine learning. Provides: classification (SVM, Random Forest, KNN), regression (Linear, Ridge), clustering (K-Means, DBSCAN), dimensionality reduction (PCA), model selection (cross-validation, GridSearchCV), and preprocessing. Consistent fit/predict API."},

    {"q": "What is the difference between supervised and unsupervised learning?",
     "a": "Supervised learning trains on labelled data (input → known output): classification (spam/not spam) and regression (house price). Unsupervised learning finds patterns in unlabelled data: clustering (K-Means groups similar items) and dimensionality reduction (PCA). Reinforcement learning learns through rewards/penalties."},

    {"q": "What is overfitting?",
     "a": "Overfitting is when a model learns the training data too well — including noise — and performs poorly on unseen data. Signs: very high training accuracy, much lower validation accuracy. Fixes: more training data, regularisation (L1/L2), dropout (neural nets), simpler model, cross-validation, early stopping."},

    {"q": "What is a neural network?",
     "a": "A neural network is a ML model inspired by the brain, composed of layers of interconnected nodes (neurons). Input layer receives data; hidden layers learn representations; output layer makes predictions. Trained via backpropagation and gradient descent. Deep learning = neural networks with many hidden layers. Libraries: TensorFlow, PyTorch, Keras."},

    {"q": "What is a train/test split?",
     "a": "A train/test split divides data into a training set (model learns from this) and a test set (unseen data to evaluate performance). Common split: 80% train, 20% test. Use sklearn.model_selection.train_test_split(). Use a validation set or k-fold cross-validation to tune hyperparameters without polluting the test set."},

    {"q": "What is feature engineering?",
     "a": "Feature engineering is the process of using domain knowledge to create, transform, or select input variables (features) that improve ML model performance. Examples: encoding categorical variables, scaling numerical features, creating interaction terms, extracting date components (day of week, is_holiday), log-transforming skewed data."},

    {"q": "What is a confusion matrix?",
     "a": "A confusion matrix shows a classification model's performance across all classes. For binary classification: True Positive (correctly predicted positive), True Negative, False Positive (Type I error), False Negative (Type II error). Derived metrics: Accuracy = (TP+TN)/total, Precision = TP/(TP+FP), Recall = TP/(TP+FN), F1 = harmonic mean of precision and recall."},

    # ── JavaScript ───────────────────────────────────────────────
    {"q": "What is JavaScript?",
     "a": "JavaScript is the programming language of the web — the only language browsers run natively. It makes pages interactive (DOM manipulation, event handling). Node.js brings JavaScript to the server. Modern JS (ES6+) has classes, arrow functions, async/await, modules, and destructuring."},

    {"q": "What is the difference between let, const, and var?",
     "a": "var is function-scoped, hoisted, and allows re-declaration — largely avoid it. let is block-scoped and can be reassigned but not re-declared. const is block-scoped and cannot be reassigned (but object properties can still be mutated). Use const by default; use let when you need to reassign."},

    {"q": "What is a Promise in JavaScript?",
     "a": "A Promise represents a value that will be available in the future — it is either pending, fulfilled, or rejected. Use .then() for success and .catch() for errors. async/await is syntactic sugar over Promises: await pauses execution until the Promise resolves. Example: const data = await fetch('/api').then(r => r.json())."},

    {"q": "What is the DOM?",
     "a": "The DOM (Document Object Model) is the browser's in-memory tree representation of an HTML page. JavaScript can read and modify it: document.getElementById('id'), element.textContent = 'Hello', element.addEventListener('click', handler). Changes to the DOM update what the user sees in real time."},

    {"q": "What is Node.js?",
     "a": "Node.js is a JavaScript runtime built on Chrome's V8 engine that runs JS outside the browser — on servers, CLIs, and build tools. It uses a non-blocking, event-driven I/O model making it fast for concurrent connections. npm is Node's package manager with millions of packages."},

    {"q": "What is React?",
     "a": "React is a JavaScript library for building UIs with reusable components. It uses a Virtual DOM for efficient updates and JSX (HTML-like syntax in JS). State management: useState, useReducer, useContext hooks. Large ecosystem: Next.js (SSR/SSG), React Router, Redux, React Query. Developed by Meta."},

    # ── General Programming Concepts ─────────────────────────────
    {"q": "What is an algorithm?",
     "a": "An algorithm is a finite, step-by-step procedure for solving a problem or performing a computation. It must be: correct (produces right output), finite (terminates), unambiguous (each step is clear). Algorithms are independent of programming language — the same algorithm can be implemented in any language."},

    {"q": "What is a compiler vs an interpreter?",
     "a": "A compiler translates source code to machine code all at once before execution (C, C++, Go, Rust). Compiled programs run fast but compilation takes time. An interpreter translates and executes code line-by-line at runtime (Python, Ruby). Python actually compiles to bytecode (.pyc) then interprets it — a hybrid approach."},

    {"q": "What is a design pattern?",
     "a": "A design pattern is a reusable solution to a common software design problem. Categories: Creational (Singleton, Factory, Builder), Structural (Adapter, Decorator, Proxy), Behavioural (Observer, Strategy, Command). Patterns are language-agnostic templates, not code. They improve communication between developers."},

    {"q": "What is the Singleton pattern?",
     "a": "The Singleton pattern ensures a class has only one instance and provides a global access point to it. Use cases: database connection pool, configuration object, logger. In Python, the simplest approach is a module-level variable (modules are singletons by default). Singletons make testing harder — consider dependency injection instead."},

    {"q": "What is the Factory pattern?",
     "a": "The Factory pattern provides an interface for creating objects without specifying the exact class. A factory function or class decides which concrete class to instantiate based on input. Example: ShapeFactory.create('circle') returns a Circle object. Decouples object creation from the code that uses it."},

    {"q": "What is the Observer pattern?",
     "a": "The Observer pattern defines a one-to-many relationship: when a subject changes state, all registered observers are notified automatically. Examples: event listeners in JavaScript (addEventListener), Django signals, GUI frameworks. Promotes loose coupling between the subject and observers."},

    {"q": "What is functional programming?",
     "a": "Functional programming (FP) treats computation as the evaluation of mathematical functions. Key principles: pure functions (same input always gives same output, no side effects), immutability, first-class functions (functions as values), higher-order functions (map, filter, reduce). Python supports FP alongside OOP."},

    {"q": "What is immutability?",
     "a": "An immutable object cannot be changed after creation. Python's immutable types: int, float, str, tuple, frozenset, bytes. Immutability makes code easier to reason about, enables safe sharing between threads, and allows hashing (dict keys must be hashable). Functional programming favours immutability."},

    {"q": "What is a pure function?",
     "a": "A pure function always returns the same output for the same input (deterministic) and has no side effects (doesn't modify external state, no I/O). Benefits: easy to test (no mocks needed), safe to cache (memoize), and safe to parallelise. Aim to write as many pure functions as possible."},

    {"q": "What is the difference between synchronous and asynchronous code?",
     "a": "Synchronous code executes line by line — each line waits for the previous to finish. Asynchronous code can start an operation and continue doing other work while waiting for it to complete (I/O, network). Python async/await, JavaScript Promises, and callbacks all enable async programming. Async is crucial for high-concurrency servers."},

    {"q": "What is a REST vs SOAP API?",
     "a": "REST uses standard HTTP methods, is stateless, and typically returns JSON — lightweight and easy to consume. SOAP is a protocol that uses XML messages and has strict standards (WSDL, WS-Security). SOAP is more rigid but has built-in error handling and is still used in enterprise/financial systems. REST is the modern default."},

    {"q": "What is serialization?",
     "a": "Serialisation converts an object into a format that can be stored or transmitted (JSON, XML, binary, pickle). Deserialisation reverses the process. Python: json.dumps/json.loads for JSON, pickle.dumps/pickle.loads for binary Python objects. APIs serialise data to JSON; ORMs serialise objects to/from database rows."},

    {"q": "What is an IDE?",
     "a": "An IDE (Integrated Development Environment) provides a comprehensive environment for coding: editor, debugger, autocomplete, linting, version control integration, terminal. Popular Python IDEs: PyCharm (full-featured), VS Code (lightweight, extensible with plugins), Jupyter Notebook (interactive, data science). Editor choice is personal — use what makes you productive."},

    {"q": "What is linting?",
     "a": "A linter is a tool that analyses code for style errors, bugs, and bad practices without running it. Python linters: Flake8 (PEP 8 style + errors), Pylint (more thorough), Ruff (extremely fast, Rust-based, covers Flake8+isort+more), mypy (type checking). Integrate into CI and your editor for continuous feedback."},

    {"q": "What is PEP 8?",
     "a": "PEP 8 is Python's official style guide. Key rules: 4 spaces per indent, max 79 characters per line, two blank lines between top-level definitions, one blank line between methods, imports at the top (stdlib → third-party → local), snake_case for variables/functions, PascalCase for classes, UPPER_SNAKE for constants."},

    {"q": "What is a virtual machine?",
     "a": "A virtual machine (VM) emulates a complete computer within software — it has its own OS, CPU, memory, and storage. Tools: VirtualBox, VMware, Hyper-V. In Python context, the CPython VM executes bytecode. Cloud VMs (AWS EC2, GCP Compute Engine) are on-demand virtual servers. Containers (Docker) are lighter than VMs."},

    {"q": "What is an API key?",
     "a": "An API key is a unique identifier used to authenticate requests to an API. It is sent in request headers (Authorization: Bearer key or X-API-Key: key). Keep keys secret — never hardcode in source code. Store in environment variables or secrets managers. Rotate regularly and restrict by IP/scope where the API allows."},

    {"q": "What is the difference between HTTP GET and POST?",
     "a": "GET retrieves data from the server — parameters are in the URL query string, bookmarkable, cacheable, idempotent. POST sends data to the server (form submission, JSON body) — data is in the request body, not bookmarkable, not cached, used for creating/modifying data. GET requests should never change server state."},

    {"q": "What is a CDN?",
     "a": "A CDN (Content Delivery Network) is a geographically distributed network of servers that delivers static assets (images, CSS, JS, videos) from a server close to the user, reducing latency. Examples: Cloudflare, AWS CloudFront, Fastly. Essential for high-traffic sites. Also provides DDoS protection and SSL termination."},

    {"q": "What is microservices architecture?",
     "a": "Microservices splits an application into small, independent services that each handle a specific business capability and communicate via APIs (REST, gRPC, message queues). Benefits: independent deployment, scalability, technology flexibility. Challenges: distributed system complexity, network latency, data consistency. Contrast with monolithic architecture."},

    {"q": "What is a monolithic architecture?",
     "a": "A monolith is a single deployable unit containing all application logic — UI, business logic, and database layer together. Simpler to develop and deploy initially; becomes harder to scale and change as it grows. Most applications should start as a monolith and extract services only when there is a clear reason."},

    {"q": "What is message queuing?",
     "a": "Message queuing decouples producers (services that send tasks) from consumers (services that process them) via a queue. Benefits: absorbs traffic spikes, enables async processing, improves resilience. Tools: RabbitMQ, Apache Kafka, AWS SQS, Celery (Python task queue using Redis/RabbitMQ as broker)."},

    {"q": "What is a regex?",
     "a": "A regular expression (regex) is a pattern for matching text. Examples: \\d+ matches one or more digits, [a-z]+ matches lowercase letters, ^start matches at string start, end$ matches at string end, .* matches anything. In Python: import re; re.search(r'\\d+', 'abc123') finds '123'. Test patterns at regex101.com."},

    {"q": "What is Unicode?",
     "a": "Unicode is a universal character encoding standard that assigns a unique code point to every character in every writing system. Python 3 strings are Unicode by default. UTF-8 is the most common encoding — it represents ASCII as single bytes and other characters as 2-4 bytes. Always specify encoding when opening files: open('f', encoding='utf-8')."},

    {"q": "What is an abstract data type?",
     "a": "An abstract data type (ADT) defines a data structure by its behaviour (operations and their semantics) without specifying implementation. Examples: Stack (push/pop/peek), Queue (enqueue/dequeue), Set (add/remove/contains). The same ADT can have multiple implementations — e.g., a Stack can be implemented with a list or linked list."},

    {"q": "What is the difference between pass by value and pass by reference?",
     "a": "In pass-by-value, a copy of the variable is passed — changes inside the function don't affect the original. In pass-by-reference, the function receives a reference to the original — changes affect the original. Python uses 'pass by object reference': immutable objects (int, str) behave like value; mutable objects (list, dict) behave like reference."},

    {"q": "What is a namespace?",
     "a": "A namespace is a mapping from names to objects — it prevents naming conflicts. Python has: local namespace (inside a function), enclosing namespace (outer function), global namespace (module level), built-in namespace (Python built-ins). The LEGB rule defines lookup order: Local → Enclosing → Global → Built-in."},

    {"q": "What is the difference between a process and a thread?",
     "a": "A process is an independent program with its own memory space. A thread is a lightweight unit of execution within a process that shares the process's memory. Threads are cheaper to create and communicate easily, but share state (risk of race conditions). Processes are isolated (safer) but communicate via IPC or sockets."},

    {"q": "What is a race condition?",
     "a": "A race condition occurs when the output of a program depends on the unpredictable timing of concurrent operations. Example: two threads reading and incrementing a counter simultaneously can both read the same value and both write the same incremented value — losing one update. Fix with locks, atomic operations, or using thread-safe data structures."},

    {"q": "What is a deadlock?",
     "a": "A deadlock occurs when two or more threads/processes each hold a resource the other needs and both wait forever. Example: Thread A holds lock 1 and waits for lock 2; Thread B holds lock 2 and waits for lock 1. Prevention: always acquire locks in the same order, use timeouts, or use higher-level concurrency abstractions."},

    {"q": "What is an event loop?",
     "a": "An event loop continuously checks for and dispatches events/tasks. In Python's asyncio, the event loop runs coroutines — when one awaits I/O, the loop suspends it and runs another. In JavaScript, the event loop processes the call stack, microtask queue, and macro-task queue. It enables non-blocking concurrency on a single thread."},

    {"q": "What is tail call optimisation?",
     "a": "Tail call optimisation (TCO) allows recursive functions where the recursive call is the last operation to reuse the current stack frame instead of adding a new one — preventing stack overflow. Python does NOT implement TCO by design (Guido van Rossum's decision). Convert deep recursion to iteration or use trampolining if needed."},

    {"q": "What is garbage collection?",
     "a": "Garbage collection (GC) automatically frees memory that is no longer referenced by the program. Python uses reference counting as the primary mechanism — when an object's reference count hits zero, it is freed immediately. The gc module handles reference cycles that reference counting cannot break."},

    {"q": "What is memory management in Python?",
     "a": "Python manages memory automatically via the private heap. The memory manager allocates/deallocates memory; the garbage collector handles cycles. You rarely need to manage memory manually. To free large objects explicitly: del obj. Profile memory with tracemalloc or memory-profiler. CPython caches small integers (-5 to 256) and interned strings."},

    {"q": "What is the difference between compiled and interpreted languages?",
     "a": "Compiled languages (C, C++, Go, Rust) are translated to machine code before running — fast execution, platform-specific binary. Interpreted languages (Python, Ruby) are translated at runtime — easier development, slower execution. Python is a hybrid: source → bytecode (.pyc) → CPython VM. JIT-compiled variants (PyPy) blur the line further."},

    {"q": "What is an interface?",
     "a": "An interface defines a contract — a set of methods a class must implement — without providing the implementation. In Python, interfaces are implemented via abstract base classes (ABCs) using the abc module. Duck typing means Python doesn't enforce interfaces strictly — if an object has the right methods, it works. Protocol classes (Python 3.8+) enable structural subtyping."},

    {"q": "What is duck typing?",
     "a": "Duck typing is Python's philosophy: 'If it walks like a duck and quacks like a duck, it's a duck.' You don't check an object's type — you just call the methods you need. If the object has them, it works. This makes Python very flexible and enables writing generic code without inheritance hierarchies."},

    {"q": "What is the difference between a compiled language and a scripting language?",
     "a": "Compiled languages are translated to machine code ahead of time (C, C++, Rust). Scripting languages are typically interpreted at runtime and used for automation, glue code, and rapid development (Python, Bash, JavaScript). The boundary is blurry — Python is often called a scripting language but is used for complex applications too."},

    {"q": "What is an API endpoint?",
     "a": "An API endpoint is a specific URL that accepts requests and returns responses for a particular resource or action. Example: GET https://api.example.com/users returns all users; POST https://api.example.com/users/42/follow follows user 42. Each endpoint should have a single, clear purpose."},

    {"q": "What is the cloud?",
     "a": "The cloud refers to servers, storage, databases, networking, software, and analytics delivered over the internet on a pay-as-you-go basis. Major providers: AWS (Amazon), Azure (Microsoft), GCP (Google). Models: IaaS (virtual servers), PaaS (managed platforms like Heroku), SaaS (software like Gmail). Benefits: scalability, no hardware management, global reach."},

    {"q": "What is serverless computing?",
     "a": "Serverless means you write functions that run in response to events without managing servers. The provider (AWS Lambda, Google Cloud Functions, Azure Functions) handles infrastructure, scaling, and billing per invocation. Great for APIs, webhooks, scheduled jobs, and event-driven architectures. Python is a first-class serverless language."},

    {"q": "What is an IDE vs a text editor?",
     "a": "A text editor (VS Code, Sublime, Vim, Emacs) is lightweight and focuses on editing code, with plugins for language features. An IDE (PyCharm, IntelliJ) is a full environment with built-in debugging, refactoring, database tools, and deep language understanding out of the box. VS Code with Python extension bridges the gap."},

    {"q": "What is open source software?",
     "a": "Open source software has publicly available source code that anyone can view, use, modify, and distribute (subject to the license). Python itself is open source (PSF license). Key licenses: MIT (very permissive), Apache 2.0, GPL (copyleft — derivatives must also be open source). Most Python libraries are open source on GitHub/PyPI."},

    {"q": "What is the difference between a framework and a library?",
     "a": "A library is a collection of tools you call when you need them — you are in control (requests, NumPy). A framework provides a skeleton and calls your code at defined points — inversion of control (Django, Flask). As Martin Fowler says: 'A library is code you call; a framework calls your code.' Both extend what you can do without reinventing wheels."},
]