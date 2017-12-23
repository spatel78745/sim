class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name
        self.tricks = []
        
    def add_trick(self, trick):
        self.tricks.append(trick)
        
if __name__ == "__main__":
    fido = Dog("Fido")
    buddy = Dog("Buddy")
    fido.add_trick("play dead")
    fido.add_trick("roll over")
    print(fido.name, fido.tricks)
    
    
