#Different Types of Parameters

#Basic Parameters : assume their value from arguments passed in

def name_printer(first, last, middle):
    print(f'Hello {first} {middle} {last}.')

#--Positional Arguments : the postion of the argument determines which parameter it becomes the value of
name_printer('Dylan' ,'Katina', 'Michael')

#-- KeyWord Arguments : we explicitly state which parameter takes which value
name_printer(first='Dylan', middle='Michael', last='Katina')

#--- Default Parameters : give a param a default value if none is passed in

def tomb_stone(birth, death='TBD'):
    print(f'''
    This Person lived from {birth} 
            to {death}''')
    
tomb_stone('1-18-1925', '4-16-2024') #If we don't pass in an argument for death it will take the default 'TBD'

#One thing to note, default params need to come after all non-default params

#-------Uncomment to see this break

# def breaking(broken=True, working):
#     pass # we can use pass as a temporary placeholder for our function codeblock


#--- *args : unknown number of arguments, brought into the function as a tuple



def vet_hands(staff, *vols):
    print(f'On staff today we have {staff[0]} and {staff[1]}!')
    if vols:
        print('They will be assisted by the following volunteers:')
        for vol in vols:
            print(vol)

vet_hands(['Dr. Adam', 'VT Jones'], 'Dylan', 'Grace', 'Jackson', 'Craig', 'Phillip')

#--- **kwargs : unknown amount of keyword arguments, brought into the function as a Dictionary

def routine(**daily_events):
    print(daily_events)

routine(morning='I wake up and eat breakfast', mid_morning='walk my dog', afternoon='grading and prepping', evening='Class',dinner_time='Time to eat', night='sleep')




