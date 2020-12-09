input_file = open('input.txt', "r")  # opens the file in read mode

list = []
info = []

go = 1
while go > 0:
    line = input_file.readline()
    if line == "\n":
        string = ' '.join(list)
        info.append(string)
        list = []
        print(info)
    else:
        list.append(line)
        print(line)
    if not line:
        go = 0
input_file.close()


answer = 0
checks = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

print(input)
for x in info:
    if all(d in x for d in checks):
        print('yess')
        answer += 1
    else:
       print('no')

print(answer)

#if ('ecl:' & 'iyr:' & 'eyr:' & 'hgt:' & 'hcl:' & 'ecl:' & 'pid:') in x:

#if any(x in a_string for x in matches):