## 1.2. Functions, First-class Functions and Immutable Data

- float, int, and bool are also immutable data types.
- id() to find memory location
- id changes when immutable is modified not mutable.py
  - immutable: passed by value
  - mutable: passed by reference

## 1.3. Iterators and Generators

- Iterator protocol: Any object that is an iterator must have `__iter__` and `__next__` methods in its class
- List comprehension: `list_comp = [x**2 for x in range(5)]`
- Generator comprehension: `gen_expr = (x**2 for x in range(5))`
- Generators use yield to produce a series of values in a lazy, on-demand fashion.
- The for x in iterator syntax is the same as calling next() again and again.
  - in case of generator, it deletes the previous
  - in case of others, it keeps the previous

## 1.4. Working with Collections

Note: Everything below is a function (not a method) which returns a value without modifying the variable it’s called upon.

- Reductions
  - `any()` returns `True` if any value in iterable is truthy
  - `all()` returns `True` if all values in iterable are truthy
  - `sum(iterable, [start = 0])` returns sum of all values in iterable + `[start]`
  - `len()`, `max()`, `min()`
  - `reduce(function, iterable)` apply function to first two elements of iterable, then call reduce again on a new iterable where the first element is the result obtained and the second element is the third element of the initial iterable, and so on until only one element left in the iterable. Returns the result obtained now.
- Mappings
  - `map(function, iterable)` returns iterable with function applied on each value of initial iterable.
  - `zip(*2-dimensional iterable)` i.e., `zip(iterable, iterable, … , iterable)` returns new 2-dimensional tuple with first element a tuple of 1st elements, second element a tuple of 2nd elements and so on.
  - `sorted(iterable, [key = function (applied before sorting), [reverse = False]])`
  - `reversed(iterator)` Note: remember to use a constructor like `list(reversed(iterator))` since the function returns a reversedObject and leaves it at that.
  - `enumerate(iterator, [start = 0])`
- Filter
  - `filter(function, iterator)` returns generator (remember to use a constructor with it)

## Higher-order Functions - I

- Generally but doesn't have to be: loops use mutable data types and recursions use immutable data types
- loop holds a state in a variable to know the current element being iterated. Since it maintains a state of the current iteration and is mutable, it is against functional programming.
- Recursion involves pushing stack frames to the runtime (for every element), executing given set of instructions, returning a value, and popping back from the stack. As a final result, the given problem will be solved and reduced to one single value (the return value of the first function call)
- Unlike Loops, Recursions doesn’t use mutable data types since everything is being stored in the stack frames. This allows us to write programs that operate on higher levels of abstraction.
- Our interest will be in Recursion rather than loops since recursion allows to use multiple processor cores at the same time which in turn ends in a greater cumulative CPU clock speed. In case of loops, it uses same core throughout the iteration and the clock speed of a CPU core cannot be increased more than a limit and becomes too expensive with greater clock speeds. In Big Data, this clock speed plays crucial role in data processing and hence Recursion is our point of interest.
- Recursion is of two types:
  - Head recursion
  - Tail recursion

