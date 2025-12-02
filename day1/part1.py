'''
Advent of Code Day 1 - unlocking the safe
'''

#setting up base values
dial = 50
count = 0

#open file
with open('input.txt') as file:
    #split inputs
    for i in file:
        direction = i[0]
        amount = int(i[1:])
        
        match direction:
            case 'L':
                dial -= amount

            case 'R':
                dial += amount

        #correct overflow
        dial %= 100

        if dial == 0:
            count += 1

print(count)
