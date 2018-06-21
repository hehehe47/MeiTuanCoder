def insert_into_list(pro_k, k, pro_indvi):
    if len(pro_k) < k:
        pro_k.append(pro_indvi)
    else:
        pro_k = sorted(pro_k, reverse=True)
        last = pro_k.pop()
        if last < pro_indvi:
            pro_k.append(pro_indvi)
        else:
            pro_k.append(last)
    return pro_k


l = [1, 2, 3, 4, 5]

k = 3
pro_k = []
for pro_indvi in l:
    pro_k = insert_into_list(pro_k, k, pro_indvi)
print(pro_k)