![Difference between head and tail recursion](https://imgur.com/2PfTkcs.png)

## `functools` Module

- `@lru_cache([maxsize=128])` memos return value for next call with same input

```python
>>> import functools
>>> @functools.lru_cache(maxsize=2)
... def square(num):
...     print("running", num)
...     return num ** 2
>>> square(2)
running 2
4
>>> square(2)
4
>>> square(1)
running 1
1
>>> square(3)
running 3
9
>>> square(2)
running 2
4
>>> square(3)
9
```

- `partial(function, parameters)` returns a new function which is the same as the function entered but with less required arguments
- `partialmethod(function, parameters)` same as partial but for class methods
- `@wraps` creates a user-defined decorator that preserves the metadata (such as the name, docstring, and other attributes) of the original function in the wrapper function.

## `itertools` Module
- `count([start = 0, step = 1])` return an iterator with values from 0 to infinity. It’s commonly used with zip to assign indexes like `scores = list(zip(functools.count(), (100, 95, 64, 97, 99)))`
- `cycle(iterator)` returns an iterator which has the entered iterator repeated over and over again infinitly
- `repeat(value, [times=None])` returns an iterator which has the entered value `times` times (infinite times by default)
- `accumulate(iterator, function)`same as reduce but order of arguments is reversed
- `chain(*iterator)` joins the iterators entered one after the other
- `chain.from_iterable(list)` same as chain but takes all arguments inside one list
- `compress(iterator, [*True/False])` returns a new iterator with only elements whose corressponding index in the second argument list is True.
- `zip_longest()` zips everything, where it would've stopped if it was zip, it just puts a None there this time
- `permutations(iterable, n)` all the ways the values in iterable can be arranged in `n` places where order does not matter
- `product(iterable, [repeat = n])` all possible ways *with repetition* that values of entered iterable can be arranged in `n` places. If repeat is ommited, repeats iterable as it is.
- `filterfalse(function, iterable)` same as built in `filter()` but for falsy values instead of truthy
- `dropwhile(function, iterable)` starts iteration from where the first falsy (returns `False` when passed in function) value is found.
- `takewhile(function, iterable)` keeps iterating until falsy (returns `False` when passed in function) value is found, where it stops iteration.
- `starmap(function, 2-dimensional list of tuples)` runs function one by one each time with a different set of arguments provided by list entered.

## Higher-order Functions - II
function is callable because it is an object with the method `__call__`
- `callable(object)` tells if object can be called or not
- We can make any class instance callable (like a function) using the call method as follows
```python
class Greet:
    def __init__(self, greeting):
        self.greeting = greeting
    def __call__(self, name):
        return self.greeting + ' ' + name
greeter = Greet('Hello')
print(greeter.greeting)
print(greeter('World'))
```
- The data types in python such as int, float, str, list, tuple and dict are classes by themselves which are callable. eg. `print(int(123))` works
- attributes that are callable are known as “methods” of the class/ object they are called upon.
- `print(dir(list.append))` has the `__call__` method in it. This tell us List is a class which has a method named “append” in it. This method is callable because of the `__call__` method present in it.
- `my_list.append(5)` is the same as `my_list.append.__call__(5)`
- A function is said to be pure if it does not modify the state of anything beyond its scope. In functional programming where there is no state at all.
- Avoiding global variables in programming is a general thumb rule and likewise, avoiding state changes to the objects outside the scope is a thumb rule for functional programming.
```python
# impure function
def append_4(input_list):
    input_list.append(4)
    return input_list
# pure function
def append_4(input_list):
    temp_list = input_list[:]
    temp_list.append(4)
    return temp_list
```
- Modifying a class definition or a function definition during runtime is called as monkey patching (it should be avoided)
- Currying: function inside function and then calling outerfunction then inner function in the same line
```python
def add(a):
    def add_a(b):
        return a + b
    return add_a
print(add(2)(3))
```
## 1.7. File Operations in Python
I am only writing stuff that's somewhat new to us
- To loop through each line in file without readlines
```python
file = open("abc.txt", "r")
for x in file:
    print(x)
```

## 1.8. Data preprocessing
- Pandas series: unidimensional array of indexed data
- Missing data is generally referred to as null, NaN or NA. In pandas it is represented by None. It can only be used in arrays containing python objects.

`import numpy as np`
- `np.array(list)` returns numpy array
- `array.sum()` returns error if numpy array has any None value in it
- `np.nan` represents NaN. Any operations on NaN returns NaN. However these methods find sum ignoring NaN values:
  - `np.nansum(array)`
  - `np.nanmax(array)`
  - `np.nanmin(array)`
- native data types like `int` are way faster than python `object` data type

`import pandas as pd`
- `pd.Series(iterable, [dtype])` returns pandas Series data type, converts both None and np.nan into NaN.
  - for numbers dtype is float64
  - when we pass dtype='int' it becomes int32
- Manipulation (it’s like list manipulation!)
  - `series[0] = None` sets first value to NaN
  - `print(data.values)` When we print this we get formatted data and dtype of data
  - `print(data.index)` we get something `like RangeIndex(start=0, stop=4, step=1)`
  - `print(data[1])` gives value at index 1
  - `print(data[1:3])` we get formatted data at index 1, 2 and dtype of data
- Next up we will do these functions! (Handling missing data)
  - In below statements `series` is any variable containing pandas series datatype
  - `series.isnull()` - when printed, gives formatted data but in value column it shows True or False where there is value or NaN respectivly and dtype: bool
  - `series.notnull()` - Opposite of isnull()
    - `data[data.notnull()]` when printed, gives all data that is not NaN or None. 
  - `series.dropna()` removes all NaN and None values from series
  - `series.fillna(value)` - Return a copy of the data with NaN or None values replaced with `value`

In below statements `df` is any variable containing pandas DataFrame datatype
- `pd.DataFrame(2 dimensional list)` returns a pandas DataFrame datatype.
- `df.dropna()` drops all rows that have any na (None or NaN)
- `df.dropna(axis='columns')` drops all columns that have any na
- `df[3] = np.nan` creates a new column with all NaN values
- `df[3] = [98, 2, 33]` creates a new column with values 98 to row 1, 2 to row 2 and 33 to row 3
- `df.dropna(how='all')` only removes rows which have all na values
- `df.dropna(axis='columns', how='all')` only removes columns which have all na values then returns result (remember to store it in a variable!)
- `df.dropna(thresh=3)` only removes rows which have less than three values (remember to store it in a variable!)
- `df.dropna(axis='columns', thresh=3)` only removes columns which have less than three values (remember to store it in a variable!)

Changing indexing
- `pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))` will index the series with a, b, c, d, e instead of 0, 1, 2, 3, 4, 5

Filling in Null values
- `series.fillna(0)` to replace with 0
- `series.fillna(method='ffill')` forward fill: last filled value is placed in place of null
- `series.fillna(method='bfill')` backward fill: value filled after null is replaced with null

## EDA (Exploratory Data Analysis)
- `digits = pd.read_csv("URL", [header])` open CSV file from URL. When header = None, it means the CSV file we are importing does not have headings row.
- `df.describe()` when printed gives count, mean, standard deviation, minimum and maximum values and the quantiles of the data
- `df.head(10)` returns first 10 rows
- `df.tail(10)` returns last 10 rows
- `df.sample()` returns 10% of the data randomly selected
- `df.sample(10)` returns 10 random rows

Note: loc uses label, iloc uses integer (index)
- `df.loc[0, :]` returns table with all columns of row 0
- `df.loc[[0, 1, 2], :]` returns table with all columns of row 0, 1 and 2.
- `df.loc[[0:2], :]` gives the same result as above. Notice the range is inclusive!
- `df.loc[:, 'Name']` gives all the row values of column `'Name'`
- `df.loc[:, ['Name', 'Age']]` gives all the row values of column `'Name'` and column `'Age'`
- `df.loc[:, ['Name':'Embarked']]` gives all the row values of all columns `'Name'` between `'Embarked'`(inclusive)
- `df.loc[df.Sex=='Male']` all rows where Sex is Male
- `df.loc[df.Sex=='Male', 'Name']` all names where Sex is Male
- `df.iloc[:, 0:2]` all rows but only show their first and second column
- `df.iloc[:, 0:2]` all rows but only show their first and second column
- `df.iloc[0:2, :]` all columns but only show their first and second column

## Queries
- `df.query('Petal_length > Sepal_length')` when printed gives rows which follow the specified query

## Features
Feature engineering increases the predictive power of algorithms

🚧 This section is currently under development and will be completed soon 🚧