class Person(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name


class woman(Person):
    def sing(self):
        print "Lalalalala"

class man(Person):
    def dance(self):
        print "trap trap"

if __name__ == '__main__':
    olivia = woman(20, "Olivia")
    olivia.sing()

    oli = man(20,"Oli")
    oli.dance()