# coding: utf-8

Ideal_file = open("Ideal.txt", "r")
Player_file = open('Player.txt')
Player_massive = Player_file.read().split()
Ideal_massive = Ideal_file.read().split()

type_1 = []
time_begin = []
time_end = []
type_id = []
time_begin_id = []
time_end_id = []
Player = []
Ideal = []
points = 0

for i in range(len(Player_massive)):
    if (i % 3 == 0):
        type_1.append(Player_massive[i])
    elif (i % 3 == 1):
        time_begin.append(int(Player_massive[i]))
    elif (i % 3 == 2):
        time_end.append(int(Player_massive[i]))

for i in range(len(Ideal_massive)):
    if (i % 3 == 0):
        type_id.append(Ideal_massive[i])
    elif (i % 3 == 1):
        time_begin_id.append(int(Ideal_massive[i]))
    elif (i % 3 == 2):
        time_end_id.append(int(Ideal_massive[i]))

print(type_1)
print(time_begin)
print(time_end)
print(type_id)
print(time_begin_id)
print(time_end_id)

Player.append(type_1)
Player.append(time_begin)
Player.append(time_end)

Ideal.append(type_id)
Ideal.append(time_begin_id)
Ideal.append(time_end_id)

for i in range(len(Ideal[0])):
    if (Player[0][i] == Ideal[0][i]):
        mid_player = abs(Player[2][i] - Player[1][i])
        mid_ideal = abs(Ideal[2][i] - Ideal[1][i])
        if (((Player[1][i] <= (mid_ideal) / 2) and (Player[1][i] >= Ideal[1][i])) or
                ((Player[2][i] >= (mid_ideal) / 2) and (Player[2][i] <= Ideal[2][i]))):
            points += 0.5
        elif (mid_player <= mid_ideal):
            points += 1

print(points)
