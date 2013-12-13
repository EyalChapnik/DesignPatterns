class AbsMeal(object):

    def __init__(self, *args, **kwargs):
         if self.__class__ is AbsMeal:
             raise TypeError('abstract class cannot be instantiated')
         
    def prepare(self): print('prepare is the same')
    def cook(self): raise TypeError('abstract method must be overridden')
    def eat(self): raise TypeError('abstract method must be overridden')

    def go(self):
        self.prepare()
        self.cook()
        self.eat()

class Pizza(AbsMeal):

    def cook(self):
        print "Cook Pizza"

    def eat(self):
        print "Eat Pizza"

class Tea(AbsMeal):

    def cook(self):
        print "Cook Tea"

    def eat(self):
        print "Eat Tea"

makePizza = Pizza()
makePizza.go()

print 25*"+"

makeTea = Tea()
makeTea.go()
