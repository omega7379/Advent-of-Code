'''
Advent of Code Day 1 - unlocking the safe
'''

#base values
dial = 50
count = 0

#open file
with open('input.txt') as file:
    for i in file:
        direction = i[0]
        amount = int(i[1:])
        step = 1 if direction == 'R' else -1

        #how many full rotations
        count += amount // 100

        #partial rotations that go through 0
        for _ in range(amount % 100):
            dial = (dial + step) % 100
            if dial == 0:
                count += 1

print(count)

