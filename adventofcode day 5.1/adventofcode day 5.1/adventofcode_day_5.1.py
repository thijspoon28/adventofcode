input_file = open('input.txt', "r")  # opens the file in read mode
input = [(line) for line in input_file.read().splitlines()]
input_file.close()

answer = 0

for i in input:
    print(i)
    id = 0

    numberR = 64
    numberC = 4
    row = 0
    colomn = 0
    for x in i:
        print(x)
        if x == 'B':
            row = row + numberR
            numberR = numberR / 2
        if x == 'F':
            numberR = numberR / 2
            
        if x == 'R':
            colomn = colomn + numberC
            numberC = numberC /2

        if x == 'L':
            numberC = numberC /2

        print('row')
        print(row)
        print('colomn')
        print(colomn)
    id = row * 8 + colomn
    print('id')
    print(id)
    if id > answer:
        answer = id
        print('YESSSSSSSSSSSSSSS')
        print(answer)
print(answer)
print(answer)
print(answer)
        

