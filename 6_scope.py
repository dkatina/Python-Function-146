#In python we have two kinds of scope, Global Scope, and Local Scope

#The scope determines what variables are accessible


#Global scope is anywhere out side of your functions

x = 7 #All these variables are considered to be golbal variables and can be accessed anywhere in your code
a = 'Words'
alist = ['item', 'item', 'item']


if x:
    print(x)


#Local scope is created inside of functions

def local_func():
    y =7 #This is local variable, and can only be referenced within this function

    print(x) # can call global variables into local scope

print(y) # cannot call local vars into global scope

