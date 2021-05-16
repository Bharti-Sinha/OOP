class Bird:
     def intro(self):
       print("I am warm-blooded vertabrate with feathers, a beaked jaw and wings")
 
     def flight(self):
       print("I don't know how I should fly unless you tell me what kind of bird I am...\n")
 
class Parrot(Bird):
     def flight(self):
       print("As a parrot, I fly in the sky\n")
 
class Penguin(Bird):
     def flight(self):
       print("As a penguin, I fly only under water\n")

#obj_bird = Bird()
#obj_parr = Parrot()
#obj_peng = Penguin()
#
#obj_bird.intro()
#obj_bird.flight()
#
#obj_parr.intro()
#obj_parr.flight()
#
#obj_peng.intro()
#obj_peng.flight()

birds = []
birds.append(Bird())
birds.append(Parrot())
birds.append(Penguin())

for i in birds:
    i.intro()
    i.flight()
