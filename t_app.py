name = ['amir', 'sara', 'davood', 'tina']
def hello(name):
    for names in name:
        print("helli: " + names)

ints = 32
add = 0
while True:
    add += 1
    print(add)
    if add == ints:
        break

print("hello")

class Name:
    def __init__(self, name):
        self.name = name

    def run_1(self):
        log = self.name + " :"
        return log
    
dar = Name('amir')
dar.run_1()
ff = Name('good')
ff.run_1()
