class Bird:
    def sound(self):
        return "Chirp"

class Crow(Bird):
    def sound(self):
        return "Caw"

class Sparrow(Bird):
    def sound(self):
        return "Tweet"

def make_sound(bird):
    print(bird.sound())

make_sound(Crow())
make_sound(Sparrow())
