"""
	hero-villian game
"""

no_of_players=int(input('No of players:'))

hero=[]
villian=[]
win=0

print('Enter strength of hero:')
for i in range(no_of_players):
    strength=int(input('Enter strength:'))
    hero.append(strength)

print('Enter strength of villian:')
for i in range(no_of_players):
    power = int(input('Enter power:'))
    villian.append(power)

hero.sort()
villian.sort()

for i in range(no_of_players):
    if hero[i]>=villian[i]:
        win+=1

if win==no_of_players:
    print('Win!')
else:
    print('Lose')