# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

data = sys.stdin.readlines()

items = int(data[0].strip())
data = data[1:]
lst = []

for line in data:
    #print line
    line = line.strip()
    if line:
        lst.append(int(line))

candies = [0]*items
if lst[0] <= lst[1]:
    candies[0] = 1
if lst[items-1] <= lst[items-2]:
    candies[items-1] = 1
for i in range(1, items-1):
    if lst[i] <= lst[i-1] and lst[i] <= lst[i+1]:
        candies[i] = 1
inc = False
start = False
startCount = 0
for i in range(1, items):
    if candies[i-1] == 1 and candies[i] == 0:
        start = True
    if start:        
        startCount += 1
        if lst[i] > lst[i-1] and candies[i] == 0:
            candies[i] = candies[i-1]+1
        else:
            if startCount >= 2 and candies[i] != 1 and lst[i] != lst[i-1]:
                candies[i-1] = 0                
            start = False
            startCount = 0

for i in range(items-2, -1, -1):
    if candies[i+1] == 1 and candies[i] == 0:
        start = True
    if start:        
        if lst[i] > lst[i+1] and candies[i] == 0:
            candies[i] = candies[i+1]+1
        else:    
            start = False

for i in range(items-1):
    if candies[i] == candies[i+1]:
        if lst[i] > lst[i+1]:
            candies[i] += 1
        if lst[i] < lst[i+1]:
            candies[i+1] += 1
    elif candies[i] < candies[i+1]:
        if lst[i] > lst[i+1]:
            candies[i] = candies[i+1]+1
    elif candies[i] > candies[i+1]:
        if lst[i] < lst[i+1]:
            candies[i+1] = candies[i]+1
             
#print candies
print sum(candies)
