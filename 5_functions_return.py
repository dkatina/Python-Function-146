
#The goal of many functions is to produce something
#--- take something in as an argument
#--- manipulate it/ do something with it
#--- return the output

#simple function

def addition(a, b):
    return a + b


total = addition(2, 2)
print(total)

# doubler function takes in a list of nums, doubles all the nums and returns a list of doubled nums

def doubler(nums):
    doubled_nums = []
    for num in nums:
        doubled_num = num*2
        doubled_nums.append(doubled_num)
    
    return doubled_nums #return causes your function to terminate and returns whatever value adjacent

my_nums = [1,2,3,4,5,6]
dnums = doubler(my_nums)
print(dnums)

#----- No return

def greet_card(name):
    print(f'Have a nice day, {name}' )

card_message = greet_card('Travis')
print(card_message) #Function returns None if there was no return specified

#User reliant functions : function where we ask the user for input

#write a function to track the score of both teams in a basketball very quarter
#Ask how many point team1 and team2 scored at the end of every qurter
#print the final score and return the two scores as a list


#repeat a question exactly 4

def score_keeper(team1, team2):
    score_1 = 0
    score_2 = 0

    for quarter in range(4):
        points1 = int(input(f'How many points did {team1} score in quarter {quarter + 1}: '))
        points2 = int(input(f'How many points did {team2} score in quarter {quarter + 1}: '))
        score_1 += points1
        score_2 += points2
    
    print('Final Score')
    print(f'{team1}: {score_1}')
    print(f'{team2}: {score_2}')
    return [score_1, score_2]



score_keeper('Lakers', 'Hawks')
    