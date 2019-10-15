s = input()
score = {'Stuart':0, 'Kevin':0}

l, l1 =[], []
for i in range(len(s)):
    if s[i] in 'AEIOU':
        for j1 in range(1, len(s)-i+1):
            w1 = s[i:i+j1]
            if not w1 in l:
                l.append(w1)

    else:
        for j in range(1, len(s)-i+1):
            w = s[i:i+j]
            if not w in l1:
                l1.append(w)

for k in l:
    
    score['Kevin']+=s.count(k)
for k1 in l1:
    score['Stuart']+=s.count(k1)

a = max(list(score.values()))
print(l)
print(l1)
print(score)
if score['Stuart']!=score['Kevin']:
    for x in score:
        if score[x]==a:
            print(str(x)+' '+str(a))
else:
    print('Draw')
