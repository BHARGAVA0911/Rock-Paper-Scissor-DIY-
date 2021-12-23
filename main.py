from random import randint
system=['rock','paper','scissor']
print()
print('Rock, Paper, Scissor game')
print()
print('Rules of the game: ')
print('1. Rock WINS in front of Scissor.')
print('   Rock LOOSES in front of Paper.')
print()
print('2. Paper WINS in front of Rock.')
print('   Paper LOOSES in front of Scissor.')
print()
print('3. Scissor WINS in front of Paper.')
print('   Scissor LOSSES in front of Rock.')
print()
print('There will be total five rounds of play:')
print('For every win in each round a score of 1 will be added. Total score will be displayed at the end of the game')
print()
score=0
tie=0
i=1
while (i<6):
    print()
    print('Round',i)
    player=input('Enter your move among rock, paper, scissor or give end to end game: ').lower()
    computer = system[randint(0, 2)]
    if player not in system:
        print('sorry wrong move. Please choose among rock, paper, or scissor')
    elif player == computer:
        print('Its a tie between the player and the system')
        tie+=1

    elif player == 'rock':
        if computer =='paper':
            print('System choose',computer,'so system wins')
        else:
            print('System choose',computer,'so you win this round')
            score+=1

    elif player == 'scissor':
        if computer =='rock':
            print('System choose',computer,'so system wins')
        else:
            print('System choose',computer,'so you win this round')
            score+=1

    elif player == 'paper':
        if computer =='scissor':
            print('System choose',computer,'so system wins')
        else:
            print('System choose',computer,'so you win this round')
            score+=1
    i+=1
print()
print('score = ',score)
print('tie = ',tie)
system_score = 5-tie-score
print('system score',system_score)
print()
if score == system_score:
    print('Its a tie between you and the system')
elif score > system_score:
    print('Congratulations!! You won the game')
else:
    print('Opps!! Sorry you lost the game')
    print('Better luck next time')



