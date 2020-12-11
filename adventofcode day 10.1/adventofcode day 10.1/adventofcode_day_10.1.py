input_file = open('input.txt', "r")  # opens the file in read mode
input = [(line) for line in input_file.read().splitlines()]
input_file.close()

input = list(map(int, input))
input.sort()

print(input)
x = 0
for i in input:
    print('test')
    if i == (x + 1):
        print('somin')
        print(x)
        x += 1
    if i == (x + 2):
        print('somin')
        print(x)
        x += 2
    if i == (x + 3):
        print('somin')
        print(x)
        x += 3