s = input()

index = 0

while True:
    if index == len(s):
        break
    if s[index] == 'B':
        index = index + 1
    else:
        break
    
leftPart = s[:index]
leftIndex = index

index = len(s) - 1

while True:
    if index == -1:
        break
    if s[index] == 'W':
        index = index - 1
    else:
        break
    
rightPart = s[index+1:]
rightIndex = index

middlePart = s[leftIndex: rightIndex+1]



midle_part_list = list(middlePart)
countW = midle_part_list.count('B')



solveLeft = middlePart[:countW]
solveRight = middlePart[countW:]



decreaseLeftPart = list(solveLeft).count('W')
decreaseRightPart = list(solveRight).count('B')

if decreaseLeftPart != decreaseRightPart:
    raise Exception('не удалось посчитать')



count_B_insert = len(solveLeft) - decreaseLeftPart
count_W_insert = len(solveRight) - decreaseRightPart

print(decreaseLeftPart * 2)

res = leftPart + 'B'*count_B_insert + 'W'*count_W_insert + rightPart

if len(res) != 0:
    print(res)
else:
    print('НИКОГО НЕ ОСТАЛОСЬ')
