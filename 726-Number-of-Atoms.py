#%%
formula = "H2O"

formulat_stack = []
i = 0
while i < len(formula):
    c = formula[i]
    if c == "(":
        continue
    elif c == ")":
        subfromula_count = 0
        while i + 1 < len(formula) and formula[i+1].isdigit():
            subfromula_count += formula[i+1]
            i+=1

        if len(subfromula_count) == 0:
            atom_count=1
        else:
            atom_count=int(atom_count)
        
    elif c.isupper():
        element = c
        atom_count = ''

        if i+1 <= len(formula) and c.islower():
            element = formula[i:i+2]
            i+=1

        while i + 1 < len(formula) and formula[i+1].isdigit():
            atom_count += formula[i+1]
            i+=1

        if len(atom_count) == 0:
            atom_count=1
        else:
            atom_count=int(atom_count)
        

# %%
