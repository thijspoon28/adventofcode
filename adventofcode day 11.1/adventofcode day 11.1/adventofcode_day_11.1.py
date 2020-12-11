input_file = open('input.txt', "r")  # opens the file in read mode
input = [(line) for line in input_file.read().splitlines()]
input_file.close()

subcycle = -1
cycle = -1

def check(index1, index2):
    count1 = 0
    count2 = 0
    for i in range(3):
        for x in range(3):
            if input[cycle -1 +i][subcycle -1 +x] == '#':
                count1 += 1
            if input[cycle -1 +i][subcycle -1 +x] == 'L':
                count2 += 1




for i in input:
    print(i)
    cycle += 1
    for x in input[cycle]:
        subcycle += 1
        print(x)
        if x == '.':
            continue
        if x == 'L':
            check(cycle, subcycle)


