#Type Conversion functions str, int, float, bool 

#Allow us to convert from one datatype to another, as long as it qualifying data

my_str = '5'
print(my_str)
print(type(my_str))

#Converting from string to int
my_int = int(my_str)
print(my_int)
print(type(my_int))

#Converting from int to float

my_float = float(my_int)
print(my_float)
print(type(my_float))

#Converting from float to string

my_str = str(my_float)
print(my_str)
print(type(my_str))


my_bool = False
print(my_bool)
print(type(my_bool))

bool_str = str(my_bool)
print(bool_str)
print(type(bool_str))

bool_int = int(my_bool)
print(bool_int)
print(type(bool_int))


word = ['items']

if word:
    print('We have value')