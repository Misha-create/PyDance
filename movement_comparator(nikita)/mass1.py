
# coding: utf-8

Ideal_file = open("Ideal.txt", "r")
Player_file = open('Player.txt')
Player_massive = Player_file.read().split()
Ideal_massive = Ideal_file.read().split()

type_1 = []
time_player = []
type_id = []
time_begin_id = []
time_end_id = []
Player = []
Ideal = []
points = 0

for i in range(len(Player_massive)):
    if (i % 2 == 0):
        type_1.append(Player_massive[i])
    elif (i % 2 == 1):
        time_player.append(int(Player_massive[i]))

for i in range(len(Ideal_massive)):
    if (i % 3 == 0):
        type_id.append(Ideal_massive[i])
    elif (i % 3 == 1):
        time_begin_id.append(int(Ideal_massive[i]))
    elif (i % 3 == 2):
        time_end_id.append(int(Ideal_massive[i]))

print(type_1)
print(time_player)
print(type_id)
print(time_begin_id)
print(time_end_id)

Player.append(type_1)
Player.append(time_player)

Ideal.append(type_id)
Ideal.append(time_begin_id)
Ideal.append(time_end_id)

for i in range(len(Ideal[0])):
    if (Player[0][i] == Ideal[0][i]):
        if ((Player[1][i] <= Ideal[2][i]) and (Player[1][i] >= Ideal[1][i])):
            points += 1

print(points)
