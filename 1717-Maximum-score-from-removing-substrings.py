#https://leetcode.com/problems/maximum-score-from-removing-substrings/description/

#%%
s = "aabbaaxybbaabb"
x = 5
y = 4
#%%
score = 0
if y>x:
    while 'ba' in s or 'ab' in s:
        while 'ba' in s:
            score += y * s.count('ba')
            s = s.replace('ba','')
        score += x * s.count('ab')
        s = s.replace('ab','')
else:
    while 'ba' in s or 'ab' in s:
        while 'ab' in s:
            score += x * s.count('ab')
            s = s.replace('ab','')
        score += y * s.count('ba')
        s = s.replace('ba','')
score
s
# %%
s = "aabbaaxybbaabb"

score = 0
stack = []
print(s)

for i in range(len(s)):
    
    if stack[-1:] == ['a'] and s[-(i+1)] == 'b': # ba
        print(f'removing {stack[-1]}')

        stack.pop()
        score += y
    elif stack[-1:] == ['b'] and s[-(i+1)] == 'a': # ab
        print(f'removing {stack[-1]}')
        stack.pop()
        score += x
    else:
        stack.append(s[-(i+1)])
        print(s[-(i+1)])
    
print(score)
print(''.join(reversed(stack)))
    
# %%
while 'ba' in s or 'ab' in s:
        while 'ab' in s:
            score += x * s.count('ab')
            s = s.replace('ab','')
        score += y * s.count('ba')
        s = s.replace('ba','')
score
# %%
stack=[]
stack[-1:][0]
# %%
