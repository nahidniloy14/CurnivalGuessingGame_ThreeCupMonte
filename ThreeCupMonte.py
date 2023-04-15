from random import shuffle

my_list = [1, 2, 3]


# Shuffle the cup
def cup_shuffle(shuffle_list):
    shuffle(shuffle_list)
    return shuffle_list


#print(cup_shuffle(my_list))

shuffle_index=my_list.index(1)+1
#print(shuffle_index)

#User guess a cup
def player_guess():
    guess = ''
    while guess not in ['3', '1', '2']:
        guess = input("Guess in which cup the ball might be 1, 2 or 3: ")
    return int(guess)




user_index=player_guess()
#print(user_index)

if shuffle_index == user_index:
    print("Correct Guess")
else:
    print("Wrong Guess")
    print("The ball is in cup no : " +str(shuffle_index))
