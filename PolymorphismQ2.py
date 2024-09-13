class English:

    def greeting(self):
        print("Hello")

class French:

    def greeting(self):
        print("Bonjour")

def greet(language):
    language.greeting()

a = English()
b = French()
greet(a)
greet(French())