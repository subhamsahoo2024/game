import random as rd
def roll():
    value=rd.randint(1,6)
    return value

while True:
    numplayer=input("Enter number of players(2-6):")
    if numplayer.isdigit():
        numplayer=int(numplayer)
        if(numplayer<2 or numplayer>6):
            print("players should be between 2 to 6\nenter again!")
            continue
        break
    else:
        print("Invalid input try again!")
        continue
while True:
    maxscore=input("Enter maximum score:")
    if maxscore.isdigit():
        maxscore=int(maxscore)
        break
    else:
        print("Invalid input try again!")
        continue
player_scores=[0 for i in range(numplayer)]
dummy=[-1 for i in range(numplayer)] 
while max(player_scores)<maxscore:
    for i in range(numplayer):
        print("Players",i+1,"chance")
        print("Your previous score was",player_scores[i])
        current_score=0
        while True:
            yn=input("Do you want to roll(y/n):")
            if yn.isalpha()==0:
                print("Enter a y or n!")
                continue
            if (yn.lower()=='n'):
                break
            value=roll()
            print("You rolled a",value)
            if (dummy[i]==-1):
                if value==6:
                    print("your score counting is started")
                    dummy[i]=0
                    continue
                else:
                    print("your score counting is not started")
                    break
            elif value==1:
                print("Your chance ended")
                current_score=0
                print("Current Score is",current_score)
                break
            current_score+=value
            print("Current Score is",current_score)
        player_scores[i]+=current_score
        print("Total Score is",player_scores[i],"\n")
maxvalue=max(player_scores)
print("Player",player_scores.index(maxvalue)+1,"won with a score of",maxvalue)
        
