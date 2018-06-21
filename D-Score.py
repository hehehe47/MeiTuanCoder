'''
Description:
    小胖参加了人生中最重要的比赛——MedoC资格赛。MedoC的资格赛由m轮构成，使用常见的“加权标准分”的规则。每位选手需要参加所有的m轮的比赛。
    在一轮中，能取得的分数为自己的成绩除掉最高分的成绩。每个选手的总分为每一轮获得的分数乘上这一轮比赛占得比重。如果在某一轮比赛中所有人获得了零分，那么所有选手在这一轮获得的分数都为0分。
    比如说，资格赛一共3轮，三轮的权重分别为30%, 30%, 40%。在第一轮中，小胖获得了300分，最高分也为300分。
    在第二轮中，小胖获得了0分，最高分也为0分。在第三轮中，小胖获得了150分，最高分为300分，那么小胖的总分为(300/300)*30%+0*30%+(150/300)*40%=0.5。
    一共有n位选手参加了比赛，其中成绩最高的k位选手能够晋级到初赛。如果有多人在分数线上同分，那么系统会随机在这些同分的人中选取，选满k个晋级为止。
    小胖现在知道了每个选手每场比赛的成绩，但是由于他的疏忽，其中的某个人某场比赛的成绩消失了。所以更多人出线的情况变得未知起来。现在只知道成绩一定是0到C之间的一个整数（包含0和C）。
    小胖想知道对于每个人的出线情况是怎么样的，也就是一定能出线，一定不能出线还是有可能出线。

Input description:
    第一行四个正整数n,m,k,C (m <= 6, k <= n <= 500, C <= 500)。n选手 m轮数 k最高的几位 C潜在可能的最高分
    接下来一行m个整数w1, w2, ..., wm，表示每场比赛的权重，第i场比赛的权重为wi/(w1+w2+...+wm)，保证wi >= 0且1 <= w1 + w2 + ... + wm <= 1000。
    接下来n行每行m个整数，第i个整数表示这个选手在第i场比赛中获得的成绩。如果这个数字为-1表示这个数据丢失，保证恰好有一个-1。

Output description:
    n行每行输出一个1到3之间的整数。1表示一定出线，2表示一定不出线，3表示可能出线。

Examples:
    Input：              Output:
    4 2 2 100               1
    1 1                     3
    100 99                  3
    70 70                   2
    40 -1
    100 39



Correct rate:40.47%
'''


def insert_into_list(pro_k, k, pro_indvi):
    if len(pro_k) < k:
        pro_k.append(pro_indvi)
    else:
        pro_k = sorted(pro_k, reverse=True)
        last = pro_k.pop()
        if last < pro_indvi:
            pro_k.append(pro_indvi)
            pro2.append(last)
        else:
            pro_k.append(last)
            pro2.append(pro_indvi)
    return pro_k, pro2


n, m, k, c = tuple(map(int, input().split(' ')))
weight_list = list(map(int, input().split(' ')))
weight_sum, min_pro, max_pro = 0, 0, 0
for j in range(m):
    weight_sum += weight_list[j]
pro = []
pro_k, pro2 = [], []
d = {}
q = 0
for i in range(n):
    scores = list(map(int, input().split(' ')))
    pro_indvi = 0
    if -1 in scores:
        idx = scores.index(-1)
        scores[idx] = 0
        for s, w in zip(scores, weight_list):
            pro_indvi += float(s / c) * float(w / weight_sum)
        min_pro = pro_indvi
        pro_indvi = 0
        scores[idx] = c
        for s, w in zip(scores, weight_list):
            pro_indvi += float(s / c) * float(w / weight_sum)
        max_pro = pro_indvi
        d[i] = -1
        q = i
        continue
    for s, w in zip(scores, weight_list):
        pro_indvi += float(s / c) * float(w / weight_sum)
    d[i] = pro_indvi
    pro_k, pro2 = insert_into_list(pro_k, k, pro_indvi)
    pro.append(pro_indvi)
# pro_d = {}
# pro = sorted(pro, reverse=True)
# count, count2 = 0, 1
# for idx, p in enumerate(pro):
#     if idx + 1 <= k:
#         pro_d[p] = 1
#         count2+=1
#     elif p not in pro_d.keys():
#         pro_d[p] = 2
#     if p >= max_pro:
#         count += 1
# for p in pro:
#     if max_pro >= p >= min_pro and pro_d[p] != 2 and count2 != k:
#         pro_d[p] = 3
# if count + 1 == k and max_pro in pro_d and max_pro == pro[count - 1] and count2 != k:
#     pro_d[max_pro] = 1
#
# for i in range(n):
#     if d[i] != -1:
#         s = str(pro_d[d[i]])
#     else:
#         if count2 == k:
#             s = str(1)
#         elif pro_d[max_pro] != 2:
#             s = str(3)
#         else:
#             s = str(2)
#     if i != n - 1:
#         s += '\n'
#     print(s, end='')
# # print(pro[count])
# print(pro_k)
pro_k = sorted(pro_k, reverse=True)
pd = {}
for p in pro2:
    pd[p] = 2
if len(pro_k) < k:
    pro_k.append(-1)
if min_pro > pro_k[k - 1]:
    pro2.append(pro_k.pop())
    pd[-1] = 1
elif max_pro >= pro_k[k - 1]:
    pd[-1] = 3
    pd[pro_k[k - 1]] = 3
else:
    pd[-1] = 2
    pd[pro_k[k - 1]] = 1
# print(pd)

for i in range(n):
    if d[i] not in pd.keys():
        s = str(1)
    else:
        s = str(pd[d[i]])
    if i != n - 1:
        s += '\n'
    print(s, end='')
