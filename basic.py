# class code: message is not specific to each object. Instead, it is executed once per class.

import sys


class ParentClass:
    sys.stdout.write("Hello from a world where we adapt from nature. \n")  # class code
    eyes = 2
    hair = 'black'
    hair_strands = 1000


sys.stdout.write("Before creation of objects. \n")

object_child1 = ParentClass()
object_child1.hair_strands = 1700
object_child1.hair = 'brown'
object_child2 = ParentClass()
object_child2.hair_strands = 2000
object_child2.hair = 'red'

sys.stdout.write("After creation of objects. \n")

sys.stdout.write("Child 1 has " + str(object_child1.hair_strands) + " hair strands" + "\n")
sys.stdout.write("Child 2 has " + str(object_child2.hair_strands) + " hair strands" + "\n")
sys.stdout.write("Child 1 has " + str(object_child1.hair) + " hair." + "\n")
sys.stdout.write("Child 2 has " + str(object_child2.hair) + " hair." + "\n")
sys.stdout.write("Child 1 has " + str(object_child1.eyes) + " eyes" + "\n")
sys.stdout.write("Child 2 has " + str(object_child2.eyes) + " eyes" + "\n")

sys.stdout.write(str(object_child1) + "\n")
sys.stdout.write(str(object_child2) + "\n")
