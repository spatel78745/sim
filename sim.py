'''
A network simulator.

Coding Conventions
- Data attributes are prefixed with a single underscore e.g. self._time

Key
- MIS: Mistake
- PRD: Prediction
- QUE: Question

'''

'''
This example illustrates "private" variables. First, some facts:
- attributes prefixed with __var are textually renamed _classname__var

Now, let's say that there was no "__update". Then MappingSubclass.update would
override Mapping.update and __init__ would call MappingSubclass.update. Thus,
as is says in the Python tutorial, __init__ would be broken.
'''

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update

class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)

class BaseClassName:
    def __init__(self, arg1, arg2):
        print("Created:", self.__class__)
        self._arg1 = arg1
        self._arg2 = arg2

    def method(self):
        print("In:", self.__class__, "arg1:", self._arg1, "arg2:", self._arg2)

# MIS: Forgot to subclass from BaseClassName
# QUE: Why did everything work except isinstance() and issubclass()
class DerivedClassName(BaseClassName):
    def __init__(self, arg3):
        print("Created:", self.__class__)
        # MIS Forgot "self" in call to base-class __init__ 
        BaseClassName.__init__(self, 68, 69)
        # MIS Forgot data-attribute naming convention
        self._arg3 = arg3

    def method(self):
        print("In:", self.__class__, "arg1:", self._arg1, "arg2:", self._arg2,
              "arg3:", self._arg3)

class Event:
    def __init__(self, time, message):
        # MIS Named attribute same as method
        self._time = time
        self._message = message

    # MIS Forgot "self." when accessing data attributes
    # QUE Should Pyhton programs have accessors?
    def time(self)   : return self._time
    def message(self): return self._message
    def sayHello(self): print("Hello")

class Separator:
    sectionNum = 1
    # MIS In classes, statements outside of functions are executed
    def sep():
        # MIS Class attributes must be qualified with the class name
        print(Separator.sectionNum, "================================")

'''
Can I use self.__class__.name as a default argument value in the argument-list
of __init__?

No, because 'self' is undefined in the argument list.
'''
class DefaultArgument:
    def __init__(self, name=''):
        if (name): self._name = name
        else     : self._name = self.__class__.__name__

def testDefaultArgument():
    d1 = DefaultArgument()
    d2 = DefaultArgument('sameer')

'''
QUE: because exit() and quit() don't return to the interpreter prompt.
'''
def testTheRest():
    quit()
    
    e = Event('+10', 'toggle new')

    # MIS Forgot that "print()" inserts spaces
    print('time:', e.time())
    print('message:', e.message())
    Separator.sep()

    # PRD "In:<class '__main__.DerivedClassName'> arg1: 68
    # arg2: 69, arg3: 3
    d = DerivedClassName(3)
    d.method()

    # PRD print true
    print(isinstance(d, DerivedClassName))

    # PRD print true
    # MIS Objects are instances of the entire hierarchy
    print(isinstance(d, BaseClassName))

    # PRD print true
    # MIS A derived class is not an instance of it's base classes
    print(isinstance(BaseClassName, DerivedClassName))

    # PRD print true
    print(issubclass(DerivedClassName, BaseClassName))

    # PRD print false
    print(issubclass(BaseClassName, DerivedClassName))

if (__name__ == '__main__'):
    testDefaultArgument()

