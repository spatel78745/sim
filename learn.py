'''
Network Simulator

Coding conventions
- CamelCase
- instance variables begin with _
- class private variables begin with _

- Functions should throw exceptions instead of returning error codes
'''

'''
class Thing

notify
'''

class Observer:
    def notify(self, thing):
        pass

'''
class Thing

sendMessage
addObserver

sendMessage
- Syntax: <message> <arguments...>
- May cause observers to be notified. ALL or no observers are notified.

e.g. wire.sendMessage("set voltage 5")

'''
class Thing:
    def __init__(self):
        self.observers = []

    def sendMessage(self, msg):
        pass

    def addObserver(self, obs):
        pass

def testThing:
    class MyObserver(Observer):
    t = Thing()
    t.sendMessage("hello")
    t.addObserver(


if ??? == "__main__":
    
