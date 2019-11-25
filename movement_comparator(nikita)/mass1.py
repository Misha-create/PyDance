# coding: utf-8
import random
import time

n = 5
m = 3
type_1 = ["a", "b", "c", "d", "e"]
time_begin = [1, 3, 5, 6, 5]
time_end = [3, 5, 7, 8, 9]
type_id = ["a", "b", "c", "d", "e"]
time_begin_id = [1,2,3,6,5]
time_end_id = [4,4,5,8,9]
Player = []
Ideal = []
points = 0

Player.append(type_1)
Player.append(time_begin)
Player.append(time_end)

for i in range(len(Player[0])):
    for j in range(len(Player)):
        print(Player[j][i], end=' ')
    print()

Ideal.append(type_id)
Ideal.append(time_begin_id)
Ideal.append(time_end_id)

for i in range(len(Ideal[0])):
    for j in range(len(Ideal)):
        print(Ideal[j][i], end=' ')
    print()

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