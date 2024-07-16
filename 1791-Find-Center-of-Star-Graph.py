# %%
# https://leetcode.com/problems/find-center-of-star-graph/?envType=daily-question&envId=2024-07-16


edges = [[1,2],[2,3],[4,2]]
# Expected output : 2

edges = [[1,2],[5,1],[1,3],[1,4]]
# Expected output : 1

if edges[0][0] in edges[-1]: 
    print(edges[0][0])
else:
    print(edges[0][1])
# %%
