import re 

hand = open('test.txt')
num = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('([0-9]+)', line)
    num  = num + stuff
sum = 0
for nums in num:
    sum = sum + int(nums)

print(sum)

