input_file = open('input.txt', "r")  # opens the file in read mode
input = [(line) for line in input_file.read().splitlines()]
input_file.close()


y = 0
tree1=0
tree2=0
tree3=0
tree4=0
tree5=0

print(input)


for i in input:
    if y > 30:
        y -= 31
    if i[y] == '#':
        tree1 += 1
    print(i[y])
    print(tree1)
    y += 1
   

#answer = 64
y = 0
for i in input:
    if y > 30:
        y -= 31
    if i[y] == '#':
        tree2 += 1
    print(i[y])
    print(tree2)
    y += 3


#answer = 259
y = 0
for i in input:
    if y > 30:
        y -= 31
    if i[y] == '#':
        tree3 += 1
    print(i[y])
    print(tree3)
    y += 5


#answer = 65
y = 0
for i in input:
    if y > 30:
        y -= 31
    if i[y] == '#':
        tree4 += 1
    print(i[y])
    print(tree4)
    y += 7


#answer = 59
y = 0

for i in input[::2]:
    if y > 30:
        y -= 31
    if i[y] == '#':
        tree5 += 1
    print(i[y])
    print(tree5)
    y += 1
    


#answer = 35

print(tree1*tree2*tree3*tree4*tree5)
