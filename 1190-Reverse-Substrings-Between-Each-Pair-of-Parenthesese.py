# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/?envType=daily-question&envId=2024-07-11

# %%
s = "(abcd)"
# %%
stack = []
for i in s:
    if i == ')':
        sub_stack = []        
        while stack[-1] != '(':
            sub_stack.append(stack.pop())
        stack.pop()
        stack.extend(sub_stack)
    else:
        stack.append(i)
        
new_s = ''.join(stack)
new_s