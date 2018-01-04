class Human(object):
    def __init__(self, age, name):
        """
        :type age: int
        :type name: str
        """
        self.age = age
        self.name = name

    def get_older(self):
        self.age += 1 # same as self.age = self.age + 1

    def get_younger(self):
        self.age -= 1

    def greeting(self):
        return "Hello my name is " + self.name + " and I am " + str(self.age)

if __name__ == '__main__':
    alfred = Human(19,"Alfred")
    #alfred is an instance in the class human
    print alfred.age #access attributes with "."
    print alfred.name
    alfred.get_older()
    print alfred.age
    print alfred.name
    alfred.get_younger()
    print alfred.age
    print alfred.name
    print alfred.greeting()


# self is a placeholder for e.g. alfred, if there are more humans it should apply only to the 'self'/the human that is in question
# if there were alfred and manfred it would only make alfred older and not both of them

