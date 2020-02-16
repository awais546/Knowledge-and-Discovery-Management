inp = {'A':['B','C','D'],'B':['A','C','D','E'],'C':['A','B','D','E'],'D':['A','B','C','E'],'E':['B','C','D']}
split_list = []
#Mapper
for each in inp:
    for item in inp[each]:
        key = ''.join(sorted(each+item))
        split_list.append((key,inp[each]))
        print(key,inp[each])
shuffle_list = []
shuffle_list_check = []

#shuffling and reducing
for i in range(len(split_list)):
    for j in range(len(split_list)):
        if split_list[i][0] in shuffle_list_check:
            continue
        if i == j:
            continue
        if split_list[i][0] == split_list[j][0]:
            value = list(set(split_list[i][1]).intersection(set(split_list[j][1])))
            value.sort()
            shuffle_list.append((split_list[i][0],value))
    shuffle_list_check.append(split_list[i][0])
print('\nFinal output')
for each in shuffle_list:
    print(each)

