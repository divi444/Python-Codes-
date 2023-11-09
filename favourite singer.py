#this is solution for the problem favourite singer in hackerrank 
ab = int(input())
g = input()
g = list(map(int, g.split()))
dictionaryA = {}
for i in g:
    if i not in dictionaryA:
        dictionaryA[i] = 1
    else:
        dictionaryA[i] += 1
maxiof = max(dictionaryA.values())
p = list(dictionaryA.values())
Y = p.count(maxiof)
print(Y)

