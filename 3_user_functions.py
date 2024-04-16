# USER DEFINED FUNCTIONS

#They give us repeatable power

#Syntax

#def function_name(parameters):
#   code block to be executed on function call


#--- Simple Function

def greeting():
    print('Hello there traveler!')


greeting() #Calling a function by it's name dont forget ()
greeting() #multiple calls
greeting()

#--- Function with Parameters
# establish a required variable/value for our function

def personalized_greet(name):
    print(f'Hello {name}, Welcome to Functions!')

#The value that we pass in for a parameter is called and ARGUMENT
personalized_greet('Dylan')
personalized_greet('Travis')
personalized_greet('Rhia')


#--- More Complex Example

#function to give info about ct classes

def class_info(instructors, students):
    print(f'This class is taught by {instructors[0]} and {instructors[1]}')
    class_size = len(students)
    print(f'It has {class_size} students:')
    for student in students:
        print(student)

ins_146 = ['Dylan', 'Travis']
students_146=['Harsh', 'AJ', 'Noach', 'Isaias', 'Marie']

ins_144 = ['Ryan', 'Alex']
stus_144 = ['Billy Bob', 'Barney', 'Ted', 'Marshall', 'Lily','Robin']

class_info(ins_146, students_146)

class_info(ins_144, stus_144)