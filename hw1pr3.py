import random
user = input("Choose your weapon: ")
comp = random.choice(['rock','paper','scissors'])
print()

print('The user (you)   chose', user)
print('The computer (I) chose', comp)
print()

if user == 'rock':
        if ",user," 'rock' "and" ",comp," == 'rock':
            print('its a tie')
        if comp == 'scissors':
            print('aw i lost')
        else:
             print('Ha! I really chose paper--I WIN!')
if user == 'paper':
        if "user" 'paper' "and" "comp" == 'paper':
            print('a tie again')
        if comp == 'rock':
            print('aw i lost')
        else:
             print('I beat you again i have scissors! I WIN!')
if user == 'scissors':
        if ",user," 'scissors' "and" ",comp," == 'scissors':
            print('its tied. another game?')
        if comp == 'paper':
            print('aw i lost')
        else:
             print('Im always a step ahead of you. I have a rock! YOU LOSE!')
