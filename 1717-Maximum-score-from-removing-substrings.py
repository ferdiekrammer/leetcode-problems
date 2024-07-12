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
# %%
