# class code: message is not specific to each object. Instead, it is executed once per class.
# self acts as a reference to the current instance of a class
# Using self as the first parameter to the method binds the class attributes with that method’s arguments.
# self parameter allows us to access methods and attributes that are within the class
# make sure to put those methods under the most appropriate class.

import sys


class ParentClass:
    sys.stdout.write("Hello from a world where we adapt from nature. \n")  # class code
    eyes = 2
    hair = 'black'
    hair_strands = 1000

    def a_method_in_the_class(self):
        sys.stdout.write("Hello from inside a method \n")

    def method1(self):
        sys.stdout.write("Hello from inside a method1 \n")
        # method2() gives NameError: name 'method2' is not defined
        self.method2()
        # self.method2()  is necessary as method2 is a member of the object in which method1 is contained.
        sys.stdout.write("\n The value of hair is " + self.hair)

    def method2(self):
        sys.stdout.write("Hello from inside a method2 \n")


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

object_child1.a_method_in_the_class()
'''
#    def a_method_in_the_class(): # without self 
        sys.stdout.write("Hello from inside a method \n")
        
    TypeError: a_method_in_the_class() takes 0 positional arguments but 1 was given
'''


object_child1.method1()
