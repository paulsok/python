class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def description(self):
        return "%s is %s years old" % (self.name, self.age)


    def speak(self, sound):
        return "%s says %s" % (self.name, sound)


jack = Dog("Jack", 4)

print(jack.description()) # распечатает 'Jack is 4 years old'
print(jack.speak("Woof Woof")) # распечатает 'Jack says Woof Woof'
print(jack.speak("Bow Wow")) # распечатает 'Jack says Bow Wow'
        
