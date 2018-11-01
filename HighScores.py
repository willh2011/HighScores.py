'''
Developers: William Haskins, Edward Allington, Dylan McKinney
'''
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

# scoresEntered = 0
# while scoresEntered < 5: