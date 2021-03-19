# Python Guideline <!-- omit in toc -->

- [Time](#time)
- [Class template with docstring](#class-template-with-docstring)
- [Magic methods](#magic-methods)
- [Class inheritance](#class-inheritance)
- [Decorators](#decorators)
- [Set up virtual environment](#set-up-virtual-environment)
- [Upload Python package to Pypi and Test Pypi](#upload-python-package-to-pypi-and-test-pypi)

## Time

Measure how much time a code section takes to run:
```python
import time

start = time.time()

'''
code that runs and takes time
'''

print('Duration: {} seconds'.format(time.time() - start))
```

## Class template with docstring

```python
class Pants:
    '''The Pants class represents an article of clothing sold in a store
    '''

    def __init__(self, color, waist_size, length, price):
        '''Method for initializing a Pants object

        Args: 
            color (str)
            waist_size (int)
            length (int)
            price (float)

        Attributes:
            color (str): color of a pants object
            waist_size (str): waist size of a pants object
            length (str): length of a pants object
            price (float): price of a pants object
        '''

        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price

    def change_price(self, new_price):
        '''The change_price method changes the price attribute of a pants object

        Args: 
            new_price (float): the new price of the pants object

        Returns: None

        '''
        self.price = new_price

    def discount(self, percentage):
        '''The discount method outputs a discounted price of a pants object

        Args:
            percentage (float): a decimal representing the amount to discount

        Returns:
            float: the discounted price
        '''
        return self.price * (1 - percentage)
```

## Magic methods
https://rszalski.github.io/magicmethods/

## Class inheritance
Example:
```python
class Clothing:

    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price
        
    def change_price(self, price):
        self.price = price
        
    def calculate_discount(self, discount):
        return self.price * (1 - discount)
        
class Shirt(Clothing):
    
    def __init__(self, color, size, style, price, long_or_short):
        
        Clothing.__init__(self, color, size, style, price)
        self.long_or_short = long_or_short
    
    def double_price(self):
        self.price = 2*self.price
    
class Pants(Clothing):

    def __init__(self, color, size, style, price, waist):
        
        Clothing.__init__(self, color, size, style, price)
        self.waist = waist
        
    def calculate_discount(self, discount):
        return self.price * (1 - discount / 2)
```

## Decorators
Source: https://realpython.com/primer-on-python-decorators/

Example 1:
```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
```

Example 2:
If the wrapped function needs to take arguments.
```
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")
```

Example 3:
```python
import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice
```

## Set up virtual environment

With Conda:
```
conda create --name environmentname
source activate environmentname
conda install numpy
```

With Venv:
```
python3 -m venv environmentname
source environmentname/bin/activate
pip install numpy
```

## Upload Python package to Pypi and Test Pypi

```
cd packagefolder
python setup.py sdist
pip install twine

# commands to upload to the pypi test repository
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/simple/ packagename

# command to upload to the pypi repository
twine upload dist/*
pip install packagename
```

More info:
- https://packaging.python.org/tutorials/packaging-projects/ 
- https://packaging.python.org/guides/distributing-packages-using-setuptools/

