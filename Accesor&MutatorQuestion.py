class Customer:
    def __init__(self, name, phoneno):
        self.name = name
        self.phoneno = phoneno

    def get_name(self):
        return self.name

    def get_phoneno(self):
        return self.phoneno

    def set_phoneno(self,phoneno):
        self.phoneno = phoneno
        return self.phoneno

c = Customer("Arbaz",9768585015)

print(c.get_name())
print(c.get_phoneno())
print(c.set_phoneno(9773583448))
