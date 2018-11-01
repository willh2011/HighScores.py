'''
Developers: William Haskins, Edward Allington, Dylan McKinney
'''
loop = 0
loop2 = 999
#players = [["Player1", "Score"], ["Player2", "Score"], ["Player3", "Score"], ["Player4", "Score"], ["Player5", "Score"]]
players = []
scores = []
entries = 0
playerEntry = ''
scoreEntry = ''
top3 = ''
while entries < 5:
    playerEntry = input("What is the player's name?")
    players.append(playerEntry)
    scoreEntry = input(f"What is {playerEntry} score? ")
    scores.append(scoreEntry)
    entries += 1
for i in range(len(scores)):
    print([1, 2, 3, 4, 5])
    
while loop < 3:
    if scores[0] > loop2:
        print(scores[0])
        loop += 1
        
    loop2 -= 1

# scoresEntered = 0
# while scoresEntered < 5:
