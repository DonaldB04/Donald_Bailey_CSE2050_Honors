#for use to randomize list of names
import random

def make_pairs(list, people, pairs):
    '''
    makes the pairs of people and returns them as tuples in a list
    '''

    #lets the user enter the amount of names based on difficulty chosen
    for i in range(people):
        name = input('Enter a name ')
        people_list.append(name)
    
    #randomizes people into a new list as tuples
    list_pair = []
    for i in range(pairs):
        person1 = list.pop(random.randrange(len(list)))
        person2 = list.pop(random.randrange(len(list)))
        pair = (person1, person2)
        list_pair.append(pair)
    
    #retuen random list
    return list_pair

#select the difficulty and establish a people list
user_difficulty = input('Please Enter Diffficulty - Easy (4 pairs), Normal(8 pairs), Hard(12 pairs) ')
people_list = list()

#easy difficulty (4 pairs)
if user_difficulty == 'Easy' or 'easy':

    pair_list = make_pairs(people_list, 8, 4)

#normal difficulty (8 pairs)
elif user_difficulty == 'Normal' or 'normal':
  
    pair_list = make_pairs(people_list, 16, 8)

#hard difficulty (16 pairs)
elif user_difficulty == 'Hard' or 'hard':

    pair_list = make_pairs(people_list, 24, 12)

#while there are still pairs to be guessed
while len(pair_list) != 0:

    #enter guesses
    person_guess = input('Enter the first person')
    person2_guess = input('Enter their partner')

    #checks is guesses are in the list together
    if (person_guess, person2_guess) in pair_list:
        
        pair_list.remove((person_guess, person2_guess))
        print('Correct!')
    
    elif (person2_guess, person_guess) in pair_list:

        pair_list.remove((person2_guess, person_guess))
        print('Correct!')
    
    else:
        print('Wrong! Try again')

#If all goes well you win
print('Congratulations, You Win!!')

