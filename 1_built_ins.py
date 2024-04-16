#Python built in Functions

#-- print(value) : prints this value to your terminal
#One of the most important tools in debugging and viewing stared values

print('Hello there')
var = 'A value inside this var'
print(var)

#String Concatenation : adding string together

word1 = 'Hello'
word2 = 'World'
word3 = word1 + word2
print(word3)

#Make sure to add spacing

word4 = word1 + ' ' + word2
print(word4)

#String Formatting : embedding variables directly into a string

#--f string

attribute = 100 #can incorporate ints directly
fav_food = 'Tacos'
statement = f'Hi, my fav food is {attribute} {fav_food}'
print(statement) #can also print the f string directly without saving to var

#-- .format()

age = 99
statement = 'Hi, I am {} years old'.format(age)
print(statement)

#-- input() : retrieve user input, and return it as a string

#-------UNCOMMENT THE FOLLOW LINES TO SEE HOW INPUT WORKS

# dog_name = input('What is your dogs name? ')
# print( f'Wow, I love the name {dog_name}!')

# age = int(input('How old are you? '))
# birthday = age + 1
# print(f'On you birthday you will be {birthday}!')

#-- type() : returns the datatype of the particular value 


var1 = True
var2 = 'Words'
var3 = 5
var4 = 5.0
var5 = ['item', 'item', 'item']


print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))


#--- len() : returns the length of an iterable as an int

var5 = ['item', 'item', 'item']
print(len(var5))

name = 'Dylan'
print(len(name))


#-- isinstance(var, type) return True or False depending on if the var is that type.
# types: str, int, float, bool, list

var = 'Hi there'
num = 4
print(isinstance(num, int))

forcast = ['Monday', 84.2, 'Tuesday', 78.9, 'Wednesday', 82.1, 'Thursday', 40.2]

total = 0
temp_count = 0
for item in forcast:
    if isinstance(item, float):
        total += item
        temp_count += 1

average = total / temp_count
print(average)


#-- abs() : returns the absolute value of a number (the positive value of that num)

x = 6
y = -3
print(abs(y))


#-- round(): rounds any float to the nearest whole number, returns an int
# .6 and up round up, .5 and down round down

a = 4.5
print(round(a))


#-- sum(list) : returns the total sum of a list of numbers

nums = [1,2,3,4,5,6.0]
total = sum(nums)
print(total)


#-- min(list) : returns the minimum value of a list of numbers

minimum = min(nums)
print(minimum)


#-- max(list) : return the maximum valu of a list of numbers

maximum = max(nums)
print(maximum)

#-- pow(num, exp) : raises a num to the power of exp, substitute for ** 

print(pow(4,3)) # == 4**3

#-- divmod(num, divisor) : returns a tuple, of the quotient annd the remainder

print(divmod(8, 5))
tup = divmod(8, 5)
print(tup[0])
print(tup[1])