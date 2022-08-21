def flatten(x):
    for i in x:
        if isinstance(i,list):
            flatten(i)
        else:
            l_new.append(i)
flatten(l)
print(l_new)
