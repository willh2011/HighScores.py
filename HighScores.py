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
counter = 0
highScore = 0
highest = 0
while entries < 5:
    playerEntry = input("What is the player's name?")
    players.append(playerEntry)
    scoreEntry = int(input(f"What is {playerEntry} score? "))
    scores.append(scoreEntry)
    entries += 1
while counter < len(scores):
    if scores[counter] > highScore:
        highScore = scores[counter]
        highest = counter
    counter += 1
print(f"High player's name is {players[highest]} and their high score is {scores[highest]}")

# scoreEntry = [  3]
# print(scoreEntry)

# while loop < 3:
#     if int(scores[0]) > int(loop2):
#         print(scores)
#         loop += 1
#         scores = -1
#     loop2 -= 1

# scoresEntered = 0
# while scoresEntered < 5:
