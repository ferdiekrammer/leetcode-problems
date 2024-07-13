# %%

# positions = [5,4,3,2,1]
# healths = [2,17,9,15,10]
# directions = "RRRRR"
# # expected return : [2,17,9,15,10]

positions = [3,5,2,6]
healths = [10,10,15,12]
directions = "RLRL"
# expected return : [14]

# positions = [1,2,5,6]
# healths = [10,10,11,11]
# directions = "RLRL"
# # expected return : []

idx_map = {p: i for i,p in enumerate(positions)}
stack = []
positions.sort()
# print(positions)
# print(idx_map)
for p in positions:
    print('p ',p)
    i = idx_map[p]
    # print('i ',i,directions[i])
    if directions[i] == 'R':
        stack.append(i)
    elif directions[i] == 'L':
        while stack and directions[stack[-1]] == "R":
            stack_idx = stack[-1]
            if healths[i] > healths[stack_idx]:
                # print(healths[i] , healths[stack_idx])
                healths[stack_idx] = 0
                healths[i] -= 1
                stack.pop()
            elif healths[i] < healths[stack_idx]:
                healths[stack_idx] -= 1
                healths[i] = 0
                break
            elif healths[i] == healths[stack_idx]:
                healths[i] = healths[stack_idx] = 0
                stack.pop()
                break
    print(healths)


print(f'final healths : {[h for h in healths if h != 0]}')
# %%
